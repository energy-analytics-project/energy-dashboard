# Energy Dashboard (ED)

The _Energy Dashboard_, a part of the _Energy Analytics Project_, is a tool to
help de-carbonize the energy sector by providing easy access to publicly
available data. See [background](./docs/background.md) for further details.

## Examples

A picture is worth a thousand words, so...

### Graphs

ED can generate graphs:

![graph1](./docs/caiso/caiso-oasis-avg-fuel-prices.png)
![graph2](./docs/caiso/caiso-oasis-avg-fuel-prices-and-fuel-prices-breakout.png.png)

### Notebooks

ED can generate Jupyter Notebooks:

* [OASIS AS_REQ (DAM)](./notebooks/oasis-as-req-dam.ipynb)
* [OASIS AS_REQ (DAM) and FUEL_PRC](./notebooks/oasis-as-req-dam-and-fuel-prc.ipynb)

## Getting Started

ED is pre-alpha. Please join the [email list](https://groups.google.com/d/forum/energy-analytics-project) to get status updates as this is all moving along
quickly.

### Tooling

[Energy Dashboard Client](https://github.com/energy-analytics-project/energy-dashboard-client.git)

### Data Sources

* [CAISO OASIS](oasis.caiso.com) : 91 data reports, totalling over 1 million time-series data points

[data sources](./data)

### Mirrors

ED publishes raw downloaded data to these publicly readable S3 object stores:

* [wasabi](http://eap.s3.us-west-1.wasabisys.com)
* [digitalocean](https://eap.sfo2.digitaloceanspaces.com)

## Documentation

* [docs](./docs)

## License

[ED is GPL3.0](./LICENSE)

## Author(s)

* Todd Greenwood-Geer : Enviro Software Solutions, LLC. : pub+github@zwrob.com
