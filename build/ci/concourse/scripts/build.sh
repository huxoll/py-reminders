#!/bin/bash
# py-reminders build.sh
#
# Copyright 2015-2019 VMware, Inc. All Rights Reserved.
# Author: Tom Hite (thite@vmware.com)
#
# SPDX-License-Identifier: https://spdx.org/licenses/MIT.html
#

set -e -x

# Save current directory
TOP="$(pwd)"

# Show current setup
echo "TOP is: " $TOP
echo ""

# change directories to the code
cd git-reminders-repo

# Install dependencies
pip install -r requirements.txt

# Build the beast
# Whee, interpreted language!  No build step!

# Copy build artifacts to the output directory
cp -a reminders ${TOP}/build/
cp -a *.py ${TOP}/build/
cp requirements.txt ${TOP}/build/
