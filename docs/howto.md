# HowTo

## Create a Jupyter Notebook

1. Download Data
  * Select one or more of the available databases below
  * Click the links with your browser, or use curl, or wget, whatever.
2. Decompress the Database(s)
  * the dataset locally on your machine
  * Use any tooling that can decompress gzip files (gzip, pigz, etc.)
3. Verify the database
  * Use sqlite to run some queries on the database
  * Noodle around a bit to get a feel for what you have and how it's structured
```sqlite3
sqlite DBNAME ".tables"
sqlite DBNAME "PRAGMA table_info(TABLE_NAME)"
sqlite DBNAME "select count(*) from TABLE_NAME"
sqlite DBNAME "select * from TABLE_NAME LIMIT 10"
```
4. Create a Jupyter Notebook and wire in your data
```python3
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pandasql import sqldf
# Create the connection
cnx  = sqlite3.connect(r'../data/data-oasis-as-req-dam/db/caiso-oasis-as-req-dam.db')
```
5. See the [example notebooks](../notebooks) for further details
  * [OASIS AS_REQ (DAM)](../notebooks/oasis-as-req-dam.ipynb)
  * [OASIS AS_REQ (DAM) and FUEL_PRC](../notebooks/oasis-as-req-dam-and-fuel-prc.ipynb)
6. Science!

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
