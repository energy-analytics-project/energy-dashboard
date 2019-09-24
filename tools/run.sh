#! /bin/bash 

LOG_LEVEL=${LOG_LEVEL:-INFO}

# keep downloads single threaded so as not to blow the caps at oasis
edc feeds list | xargs -L 1 -I {} edc --log-level ${LOG_LEVEL} feed {} proc down

# spread the remaining processing over multiple processors using 'parallel'.
edc feeds list | parallel --max-procs 90% "edc --log-level ${LOG_LEVEL} feed {} status"
edc feeds list | parallel --max-procs 90% "edc --log-level ${LOG_LEVEL} feed {} proc all"
edc feeds list | parallel --max-procs 90% "edc --log-level ${LOG_LEVEL} feed {} status"
