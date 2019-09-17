#! /bin/bash 

LOG_LEVEL=INFO

# sync local backup drive
rsync -av /mnt/PASSPORT/data/eap /mnt/DATABU/data/eap

# use just one process for downloading b/c of accepted use limits
# from caiso
# 
edc feeds list | xargs -L 1 -I {} edc feed {} proc download

# sync local backup drive
rsync -av /mnt/PASSPORT/data/eap /mnt/DATABU/data/eap

# spread the processing over multiple processors using 'parallel'.
#
edc feeds list | parallel --max-procs 50% edc --log-level ${LOG_LEVEL} feed {} status
edc feeds list | parallel --max-procs 50% edc --log-level ${LOG_LEVEL} feed {} proc unzip
edc feeds list | parallel --max-procs 50% edc --log-level ${LOG_LEVEL} feed {} proc parse
edc feeds list | parallel --max-procs 50% edc --log-level ${LOG_LEVEL} feed {} proc insert
edc feeds list | parallel --max-procs 50% edc --log-level ${LOG_LEVEL} feed {} s3archive --service wasabi
edc feeds list | parallel --max-procs 50% edc --log-level ${LOG_LEVEL} feed {} s3archive --service digitalocean

# sync local backup drive
rsync -av /mnt/PASSPORT/data/eap /mnt/DATABU/data/eap
