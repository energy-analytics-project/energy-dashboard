#! /bin/bash
# -----------------------------------------------------------------------------
# 10_fetch.sh : fetch resources (sqlite dbs)
# -----------------------------------------------------------------------------
set -x
# -----------------------------------------------------------------------------
# download() [URL] [DB] [OWNER}
#
# Download remote artifacts (sqlite databases) locally.
# 
#
# 
# Notes:
#           curl -z URL db/[LOCAL_DB_NAME]
# 
# * curl    : used for downloading b/c it is such a full featured client
# * curl -s : for silent mode (no progress bar)
# * curl -S : show errors
# * curl -z : attempt to only download resources that are newer than existing
#             resources.
# * URL     : resource url
# * LOCAL_DB_NAME: name of the local database (do not clobber one another)
# -----------------------------------------------------------------------------
download(){
    URL=$1
    DB=$2
    OWNER=$3
    curl -s -S -z data/${DB} ${URL} -o data/${DB}
    if [ $? == "0" ]; then
        echo "{date=\"`date -I`\",msg=\"success\", db=\"${DB}\", owner=\"${OWNER}\", url=\"${URL}\"}"
    else
        echo "{date=\"`date -I`\",msg=\"error\", db=\"${DB}\", owner=\"${OWNER}\", url=\"${URL}\"}"
    fi
}

# download URL
# currently using submodules for resources that are on github
# add items here that cannot be included via submodules
#download [SOME RESOURCE URL] [SOME DB NAME] "SOME USER NAME <USER@email.com>"


# update the submodules
git submodule update --recursive

# fetch and save any new data 
for m in $(ls data/data* -ad); do cd $m && make proc; done

# update the submodules
git submodule update --recursive
