DB=$1

do_sql(){
    SQL=$1
    sqlite3 $DB "$SQL"
    if [ "$?" != "0" ]; then
      echo "BADDB_:$DB:$SQL" 
    else
      echo "GOODDB:$DB" 
    fi
}

do_sql "select count(*) from report_data;"
do_sql "select count(*) from report_data where report_data.value > 0;"
