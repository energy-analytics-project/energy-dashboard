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

    'sqlite DBNAME ".tables"'
    'sqlite DBNAME "PRAGMA table_info(TABLE_NAME)"
    'sqlite DBNAME "select count(*) from TABLE_NAME"
    'sqlite DBNAME "select * from TABLE_NAME LIMIT 10"

4. Create a Jupyter Notebook and wire in your data

    import sqlite3
    import pandas as pd
    import matplotlib.pyplot as plt
    from pandasql import sqldf
    # Create the connection
    cnx  = sqlite3.connect(r'../data/data-oasis-as-req-dam/db/caiso-oasis-as-req-dam.db')

5. See the [example notebooks](../notebooks) for further details
  * [OASIS AS_REQ (DAM)](../notebooks/oasis-as-req-dam.ipynb)
  * [OASIS AS_REQ (DAM) and FUEL_PRC](../notebooks/oasis-as-req-dam-and-fuel-prc.ipynb)
6. Science!

## Datasets


### CAISO OASIS

Note: there are about 50 more caiso oasis databases that are coming online, in addition to those listed here.

#### Dataset Documentation

1. [CAISO OASIS Interface Specification](./caiso/OASIS-InterfaceSpecification_v5_1_8Clean_Independent2019Release.pdf)
  * This document describes the available data feeds (called reports) and what the fields mean.
  * Each CAISO OASIS report is prefixed by 'data-oasis-' here
  * A report named FOO_BAZ_BAR would be named 'data-oasis-foo-baz-bar' here

#### Available Datasets

* [data-oasis-prc-mpm-rtm-nomogram-cmp-hasp](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-mpm-rtm-nomogram-cmp-hasp/db/data-oasis-prc-mpm-rtm-nomogram-cmp-hasp_00.db.gz)
* [data-oasis-atl-peak-on-off](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-peak-on-off/db/data-oasis-atl-peak-on-off_00.db.gz)
* [data-oasis-ene-eim-dyn-nsi-all-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-eim-dyn-nsi-all-all/db/data-oasis-ene-eim-dyn-nsi-all-all_00.db.gz)
* [data-oasis-atl-ruc-zone-map](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-ruc-zone-map/db/data-oasis-atl-ruc-zone-map_00.db.gz)
* [data-oasis-prc-cd-intvl-lmp](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-cd-intvl-lmp/db/data-oasis-prc-cd-intvl-lmp_00.db.gz)
* [data-oasis-cbd-nodal-grp-cnstr-prc](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-cbd-nodal-grp-cnstr-prc/db/data-oasis-cbd-nodal-grp-cnstr-prc_00.db.gz)
* [data-oasis-ene-cb-mkt-sum](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-cb-mkt-sum/db/data-oasis-ene-cb-mkt-sum_00.db.gz)
* [data-oasis-atl-cbnode](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-cbnode/db/data-oasis-atl-cbnode_00.db.gz)
* [data-oasis-prc-mpm-rtm-nomogram-hasp](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-mpm-rtm-nomogram-hasp/db/data-oasis-prc-mpm-rtm-nomogram-hasp_00.db.gz)
* [data-oasis-prc-cd-sptie-lmp](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-cd-sptie-lmp/db/data-oasis-prc-cd-sptie-lmp_00.db.gz)
* [data-oasis-atl-tiepoint](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-tiepoint/db/data-oasis-atl-tiepoint_00.db.gz)
* [data-oasis-atl-tiepoint](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-tiepoint/db/data-oasis-atl-tiepoint_01.db.gz)
* [data-oasis-prc-eim-gh-rtd](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-eim-gh-rtd/db/data-oasis-prc-eim-gh-rtd_00.db.gz)
* [data-oasis-prc-nomogram-dam](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-nomogram-dam/db/data-oasis-prc-nomogram-dam_00.db.gz)
* [data-oasis-as-mileage-calc-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-as-mileage-calc-all/db/data-oasis-as-mileage-calc-all_00.db.gz)
* [data-oasis-sld-fcst-dam](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-sld-fcst-dam/db/data-oasis-sld-fcst-dam_00.db.gz)
* [data-oasis-prc-dam-sch-cnstr-dam](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-dam-sch-cnstr-dam/db/data-oasis-prc-dam-sch-cnstr-dam_00.db.gz)
* [data-oasis-prc-cd-rtm-nomogram-rctm-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-cd-rtm-nomogram-rctm-all/db/data-oasis-prc-cd-rtm-nomogram-rctm-all_00.db.gz)
* [data-oasis-atl-sp-tie](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-sp-tie/db/data-oasis-atl-sp-tie_01.db.gz)
* [data-oasis-atl-sp-tie](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-sp-tie/db/data-oasis-atl-sp-tie_00.db.gz)
* [data-oasis-crr-clearing-all-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-crr-clearing-all-all/db/data-oasis-crr-clearing-all-all_00.db.gz)
* [data-oasis-prc-mpm-default-cmp-dam](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-mpm-default-cmp-dam/db/data-oasis-prc-mpm-default-cmp-dam_00.db.gz)
* [data-oasis-sld-sf-eval-dmd-fcst](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-sld-sf-eval-dmd-fcst/db/data-oasis-sld-sf-eval-dmd-fcst_00.db.gz)
* [data-oasis-sld-sf-eval-dmd-fcst](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-sld-sf-eval-dmd-fcst/db/data-oasis-sld-sf-eval-dmd-fcst_01.db.gz)
* [data-oasis-atl-gen-cap-lst](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-gen-cap-lst/db/data-oasis-atl-gen-cap-lst_00.db.gz)
* [data-oasis-atl-gen-cap-lst](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-gen-cap-lst/db/data-oasis-atl-gen-cap-lst_01.db.gz)
* [data-oasis-ene-disp](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-disp/db/data-oasis-ene-disp_00.db.gz)
* [data-oasis-atl-itc-sp](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-itc-sp/db/data-oasis-atl-itc-sp_00.db.gz)
* [data-oasis-as-req-dam](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-as-req-dam/db/data-oasis-as-req-dam_00.db.gz)
* [data-oasis-atl-pub-sched](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-pub-sched/db/data-oasis-atl-pub-sched_00.db.gz)
* [data-oasis-sld-fcst-peak](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-sld-fcst-peak/db/data-oasis-sld-fcst-peak_00.db.gz)
* [data-oasis-prc-mpm-rtm-flowgate-hasp-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-mpm-rtm-flowgate-hasp-all/db/data-oasis-prc-mpm-rtm-flowgate-hasp-all_00.db.gz)
* [data-oasis-prc-lmp](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-lmp/db/data-oasis-prc-lmp_00.db.gz)
* [data-oasis-ene-eim-transfer-limit-all-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-eim-transfer-limit-all-all/db/data-oasis-ene-eim-transfer-limit-all-all_00.db.gz)
* [data-oasis-prc-curr-hub-lmp](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-curr-hub-lmp/db/data-oasis-prc-curr-hub-lmp_00.db.gz)
* [data-oasis-ene-eim-flex-ramp-input-rtm](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-eim-flex-ramp-input-rtm/db/data-oasis-ene-eim-flex-ramp-input-rtm_00.db.gz)
* [data-oasis-prc-ds-ref](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-ds-ref/db/data-oasis-prc-ds-ref_00.db.gz)
* [data-oasis-as-results-dam](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-as-results-dam/db/data-oasis-as-results-dam_00.db.gz)
* [data-oasis-trns-outage-all-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-trns-outage-all-all/db/data-oasis-trns-outage-all-all_00.db.gz)
* [data-oasis-prc-flex-ramp-dam](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-flex-ramp-dam/db/data-oasis-prc-flex-ramp-dam_00.db.gz)
* [data-oasis-cmmt-rmr-dam](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-cmmt-rmr-dam/db/data-oasis-cmmt-rmr-dam_00.db.gz)
* [data-oasis-atl-tac-area-map](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-tac-area-map/db/data-oasis-atl-tac-area-map_00.db.gz)
* [data-oasis-ene-ea-all-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-ea-all-all/db/data-oasis-ene-ea-all-all_00.db.gz)
* [data-oasis-atl-osm-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-osm-all/db/data-oasis-atl-osm-all_01.db.gz)
* [data-oasis-atl-osm-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-atl-osm-all/db/data-oasis-atl-osm-all_00.db.gz)
* [data-oasis-ene-eim-transfer-limits-tie-rtd-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-eim-transfer-limits-tie-rtd-all/db/data-oasis-ene-eim-transfer-limits-tie-rtd-all_00.db.gz)
* [data-oasis-as-op-rsrv](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-as-op-rsrv/db/data-oasis-as-op-rsrv_00.db.gz)
* [data-oasis-prc-mpm-cnstr-cmp-dam](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-prc-mpm-cnstr-cmp-dam/db/data-oasis-prc-mpm-cnstr-cmp-dam_00.db.gz)
* [data-oasis-ene-baa-mkt-events-rtd-all](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-baa-mkt-events-rtd-all/db/data-oasis-ene-baa-mkt-events-rtd-all_00.db.gz)
* [data-oasis-ene-wind-solar-summary](https://s3.us-west-1.wasabisys.com/eap/energy-dashboard/data/data-oasis-ene-wind-solar-summary/db/data-oasis-ene-wind-solar-summary_00.db.gz)

