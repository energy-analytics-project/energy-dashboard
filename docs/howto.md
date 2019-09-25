# HowTo

## Prepare to Create a Jupyter Notebook

### Overview

1. Install Dependencies
  * [conda](https://www.anaconda.com/distribution/#download-section)
  * [sqlite3](https://sqlite.org/index.html)
  * [jupyter](https://jupyter.readthedocs.io/en/latest/install.html)
  * [more jupyter](https://jupyter.org/install)
  * [pigz](https://zlib.net/pigz/)

1. Create a conda environment with 
  * [tutorial](https://geohackweek.github.io/Introductory/01-conda-tutorial/)

### Example

These instructions are for ubuntu. See the link above for instructions specific
to your operating system.

#### Install Dependencies

##### conda

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
chmod +x Anaconda3-2019.07-Linux-x86_64.sh 
./Anaconda3-2019.07-Linux-x86_64.sh 
```

##### sqlite3 and pigz

Note: pigz isn't necessary, you can always use gzip/gunzip... but pigz uses
all your cores, so why not?

```bash
sudo apt install sqlite3 pigz
```

#### Environment

Create a conda environment, it can be named anything, I'll call
this `edc-cli`. The environment will come with jupyter already
installed...

```bash
conda update conda
conda create -n edc-cli python=3 numpy jupyter pandas pandasql
conda activate edc-cli
```

Ok, we are ready to create a notebook!

## Create a Jupyter Notebook

### Overiew

1. Download Data
  * Select one or more of the available databases below
  * Click the links with your browser, or use curl, or wget, whatever.
1. Decompress the Database(s)
  * the dataset locally on your machine
  * Use any tooling that can decompress gzip files (gzip, pigz, etc.)
1. Verify the database
  * Use sqlite3 to run some queries on the database
  * Noodle around a bit to get a feel for what you have and how it's structured
```bash
sqlite3 {{DBNAME}} ".tables"
sqlite3 {{DBNAME}} "PRAGMA table_info({{TABLE_NAME}})"
sqlite3 {{DBNAME}} "select count(*) from {{TABLE_NAME}}"
sqlite3 {{DBNAME}} "select * from {{TABLE_NAME}} LIMIT 10"
```
1. Create a Jupyter Notebook and wire in your data
```python3
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pandasql import sqldf
# Create the connection
cnx  = sqlite3.connect(r'{{DBNAME}}')
```

### Example

#### Download Data

```bash
curl --limit-rate 10M https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-wind-solar-summary/db/data-oasis-ene-wind-solar-summary_00.db.gz -o data-oasis-ene-wind-solar-summary_00.db.gz
```

#### Decompress the Database(s)

```bash
pigz -d data-oasis-ene-wind-solar-summary_00.db.gz
```
or use gzip

```bash
gunzip data-oasis-ene-wind-solar-summary_00.db.gz
```

#### Verify the database

What tables does this report have?

```bash
$ sqlite3 data-oasis-ene-wind-solar-summary_00.db ".tables"

disclaimer_item  messagepayload   report_header
error            oasisreport      report_item
messageheader    report_data      rto
```

What does each table look like?

```bash
sqlite3 data-oasis-ene-wind-solar-summary_00.db "PRAGMA table_info(report_item)"
0|id|TEXT|0||1
1|rto_name|TEXT|0||0

sqlite3 data-oasis-ene-wind-solar-summary_00.db "PRAGMA table_info(report_data)"
0|data_item|TEXT|0||1
1|interval_end_gmt|TEXT|0||2
2|interval_start_gmt|TEXT|0||3
3|value|INTEGER|0||4
4|opr_date|TEXT|0||5
5|report_item_id|TEXT|0||0

sqlite3 data-oasis-ene-wind-solar-summary_00.db "PRAGMA table_info(report_header)"
0|report|TEXT|0||1
1|system|TEXT|0||2
2|sec_per_interval|INTEGER|0||3
3|uom|TEXT|0||4
4|interval|TEXT|0||5
5|tz|TEXT|0||6
6|mkt_type|TEXT|0||7
7|report_item_id|TEXT|0||0
```

What does some sample data look like?

```bash
sqlite3 data-oasis-ene-wind-solar-summary_00.db "select * from report_item limit 2"
45a7b62a-987b-4ac7-a131-29aab2850b0e|CAISO
8e47de63-00e1-446e-8586-825c6b6f001a|CAISO

sqlite3 data-oasis-ene-wind-solar-summary_00.db "select * from report_data limit 2"
DAM_FORECAST|2016-10-17T11:00:00-00:00|2016-10-17T10:00:00-00:00|2556|2016-10-17|45a7b62a-987b-4ac7-a131-29aab2850b0e
DAM_FORECAST|2016-10-17T22:00:00-00:00|2016-10-17T21:00:00-00:00|9409|2016-10-17|45a7b62a-987b-4ac7-a131-29aab2850b0e

sqlite3 data-oasis-ene-wind-solar-summary_00.db "select * from report_header limit 2"
ENE_WIND_SOLAR_SUMMARY|OASIS|3600|MW|ENDING|PPT|DAM|45a7b62a-987b-4ac7-a131-29aab2850b0e
ENE_WIND_SOLAR_SUMMARY|OASIS|300|MW|ENDING|PPT|RTD|61665051-e88b-4971-a3a5-6915bd2993e1
``

The tables are joined by UUIDs. Both report_header and report_data are joined to their 'parent' table, report_item, by 'report_item_id'.

In fact, if you want to see all the DDL for creating the tables, this will do it:

```bash
$ sqlite3 data-oasis-ene-wind-solar-summary_00.db ".dump" | grep CREATE
CREATE TABLE oasisreport (id TEXT, PRIMARY KEY (id));
CREATE TABLE messageheader (source TEXT, version TEXT, timedate TEXT, oasisreport_id TEXT, FOREIGN KEY (oasisreport_id) REFERENCES oasisreport(id), PRIMARY KEY (source, version, timedate));
CREATE TABLE messagepayload (id TEXT, oasisreport_id TEXT, FOREIGN KEY (oasisreport_id) REFERENCES oasisreport(id), PRIMARY KEY (id));
CREATE TABLE rto (name TEXT, messagepayload_id TEXT, FOREIGN KEY (messagepayload_id) REFERENCES messagepayload(id), PRIMARY KEY (name));
CREATE TABLE report_item (id TEXT, rto_name TEXT, FOREIGN KEY (rto_name) REFERENCES rto(name), PRIMARY KEY (id));
CREATE TABLE report_header (report TEXT, system TEXT, sec_per_interval INTEGER, uom TEXT, interval TEXT, tz TEXT, mkt_type TEXT, report_item_id TEXT, FOREIGN KEY (report_item_id) REFERENCES report_item(id), PRIMARY KEY (report, system, sec_per_interval, uom, interval, tz, mkt_type));
CREATE TABLE report_data (data_item TEXT, interval_end_gmt TEXT, interval_start_gmt TEXT, value INTEGER, opr_date TEXT, report_item_id TEXT, FOREIGN KEY (report_item_id) REFERENCES report_item(id), PRIMARY KEY (data_item, interval_end_gmt, interval_start_gmt, value, opr_date));
CREATE TABLE disclaimer_item (disclaimer TEXT, rto_name TEXT, FOREIGN KEY (rto_name) REFERENCES rto(name), PRIMARY KEY (disclaimer));
CREATE TABLE error (err_code INTEGER, err_desc TEXT, rto_name TEXT, FOREIGN KEY (rto_name) REFERENCES rto(name), PRIMARY KEY (err_code, err_desc));
```

#### Create a notebook
#### Add the database
#### Display some data
#### Display charts




## Further reading
1. See the [example notebooks](../notebooks) for further details
  * [OASIS AS_REQ (DAM)](../notebooks/oasis-as-req-dam.ipynb)
  * [OASIS AS_REQ (DAM) and FUEL_PRC](../notebooks/oasis-as-req-dam-and-fuel-prc.ipynb)
1. Science!

## Datasets

### CAISO OASIS

Note: there are more than 60 caiso oasis databases that are coming online shortly, in addition to those listed here.

#### Dataset Documentation

1. [CAISO OASIS Interface Specification](./caiso/OASIS-InterfaceSpecification_v5_1_8Clean_Independent2019Release.pdf)
  * This document describes the available data feeds (called reports) and what the fields mean.
  * Each CAISO OASIS report is prefixed by 'data-oasis-' here
  * A report named FOO_BAZ_BAR would be named 'data-oasis-foo-baz-bar' here

#### Available Datasets

* [data-oasis-atl-ruc-zone-map](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-ruc-zone-map/db/data-oasis-atl-ruc-zone-map_00.db.gz)
* [data-oasis-cbd-nodal-grp-cnstr-prc](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-cbd-nodal-grp-cnstr-prc/db/data-oasis-cbd-nodal-grp-cnstr-prc_00.db.gz)
* [data-oasis-as-mileage-calc-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-as-mileage-calc-all/db/data-oasis-as-mileage-calc-all_00.db.gz)
* [data-oasis-prc-cd-rtm-nomogram-rctm-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-cd-rtm-nomogram-rctm-all/db/data-oasis-prc-cd-rtm-nomogram-rctm-all_00.db.gz)
* [data-oasis-atl-sp-tie](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-sp-tie/db/data-oasis-atl-sp-tie_01.db.gz)
* [data-oasis-atl-sp-tie](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-sp-tie/db/data-oasis-atl-sp-tie_00.db.gz)
* [data-oasis-ene-eim-transfer-limit-all-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-eim-transfer-limit-all-all/db/data-oasis-ene-eim-transfer-limit-all-all_00.db.gz)
* [data-oasis-prc-curr-hub-lmp](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-curr-hub-lmp/db/data-oasis-prc-curr-hub-lmp_00.db.gz)
* [data-oasis-prc-ds-ref](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-ds-ref/db/data-oasis-prc-ds-ref_00.db.gz)
* [data-oasis-as-results-dam](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-as-results-dam/db/data-oasis-as-results-dam_00.db.gz)
* [data-oasis-cmmt-rmr-dam](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-cmmt-rmr-dam/db/data-oasis-cmmt-rmr-dam_00.db.gz)
* [data-oasis-as-op-rsrv](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-as-op-rsrv/db/data-oasis-as-op-rsrv_00.db.gz)
* [data-oasis-prc-mpm-cnstr-cmp-dam](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-mpm-cnstr-cmp-dam/db/data-oasis-prc-mpm-cnstr-cmp-dam_00.db.gz)
* [data-oasis-ene-baa-mkt-events-rtd-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-baa-mkt-events-rtd-all/db/data-oasis-ene-baa-mkt-events-rtd-all_00.db.gz)
* [data-oasis-ene-wind-solar-summary](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-wind-solar-summary/db/data-oasis-ene-wind-solar-summary_00.db.gz)
