#!/bin/bash
#
# Copyright 2015-2019 VMware, Inc. All Rights Reserved.
# Author: Tom Hite (thite@vmware.com)
#
# SPDX-License-Identifier: https://spdx.org/licenses/MIT.html
#

if [ -z "${CONTAINER}" ]; then
    echo 'Environment variables CONTAINER is not set.'
    echo 'It should be set to the container name to build and push.'
    exit 1
fi

# Grab the latest build output
cp -a ../../*.py ../../reminders ../../requirements.txt .

# Build and push the container
docker build --rm -t ${CONTAINER} .

if [ -z "$1" ]; then
    docker push ${CONTAINER}
fi
