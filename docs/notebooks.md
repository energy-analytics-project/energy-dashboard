# Notebooks

See https://jupyter.org/

## Guidelines

The entire idea with this project is shareable data analytics. As such, it's important that everything is:

* self-contained
* open-source
* repeatable
* consistent

1. For now, this project is in one repo. This will clearly not scale over time
   as git isn't built for this kind of use case. However, we'll cross that
   bridge when the time comes. For now, I'm getting this up and running.
1. The notebooks should reference data in this repo only. If you need external
   data, then add [tooling](./docs/tools.md), [data](./docs/data.md), and
   [docs](./docs/docs.md) to bring that external data into this repo. Then base
   your [notebooks](./docs/notebooks.md) on the data in this repo.
1. Use [open-source notebooks](https://jupyter.org/), plugins, languages, etc.
1. Add docs *and* annotate your notebook so that your process and findings are
   understandable and repeatable
1. Keep as much context and data in the repo as possible, rather than using
   external tooling such as github wiki pages, etc. Documentation should live
   _in_ the repo rather than alongside it in some external (and private)
   service.
