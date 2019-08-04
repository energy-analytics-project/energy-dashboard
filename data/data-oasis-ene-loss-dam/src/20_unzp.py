#! /usr/bin/env python3

# -----------------------------------------------------------------------------
# 20_unzp.py : unzip raw resources to XML_DIR in preparation for injestion 
# -----------------------------------------------------------------------------
import os
import zipfile as zf
import logging

CWD         = os.path.abspath(os.path.curdir)
ZIP_DIR     = os.path.join(CWD, "zip")
XML_DIR     = os.path.join(CWD, "xml")
XML_MANIFEST= os.path.join(XML_DIR, "unzipped.txt")

# -----------------------------------------------------------------------------
# resource name
# -----------------------------------------------------------------------------
RESOURCE_NAME           = "data-oasis-ene-loss-dam"

def glob_dir(path, ending):
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file() and entry.name.lower().endswith(ending.lower()):
                yield(entry.name)

def new_zip_files():
    parsed_file_set = set()
    logging.info({
        "src":RESOURCE_NAME, 
        "action":"new_zip_files"})
    if os.path.exists(XML_MANIFEST):
        with open(XML_MANIFEST, 'r') as m:
            parsed_file_set = set([l.rstrip() for l in m])
    all_file_set = set(glob_dir(ZIP_DIR, "zip"))
    new_file_set = all_file_set - parsed_file_set
    logging.info({
        "src":RESOURCE_NAME, 
        "action":"new_zip_files", 
        "new_file_set_count":len(new_file_set), 
        "all_file_set_count": len(all_file_set), 
        "parsed_file_set_count": len(parsed_file_set)})
    return list(new_file_set)

def unzip(zip_files):
    unzipped = []
    for f in zip_files:
        try:
            with zf.ZipFile(os.path.join(ZIP_DIR, f), 'r') as t:
                for zip_item in t.namelist():
                    target_artifact = os.path.join(XML_DIR, zip_item)
                    if not os.path.exists(target_artifact):
                        t.extract(zip_item, XML_DIR)
                        logging.debug({
                            "src":RESOURCE_NAME, 
                            "action":"unzip",
                            "zip_file":f,
                            "zip_item":zip_item,
                            "msg": "item extracted"})
                    else:
                        logging.debug({
                            "src":RESOURCE_NAME, 
                            "action":"unzip",
                            "zip_file":f,
                            "zip_item":zip_item,
                            "msg": "item skipped (exists already)"})
            unzipped.append(f)
        except Exception as e:
            logging.error({
                "src":RESOURCE_NAME, 
                "action":"new_zip_files",
                "file":f,
                "error": e
                })
    return unzipped


def update_manifest(unzipped_files):
    with open(XML_MANIFEST, 'a') as m:
        for u in unzipped_files:
            m.write("%s\n" % u)


if __name__ == "__main__":
    logging.basicConfig(format='{"ts":%(asctime)s, "msg":%(message)s}', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    update_manifest(unzip(new_zip_files()))
