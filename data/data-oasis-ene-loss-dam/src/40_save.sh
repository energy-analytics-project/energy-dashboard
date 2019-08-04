#! /bin/bash
set -x

git add xml/
git add db/
git commit -am "update db"
git push
