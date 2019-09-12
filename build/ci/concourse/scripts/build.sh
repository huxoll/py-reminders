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
echo "GOPATH is: " $GOPATH
echo "TOP is: " $TOP
echo ""

# Build the beast
cd git-reminders-repo
CONTAINER=nomatter make cmd/py-reminders/py-reminders

# Check static linked binary
echo "Check static link status:"
if ldd cmd/py-reminders/py-reminders; then
    echo "The py-reminders binary is dynamically linked, cannot use it."
    exit 1
fi

# Copy build artifacts to the output directory
cp -a cmd/py-reminders/py-reminders ${TOP}/build/
