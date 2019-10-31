#! /bin/bash 

LOG_LEVEL=${LOG_LEVEL:-INFO}

# final wrap up
edc feeds list | xargs -L 1 -I {} edc --log-level ${LOG_LEVEL} feed {} proc dist arch
