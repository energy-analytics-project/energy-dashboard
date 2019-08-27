# Energy Dashboard Architecture (EDA)

## Overview

This project is intended to be used and extended by programmers, users, and data-scientists.

## Technologies

* Python3           :: what data-scientists often use means easy adoption
* Jupyter Notebooks :: again, what data-scientists often use means easy adoption
* Sqlite3           :: simple well known abstraction layer (SQL) and easy to use from Python
* Github            :: cheap and easy distribution platform that live renders Jupyter Notebooks
* S3 buckets        :: cheap and ubiquitous archival, also easy to integrate with

## Components

ED is composed of the following components:

* Energy Dashboard (ED)
* Data Source Template (DST)
* Energy Dashboard Client (EDC)
* Energy Dashboard Library (EDL)
* Data Sources (also called Reports, Feeds, etc.)

### Energy Dashboard

https://github.com/energy-analytics-project/energy-dashboard.git

* Top level parent project
* Collection of data feed definitions, implemented as submodules
* Common documentation

### Data Source Template (DST)

https://github.com/energy-analytics-project/data-source-template.git

Data sources are defined by a git repo that contains:

    data/REPORT_NAME
    ├── db
    │   ├── REPORT_NAME.db
    │   └── inserted.txt
    ├── LICENSE
    ├── Makefile
    ├── manifest.json
    ├── README.md
    ├── src
    │   ├── 05_clean.py
    │   ├── 10_down.py
    │   ├── 20_unzp.py
    │   ├── 30_inse.py
    │   ├── 40_save.sh
    │   └── 50_sync.py
        ├── downloaded.txt

At a high level, using a template repo to generate data source repos yields the following benefits:

* standardized data source repos
* programatic access to important metadata via `manifest.json`
* standardized run scripts in `src/` that may have custom logic but that
  largely call into the EDL for heavy lifting
* use of state files like `downloaded.txt` and `inserted.txt` allows for:
  * resuming the work by simply re-running the python script `XX_foo.py`, and
    it will continue to append to the state file
  * completely restarting the process by deleting the state file and any
    related artifacts
  * trivial upgrade path to a true worflow engine such as `Apache Airflow`
    should that ever become necessary  

Historically the `src/XX_foo.py` files were run by `energy-dashboard/Makefile`,
but that has been deprecated and orchestration logic is now (or will be) in the
EDC/EDL. Note that such a simple pattern allows for other ways to orchestrate
the system, such as:

    ```bash
    cd energy-dashboard
    # for a in $(ls data); do pushd energy-dashboard/data/$a; [RUN SOME COMMAND]; popd; done
    for a in $(ls data); do pushd energy-dashboard/data/$a; ./src/10_down.py; popd; done
    ```

Historically, the repos were created with a Makefile command:

    ```make
    .PHONY: new
    new:
            src/create_data_source.sh "$(repo)" "$(owner)" "$(company)" "$(email)" "$(url)"
    ```

TODO: document creating a repo in the new system.


### Energy Dashboard Client (EDC)

https://github.com/energy-analytics-project/energy-dashboard-client.git

A Python3 Click based Command Line Interface for managing data sources,
creating notebooks, etc.


### Energy Dashboard Library (EDL)

https://github.com/energy-analytics-project/energy-dashboard-library.git

A Python3 library. This is where all the actual code lives for managing the
repos and datasources, creating notebooks, mirroring to S3 buckets, etc. Both
the individual data source repos `src/XX_foo.py` files and the EDC import and
use the EDL.


### Data Sources/Reports/Feeds ### Data Sources

https://github.com/energy-analytics-project/energy-dashboard/data

* CAISO OASIS : 91 data reports, totalling over 1 million time-series data points

The data sources are defined as git submodules here: [data sources](./data).
Each submodule contains a `manifest.json` that describes the report and the
database. The manifest is used to programatically generate new Jupyter
Notebooks. Also within each submodule is a list of state files that describe
exactly what has been downloaded, as well as the final database artifact which
should be stored via git lfs.

There are reasons for structuring the project this way:

* Github.com can render Jupyter Notebooks that reference Sqlite databases in
  both the main repo _and_ in git submodules
* Separating each report into a separate repo is great for isolation of
  concerns and limiting the blast radius of a poorly performing report

### Mirrors

Due to throttling by CAISO, it took several weeks to download the base set of 91
reports. You can either use the ED curated databases, or download the raw
data from one of the mirrors that ED publishes to:

* http://eap.s3.us-west-1.wasabisys.com
* https://eap.sfo2.digitaloceanspaces.com

Soon the EDC will have commands to help download the report files from either
the original source, in this case CAISO OASIS, or one of the mirrors (Wasabi or
Digital Ocean).


## Goals

### Reproducible and Extensible

The source artifacts are mirrored to S3 buckets primarily so that anyone can
reproduce these results and/or create their own ETL/pipeline and create their
own custom data store. For instance, because the source artifacts are mirrored,
one could easily write an ETL that would inject all of the records into a
different database (say postgres), use normalized table definitions, or use a
completely different table structure than the one I used.

### Programable

Using standardized patterns allows for programmatic access of the data stores. To enable this, I am doing the
following:

* transform the raw XML data into something like:

    ```bash
    [HEADER_COLUMNS] [UOM] [START] [STOP] [VALUE]
    ```

* HEADER_COLUMNS maintain unique constraints, allowing for re-running the db
  injestion pipeline to be essentially idempotent (runs subsequent to the
  initial run have no effect)
* UOM defines the data type for the value, useful for graphing, etc.
* START/STOP determine the time duration a value was held
* VALUE a float value

This simple model isn't quite programmable b/c it's not known what the
HEADER_COLUMNS are, etc. The information necessary to make this programmable is
stored in the `manifest.json`, which contains fields such as:

* ddl_create
* sql_insert
* sql_queries

NOTE: it's unclear if this is enough metadata. The proof will be if the EDC can
generate Jupyter Notebooks from arbitrary combinations of data sources.

