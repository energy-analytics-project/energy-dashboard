#!/usr/bin/env python3

import os
import json
import logging
from edl.resources import filesystem as fs
from edl.resources import log
from edl.resources import state
from edl.resources import bucket

# -----------------------------------------------------------------------------
# Config
# -----------------------------------------------------------------------------
def config():
    """
    config = {
            "source_dir"    : not used
            "working_dir"   : not used
            "state_file"    : not used
            }
    """
    config = {
            }
    return config

# -----------------------------------------------------------------------------
# Entrypoint
# -----------------------------------------------------------------------------
def run(manifest, config, logging_level=logging.INFO):
    log.configure_logging(logging_level)
    resource_name   = manifest['name']
    bucket.sync(resource_name)

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    with open('manifest.json', 'r') as json_file:
        m = json.load(json_file)
        run(m, config())
