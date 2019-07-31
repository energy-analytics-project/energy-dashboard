#! /bin/bash

./tools/01_curl_artifacts.sh

# NOTE: this will fail if ssh-key is not loaded.
# NOTE: keeping security stuff like that out-of-band.
./tools/02_update_repo.sh
