APP_NAME=energy-dashboard

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
