#! /bin/bash 

LOG_LEVEL=${LOG_LEVEL:-INFO}

# do all the heavy processing in parallel
edc feeds list | shuf | parallel --max-procs 95% "edc --log-level ${LOG_LEVEL} feed {} proc unzip parse insert save"
