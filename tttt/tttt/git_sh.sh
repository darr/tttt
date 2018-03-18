#!/bin/sh


cd $1
git add ./$2
git status -s
git commit -m "add $2"
git push origin master
