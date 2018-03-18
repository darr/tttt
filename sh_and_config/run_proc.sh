#!/bin/sh
git_name="tttt_django"
proc_name="tttt"
server_name="www.iri8.com"
venv_name="$proc_name""_django_env"
user_name="liuzy"
proc_port="9648"
uwsgi_file_name=$proc_name$proc_port"_uwsgi.ini"
basepath=$(cd `dirname $0`; pwd)
venv_full_path=$basepath"/../$venv_name"
proc_full_path=$basepath"/../$proc_name"


function create_virtual_env_folder(){
if [ ! -d "$venv_full_path" ]; then
    virtualenv $venv_full_path --no-site-packages
    source $venv_full_path/bin/activate
    pip install Django==1.6.1
    pip install django-users2
else
    source $venv_full_path/bin/activate
   echo $venv_full_path folder exist
fi
}

function create_uwsgi_config_file(){
uwsgi_config_file="./$uwsgi_file_name"
echo "[uwsgi]" >$uwsgi_config_file
echo "daemonize = ./uwsgi.log" >>$uwsgi_config_file
echo "socket = 127.0.0.1:$proc_port" >>$uwsgi_config_file
echo "chdir = $proc_full_path" >>$uwsgi_config_file
echo "wsgi-file = $proc_name/wsgi.py" >>$uwsgi_config_file
echo "home = $venv_full_path" >>$uwsgi_config_file
}

function create_nginx_config_file(){
    nginx_config_file="./"$server_name".conf"
    echo -e " server {
        listen       80;
        server_name  $server_name;

        #charset koi8-r;
        access_log  /var/log/nginx/$server_name.access.log  main;
        error_log  /var/log/nginx/$server_name.error.log;

        location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:$proc_port;
        uwsgi_param UWSGI_CHDIR $proc_full_path;
        }
        location /static/{
        alias $proc_full_path/$proc_name/static/;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /usr/share/nginx/html;
        }
        } " >$nginx_config_file

}

function create_root_config_sh(){
    nginx_conf_file_name="$server_name"".conf"
    nginx_conf_file="./"$nginx_conf_file_name
    nginx_conf_path="/etc/nginx/conf.d/"
    nginx_conf_full_path=$nginx_conf_path$nginx_conf_file_name

    root_config_file="./root_config.sh"
    echo -e "#!/bin/sh

if [ ! -f $nginx_conf_full_path ]; then
    echo $nginx_conf_full_path file do not exist
    cp $nginx_conf_file $nginx_conf_full_path
else
   echo $nginx_conf_full_path file exist cover it
    cp $nginx_conf_file $nginx_conf_full_path
fi

service nginx restart
         " >$root_config_file
}

if [ ! -d "$venv_full_path" ]; then
    virtualenv $venv_full_path --no-site-packages
    source $venv_full_path/bin/activate
    pip install Django==1.6.1
    pip install django-users2
    pip install tornado
    pip install demjson
else
    source $venv_full_path/bin/activate
   echo $venv_full_path folder exist
fi

create_uwsgi_config_file
create_nginx_config_file
create_root_config_sh

if [ ! -d "$proc_full_path" ]; then
#       echo $1 folder do not exist
    cd ..
    django-admin.py startproject $proc_name
    cd sh_and_config
else
   echo $venv_full_path folder exist
fi

#uwsgi uwsgi.ini  $proc_name $proc_port
uwsgi $uwsgi_file_name

echo "root 运行 root_config.sh 配置nginx文件"
