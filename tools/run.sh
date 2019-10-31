#! /bin/bash 
# should be run weekly (down.sh shoud be daily except when this is running)

LOG_LEVEL=${LOG_LEVEL:-INFO}

# keep downloads single threaded so as not to blow the caps at oasis
edc feeds list | xargs -L 1 -I {} edc --log-level ${LOG_LEVEL} feed {} proc down

# do all the heavy processing in parallel (run weekly as uploading to s3 buckets is currently pretty wasteful)
edc feeds list | shuf | parallel --max-procs 95% "edc --log-level ${LOG_LEVEL} feed {} proc unzip parse insert save dist arch"
