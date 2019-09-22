#!/bin/bash

FILE=$1

cat ${FILE} | sqlite3
if [ "$?" != "0" ]; then
  echo "__BADSQL__ : ${FILE}" 
else
  echo "GOODSQL : ${FILE}" 
fi
