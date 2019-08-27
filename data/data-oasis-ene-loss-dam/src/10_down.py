#! /usr/bin/env python3

# -----------------------------------------------------------------------------
# 10_down.py : download resources from resource_url
# 
# * after downloading, resource urls are appended to zip/downloaded.txt
# * zip/downloaded.txt can be checked into the repo, whereas the the downloaded
#   resources should not be checked in to git. Instead, they are uploaded to
#   an S3 bucket 'eap'.
# -----------------------------------------------------------------------------

import datetime
import requests
import sys
import os
import time
import logging
import json
from edl.resources import state
from edl.resources import log
from edl.resources import web
from edl.resources import time as xtime


# -----------------------------------------------------------------------------
# Config
# -----------------------------------------------------------------------------
def config():
    """
    config = {
            "source_dir"    : not used
            "working_dir"   : location to download zip files
            "state_file"    : fqpath to file that lists downloaded zip files
            }
    """
    cwd                     = os.path.abspath(os.path.curdir)
    zip_dir                 = os.path.join(cwd, "zip")
    state_file              = os.path.join(zip_dir, "downloaded.txt")
    config = {
            "working_dir"   : zip_dir,
            "state_file"    : state_file
            }
    return config

# -----------------------------------------------------------------------------
# Entrypoint
# -----------------------------------------------------------------------------
def run(manifest, config, logging_level=logging.INFO):
    log.configure_logging(logging_level)
    start_date      = datetime.date(*manifest['start_date'])
    resource_name   = manifest['name']
    resource_url    = manifest['url']
    download_dir    = config['working_dir']
    state_file      = config['state_file']
    # sleep for 5 seconds in between downloads to meet caiso expected use requirements
    delay = 5
    state.update(
            web.download(
                resource_name,
                delay,
                web.generate_urls(
                    xtime.range_pairs(xtime.day_range_to_today(start_date)),
                    resource_url),
                state_file,
                download_dir),
            state_file
            )

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    with open('manifest.json', 'r') as json_file:
        m = json.load(json_file)
        run(m, config())
