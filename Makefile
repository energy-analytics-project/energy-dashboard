APP_NAME=energy-dashboard
repo="repo"
owner="someone"
owner="mycompany"
email="myemail"
url="todo"

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
	#
	#		  Example:
	#
	#		  $ make new 				\
	#		  	repo="data-aaa-bbb-ccc" 	\
	#		  	owner="Your Name" 		\
	#		  	company="Your Company" 		\
	#		  	email="Your Email Address"
	#
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

.PHONY: test
test:  
	make new repo="data-aaa-bbb-ccc" owner="bilbo baggins" company="the shire, inc" email="penguins@wizards.com" url="http://onaroadtonowhere.com"
