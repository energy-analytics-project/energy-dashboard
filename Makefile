APP_NAME=energy-dashboard
repo="repo"
owner="someone"
owner="mycompany"
email="myemail"

.PHONY: all
all: help

.PHONY: help
help:
	# -----------------------------------------------------------------------------
	# Import datasets into the ${APP_NAME}
	#
	# Targets:
	#
	# 	daily 	: fetch and save resources
	# 	fetch	: fetch (curl/copy) resources to ./data
	#	save	: save resources to backing store (git)
	#	new	: create new datasource repo [args=name]
	#		  e.g. make new repo="data-AAA-BBB-CCC" owner="Todd Greenwood-Geer" company="Enviro Software Solutions, LLC" email="pub+github@zwrob.com"
	#
	# Created by:
	# Todd Greenwood-Geer <pub+github@zwrob.com>
	# Enviro Software Solutions, LLC
	# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TARGETS
# -----------------------------------------------------------------------------
.PHONY: daily
daily:  fetch save

.PHONY: fetch
fetch:  
	src/10_fetch.sh

.PHONY: save
save:  
	src/20_save.sh

.PHONY: new
new:  
	src/create_data_source.sh "$(repo)" "$(owner)" "$(company)" "$(email)"
