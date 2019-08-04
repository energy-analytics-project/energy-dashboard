#!/bin/bash

REPO=${1:-repo}
FQPATH_REPO=`pwd`/${REPO}
TEMP_REPO=.temp-data-source-template
export YEAR=$(date +%Y)
export DATA_SOURCE_NAME=${REPO}
export OWNER=${2:-owner}
export COMPANY=${3:-company}
export EMAIL=${4:-email}

echo "----------------------------------------------------"
echo "Usage: REPO OWNER COMPANY EMAIL"
echo ""
echo "TEMPLATE VARS:"
echo ""
echo "  REPO=${REPO}"
echo "  YEAR=${YEAR}"
echo "  DATA_SOURCE_NAME=${DATA_SOURCE_NAME}"
echo "  OWNER=${OWNER}"
echo "  COMPANY=${COMPANY}"
echo "  EMAIL=${EMAIL}"
echo "----------------------------------------------------"

if [ -e ${TEMP_REPO} ]; then
    echo "skipping download. remove ${TEMP_REPO} dir if you want to download a fresh template repo"
else
    echo "downloading template repo to: $TEMP_REPO"
    git clone https://github.com/energy-analytics-project/data-source-template.git ${TEMP_REPO}
fi

echo "copying repo: $REPO"
mkdir -p ${FQPATH_REPO}
(cd ${TEMP_REPO} && git archive --format=tar HEAD | (cd ${FQPATH_REPO} && tar xfp -))

echo "updating template vars: $REPO"
array=(LICENSE Makefile README.md src/10_down.py src/20_unzp.py src/30_inse.py src/40_save.sh manifest.json)

for item in ${array[*]}
do
    echo "processing : ${REPO}/${item}"
    cat ${TEMP_REPO}/${item} | ./lib/mo > ${REPO}/${item}
done

pushd ${REPO}
git init
git add *
git commit -m "initial commit" -m "auto-generated via create_data_source.sh"
popd

echo "created data source repo at: ${REPO}"
echo "TODO: update the RESOURCE_URL and any processing details in src/..."
echo "TODO: git remote add origin [path to your blank repository]"
echo "TODO: git commit"
echo "TODO: git push"
