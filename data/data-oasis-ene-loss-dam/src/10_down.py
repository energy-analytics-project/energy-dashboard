#! /usr/bin/env python3

# -----------------------------------------------------------------------------
# 10_down.py : download resources from RESOURCE_URL
# 
# * after downloading, resource urls are appended to zip/downloaded.txt
# * zip/downloaded.txt can be checked into the repo, whereas the the downloaded
#   resources should not be checked in
# * RESOURCE_URL has two replacements, _START_, and _END_, each formatted as
#   YYYYmmdd
# -----------------------------------------------------------------------------

import datetime
import requests
import sys
import os
import time
import logging

# most oasis reports seem to start in 2013
START_DATE              = datetime.date(2013,1,1)
CWD                     = os.path.abspath(os.path.curdir)
ZIP_DIR                 = os.path.join(CWD, "zip")
DOWNLOADED_MANIFEST     = os.path.join(ZIP_DIR, "downloaded.txt")

# -----------------------------------------------------------------------------
# resource name
# -----------------------------------------------------------------------------
RESOURCE_NAME           = "data-oasis-ene-loss-dam"

# -----------------------------------------------------------------------------
# resource url
# -----------------------------------------------------------------------------
RESOURCE_URL            = "http://oasis.caiso.com/oasisapi/SingleZip?queryname=ENE_LOSS&market_run_id=DAM&startdatetime=_START_T07:00-0000&enddatetime=_END_T07:00-0000&version=1"

def days():
    start_date  = START_DATE
    end_date    = datetime.datetime.now().date()
    days        = [start_date + datetime.timedelta(n) for n in range(int ((end_date - start_date).days))]
    return sorted(days)

def pairs(days):
    start = days[:-1]
    end = days[1:]
    return zip(start,end)

def urls(day_pairs, url_template):
    for (start, end) in day_pairs:
        s = start.strftime("%Y%m%d")
        e = end.strftime("%Y%m%d")
        yield url_template.replace("_START_", s).replace("_END_", e)

def file_name(url):
        s = url.replace("http://oasis.caiso.com/oasisapi/", "oasis:")\
                .replace("/", "_")\
                .replace("&", ":")\
                .replace("SingleZip", "SZ")\
                .replace("queryname", "q")\
                .replace("startdatetime", "sdt")\
                .replace("enddatetime", "edt")\
                .replace("market_run_id", "mri")\
                .replace("version", "v")
        return("%s.zip" % s)

def download(urls):
    downloaded = []
    m = set()
    if os.path.exists(DOWNLOADED_MANIFEST):
        with open(DOWNLOADED_MANIFEST, "r") as f:
            m = set([line.rstrip() for line in f])
    for url in urls:
        try:
            filename = file_name(url)
            target = os.path.join("zip", filename)
            if url in m:
                logging.info({
                    "src":RESOURCE_NAME, 
                    "action":'skip_download', 
                    "url":url, 
                    "file":target, 
                    "msg":'url exists in download manifest'})
                continue
            if os.path.exists(target):
                logging.info({
                    "src":RESOURCE_NAME, 
                    "action":'skip_download', 
                    "url":url, 
                    "file":target, 
                    "msg":'file exists locally, updating manifest'})
                downloaded.append(url)
                continue
            # url does not exist in manifest and the target file does not exist on disk, download it
            r = requests.get(url)
            if r.status_code == 200:
                with open(target, 'wb') as fd:
                    for chunk in r.iter_content(chunk_size=128):
                        fd.write(chunk)
                downloaded.append(url)
                logging.info({
                    "src":RESOURCE_NAME, 
                    "action":'download', 
                    "url":url, 
                    "file":target})
            else:
                logging.error({
                    "src":RESOURCE_NAME, 
                    "action":'download', 
                    "url":url, 
                    "file":target,
                    "status_code":r.status_code,
                    "error":'http_reuqest_failed'})
        except Exception as e:
            logging.error({
                "src":RESOURCE_NAME, 
                "action":'download', 
                "url":url, 
                "error":e})
        # sleep for 5 seconds in between downloads to meet caiso expected use requirements
        time.sleep(5)
    return downloaded

def update_manifest(urls):
    for url in urls:
        with open(DOWNLOADED_MANIFEST, "a") as f:
            f.write("%s\n" % url)

if __name__ == "__main__":
    logging.basicConfig(format='{"ts":%(asctime)s, "msg":%(message)s}', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    update_manifest(download(urls(pairs(days()), RESOURCE_URL)))
