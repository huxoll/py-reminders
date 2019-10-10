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
find . -name \*.py | xargs pylint | tee ${TOP}/py-error-files/pylint.lst

# Check the results
if [ $(cat ${TOP}/py-error-files/pylint.lst | wc -l) -gt 4 ]; then
    cat ${TOP}/py-error-files/pylint.lst
    echo 'Too many style errors! Check syntax.'
    exit 1
fi

# Test the feature code
pytest

# check the ci pipeline scripts
cd build/ci/concourse/scripts
for s in *; do
	bash -n $s
done
