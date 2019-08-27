# How To Guide

How to contribute, create a notebook, download resources, etc!

## Organization

This repo is organized at the top level as:

* [tools](./docs/tools.md)
* [data](./docs/data.md)
* [docs](./docs/docs.md)
* [notebooks](./docs/notebooks.md)

## How To ...

### Install Prerequisites

* Anaconda
    * Python3
    * Jupyter Notebooks

### Add a notebook

I'd suggest copying one of the existing notebooks. Here are
a few of the resources I've been using while creating this 
project:

* https://docs.python.org/2/library/sqlite3.html
* https://github.com/ToddG/experimental/blob/master/interview-questions/glassdoor/sorting/erlang/sortz/docs/sorting_algorithms_analysis.ipynb
* https://medium.com/analytics-vidhya/programming-with-databases-in-python-using-sqlite-4cecbef51ab9
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html#pandas.DataFrame.resample
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html
* https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
* https://pypi.org/project/pysqldf/
* https://sqlite.org/lang_select.html
* https://tech.marksblogg.com/sqlite3-tutorial-and-guide.html
* https://towardsdatascience.com/basic-time-series-manipulation-with-pandas-4432afee64ea
* https://www.dataquest.io/blog/python-pandas-databases/
* http://www.sqlitetutorial.net/


### Add a data-set

```bash
$ make help
```

```bash
# -----------------------------------------------------------------------------
# Import datasets into the energy-dashboard
#
# Targets:
#
# 	daily 	: fetch and save resources
# 	fetch	: fetch (curl/copy) resources to ./data
#	save	: save resources to backing store (git)
#	new	: create new datasource repo [args=name]
#		  e.g. make new repo="data-AAA-BBB-CCC" owner="Todd Greenwood-Geer" 
#                    company="Enviro Software Solutions, LLC" email="pub+github@zwrob.com"
#
# Created by:
# Todd Greenwood-Geer <pub+github@zwrob.com>
# Enviro Software Solutions, LLC
# -----------------------------------------------------------------------------
```

Only the `new` target is useful for non-maintainers of this repo. The `new` target
generates a new data repository project from a template git repo.


Command
```bash
make new repo="data-AAA-BBB-CCC" owner="Todd Greenwood-Geer" company="Enviro Software Solutions, LLC" email="pub+github@zwrob.com"
```

Output
```bash
make[1]: Entering directory '/home/toddg/repos/eap/energy-dashboard'
src/create_data_source.sh "data-AAA-BBB-CCC" "Todd Greenwood-Geer" "Enviro Software Solutions, LLC" "pub+github@zwrob.com"
----------------------------------------------------
Usage: REPO OWNER COMPANY EMAIL

TEMPLATE VARS:

  REPO=data-AAA-BBB-CCC
  YEAR=2019
  DATA_SOURCE_NAME=data-AAA-BBB-CCC
  OWNER=Todd Greenwood-Geer
  COMPANY=Enviro Software Solutions, LLC
  EMAIL=pub+github@zwrob.com
----------------------------------------------------
downloading template repo to: .temp-data-source-template
Cloning into '.temp-data-source-template'...
remote: Enumerating objects: 49, done.
remote: Counting objects: 100% (49/49), done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 49 (delta 18), reused 42 (delta 14), pack-reused 0
Receiving objects: 100% (49/49), 16.41 KiB | 4.10 MiB/s, done.
Resolving deltas: 100% (18/18), done.
copying repo: data-AAA-BBB-CCC
updating template vars: data-AAA-BBB-CCC
processing : data-AAA-BBB-CCC/LICENSE
processing : data-AAA-BBB-CCC/Makefile
processing : data-AAA-BBB-CCC/README.md
processing : data-AAA-BBB-CCC/src/10_down.py
processing : data-AAA-BBB-CCC/src/20_unzp.py
processing : data-AAA-BBB-CCC/src/30_inse.py
processing : data-AAA-BBB-CCC/src/40_save.sh
processing : data-AAA-BBB-CCC/manifest.json
~/repos/eap/energy-dashboard/data-AAA-BBB-CCC ~/repos/eap/energy-dashboard
Initialized empty Git repository in /home/toddg/repos/eap/energy-dashboard/data-AAA-BBB-CCC/.git/
[master (root-commit) 60db8d3] initial commit
 11 files changed, 812 insertions(+)
 create mode 100644 LICENSE
 create mode 100644 Makefile
 create mode 100644 README.md
 create mode 100644 db/inserted.txt
 create mode 100644 manifest.json
 create mode 100755 src/10_down.py
 create mode 100755 src/20_unzp.py
 create mode 100755 src/30_inse.py
 create mode 100755 src/40_save.sh
 create mode 100644 xml/unzipped.txt
 create mode 100644 zip/downloaded.txt
~/repos/eap/energy-dashboard
created data source repo at: data-AAA-BBB-CCC
TODO: update the RESOURCE_URL and any processing details in src/...
TODO: git remote add origin [path to your blank repository]
TODO: git commit
TODO: git push
make[1]: Leaving directory '/home/toddg/repos/eap/energy-dashboard'
```

Once you complete the TODO's, you can retrieve the resources for your new data source like this:

Command
```bash
cd data-AAA-BBB-CCC
make proc
```

#### Publish a data set

If you are going to maintain the dataset, then file a github ticket for me to add your database to the list of databases that this project copies.

If you want me to maintain the dataset, then file a github ticket and ask me to clone your dataset repo and I'll add it to the submodule list here.

##### The process

1. Download dataset artifacts
1. Unzip artifacts to raw data (whatever that looks like from the source)
1. Insert the raw data into a Sqlite3 database
1. KISS : if possible, keep this to a single file and single table per dataset
1. Commit the raw data and the database to the git repository
1. Contact me to have your dataset included in this repo
1. Once you've published a dataset, don't change the schema as this will break consumers, instead, create a new dataset with the new schema

### Add a tool

* Add tool deps under ./lib
* Add tools under src
* Expose tools via the Makefile



### Q&A

Q: Couldn't this more easily be implemented as an 'airflow' and be hosted on GCP and be injesting data into BigQuery automatically?... Why are you going against the flow here?
A: I want this to be free to use. Anyone should be able to perform data science.
A: I want this to be easy and simple. Jupyter notebooks and git seem pretty simple to me.
A: I don't want the hassle, cost, and complexity of having to maintain a bunch of airflows etc. 


## TODO: move this random stuff to an architecture doc

### Simple Strategies

* Use Open Source Tech : Sqlite3 + Jupyter Notebooks + git
* Use a simple database data structure
* Use a simple metadata format

The combination of these strategies means that you can easily add repos and generate
reports using a combination of datasources.

See:

### Databases

Each datasource generates a database from the downloaded XML Reports. The XML Reports are stuffed inside the .zip files.

TODO: describe the normalization steps for converting the XML Report(s) to the database(s).
TODO: deep dive on the entire pipeline architecture
