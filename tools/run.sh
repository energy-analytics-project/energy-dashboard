#! /bin/bash 

LOG_LEVEL=INFO


# spread the processing over multiple processors using 'parallel'.
#
edc feeds list | parallel --max-procs 50% edc --log-level ${LOG_LEVEL} feed {} status
edc feeds list | parallel --max-procs 50% edc --log-level ${LOG_LEVEL} feed {} proc unzip
edc feeds list | parallel --max-procs 50% edc --log-level ${LOG_LEVEL} feed {} proc parse
edc feeds list | parallel --max-procs 50% edc --log-level ${LOG_LEVEL} feed {} proc insert

# the s3 buckets will complain if hit too hard, so don't run this in parallel, run
# it sequentially...
#
#edc feeds list | xargs -L 1 -I {} edc --log-level ${LOG_LEVEL} feed {} s3archive --service wasabi
#edc feeds list | xargs -L 1 -I {} edc --log-level ${LOG_LEVEL} feed {} s3archive --service digitalocean
