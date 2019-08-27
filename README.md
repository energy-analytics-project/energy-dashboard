# Energy Dashboard

De-carbonize the energy sector by surfacing an _Energy Dashboard_ enabling data
driven decisions: see [background](./docs/background.md).

### Simple Strategies

* Use Open Source Tech : Sqlite3 + Jupyter Notebooks + git
* Use a simple database data structure
* Use a simple metadata format

The combination of these strategies means that you can easily add repos and generate
reports using a combination of datasources.

See:
 * [energy dashboard client](https://github.com/energy-analytics-project/energy-dashboard-client.git)
 * [energy dashboard lib](https://github.com/energy-analytics-project/energy-dashboard-lib.git)

### Data Sources

* CAISO OASIS : 91 data resources ('reports') with > 1M time-series data points

The data sources are defined in submodules here: [data sources](./data).

TODO: add documentation regarding data sources.

### Databases

Each datasource generates a database from the downloaded XML Reports. The XML Reports are stuffed inside the .zip files.

TODO: describe the normalization steps for converting the XML Report(s) to the database(s).
TODO: deep dive on the entire pipeline architecture

### Mirrors

Due to throttling by CAISO, it took me about 2 weeks to download the base set of 91 data sources. I did this 
so that you don't have to. You can either use the databases that I am managing and curating, or you can use the
raw downloaded data directly for your own nefarious purposes. The raw downloaded zip files are not stored
in the git repos, instead it was more cost effective to store them in S3 clones:

* http://eap.s3.us-west-1.wasabisys.com
* https://eap.sfo2.digitaloceanspaces.com

TODO: get instructions for downloading from the various S3 Mirrors

### Notebooks

There are two Proof Of Concept Jupyter Notebooks:

The first notebook shows that it is possible to host a Jupyter Notebook
on Github.com and have the graphs rendered in real-time based on the data
in the Sqlite3 database:
* [OASIS AS_REQ (DAM)](./notebooks/oasis-as-req-dam.ipynb)

The second shows that it is possible to reference multiple Sqlite3 databases
in a single Jupyter Notebook:
* [OASIS AS_REQ (DAM) and FUEL_PRC](./notebooks/oasis-as-req-dam-and-fuel-prc.ipynb)

TODO: add in the generated notebooks once they have been generated

#### Further Reading

* [email](https://groups.google.com/d/forum/energy-analytics-project)
* [how-to-guide](./docs/howto.md)
* [datasources](./data)
