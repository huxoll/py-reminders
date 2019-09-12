#!/bin/bash
#
# Copyright 2015-2019 VMware, Inc. All Rights Reserved.
# Author: Tom Hite (thite@vmware.com)
#
# SPDX-License-Identifier: https://spdx.org/licenses/MIT.html
#

# Grab the latest build output
cp -a ../cmd/py-reminders/py-reminders .

# Run the thing. Check it at http://localhost:8080
./py-reminders -dbtype=mem

curl -X Post -H "content-Type: application/json" http://localhost:8080/api/reminders -d "$(cat ../test-reminder.json)"
