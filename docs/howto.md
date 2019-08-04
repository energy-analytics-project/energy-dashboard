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

#### Create a new data set from a template

```bash
make new repo="data-AAA-BBB-CCC" owner="Todd Greenwood-Geer" company="Enviro Software Solutions, LLC" email="pub+github@zwrob.com"
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
