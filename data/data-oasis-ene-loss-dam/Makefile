.PHONE: all
all: help

.PHONY: help
help:
	# -----------------------------------------------------------------------------
	# Processor for data-oasis-ene-loss-dam
	#
	# Targets:
	#
	#     proc    : invoke all targets [down,unzip,injest,save]
	#     down    : download zip files 
	#     unzip   : unzip zip files
	#     injest  : injest xml files into sqlite db
	#     save    : commit data to store to repo
	#
	# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TARGETS
# -----------------------------------------------------------------------------
.PHONY: setup
setup:  
	pipenv install requests

.PHONY: proc
proc:  down unzip injest save

.PHONY: down
down:  
	src/10_down.py

.PHONY: unzip
unzip:  
	src/20_unzp.py

.PHONY: injest
injest:  
	src/30_inse.py

.PHONY: save
save:  
	src/40_save.sh
