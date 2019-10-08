#!/bin/bash
# py-reminders static.sh
#
# Copyright 2015-2019 VMware, Inc. All Rights Reserved.
# Author: Tom Hite (thite@vmware.com)
#
# SPDX-License-Identifier: https://spdx.org/licenses/MIT.html
#

set -e -x

# Save current directory
TOP="$(pwd)"

# Make the output area if it does not exist
mkdir -p ${TOP}/py-error-files

# change directories to the code
cd git-reminders-repo

# Install dependencies
pip install -r requirements.txt

# Test the code for formatting
#find . -name \*.go | xargs gofmt -l | tee ${TOP}/go-error-files/gofmt.lst

# Check the results
# if [ $(cat ${TOP}/go-error-files/gofmt.lst | wc -l) -ne 0 ]; then
#     cat ${TOP}/go-error-files/gofmt.lst
#     exit 1
# fi

# Test the feature code
CONTAINER=pytest

# check the ci pipeline scripts
cd build/ci/concourse/scripts
for s in *; do
	bash -n $s
done
