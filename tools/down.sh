#! /bin/bash 

LOG_LEVEL=${LOG_LEVEL:-INFO}

# keep downloads single threaded so as not to blow the caps at oasis
edc feeds list | xargs -L 1 -I {} edc --log-level ${LOG_LEVEL} feed {} proc down
