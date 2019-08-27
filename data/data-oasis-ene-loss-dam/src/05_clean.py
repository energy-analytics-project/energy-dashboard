#!/usr/bin/env python3

import os
import json
import logging
from edl.resources import filesystem as fs
from edl.resources import log
from edl.resources import state

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
    state_file = os.path.join("xml", "unzipped.txt")
    if os.path.exists(state_file):
        os.remove(state_file)
    state.update(clean_names_generator("zip"), state_file)

def clean_names_generator(path):
    for f in fs.glob_dir(path, ".zip"):
        try:
            clean_name = fs.clean_legacy_filename(f)
            os.rename(
                    os.path.join(path, f), 
                    os.path.join(path, clean_name))
            yield clean_name
        except:
            logging.error("unable to rename file: %s" % (f))

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    with open('manifest.json', 'r') as json_file:
        m = json.load(json_file)
        run(m, config())
