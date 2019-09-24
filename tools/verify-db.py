#!/usr/bin/env python3

import sys
import fileinput
import requests
import pdb

def check(line):
    """
    >>> check("https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-mpm-rtm-nomogram-cmp-hasp/db/data-oasis-prc-mpm-rtm-nomogram-cmp-hasp_00.db.gz")
    https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-mpm-rtm-nomogram-cmp-hasp/db/data-oasis-prc-mpm-rtm-nomogram-cmp-hasp_00.db.gz"
    
    >>> check("https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-wind-solar-summary/db/data-oasis-ene-wind-solar-summary_00.db.gz")
    https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-wind-solar-summary/db/data-oasis-ene-wind-solar-summary_00.db.gz
    """
    result = requests.head(line)
    if result.status_code == 200:
        print("%s" % line)
    else:
        sys.stderr.write("{'code': %d, 'url': '%s'}\n" % (result.status_code, line))

def do_something(line):
    if check(line):
        print("%s\n" % line)

def main():
    for line in fileinput.input():
        line = line.rstrip().lstrip()
        do_something(line)

if __name__== "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "d":
        import doctest
        doctest.testmod()
    else:
        main()
