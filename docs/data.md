# Data

This directory contains raw data. Once added, raw data is _never_ modified.

Data is organized by source like so:

```bash
data/SOURCE/readme.md
data/SOURCE/downloaded.manifest
data/SOURCE/TYPE
```

So the _oasis_ data set is organized like this:
```bash
data/oasis/readme.md
data/oasis/downloaded.manifest
data/oasis/xml
```

1. The `readme.md` provides details about

* tooling used to retrieve the data-set
* where the data-set is from, and what it's good for

1. The `downloaded.manifest` is a record of the downloaded items and is used for preventing duplicate downloads.

For example, this is the process for downloading the _oasis_  data-set:
* download `zip` file containing xml report(s)
* unzip `zip` file and place contents into the `data/oasis/xml` directory
* parse new xml files and insert records into database
* update downloaded.manifest with processed URLs

Subsequent runs of the _oasis_ download tooling check the `downloaded.manifest` and skip downloading of URLs that
are in the `downloaded.manifest`.
