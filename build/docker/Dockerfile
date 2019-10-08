# py-reminders minimal container definition
#
# Copyright 2015-2019 VMware, Inc. All Rights Reserved.
# Author: Tom Hite (thite@vmware.com)
#
# SPDX-License-Identifier: https://spdx.org/licenses/MIT.html
#

# Start from scratch
FROM python:3.7.4

# Add the microservice
ADD . /py-reminders
WORKDIR /py-reminders

RUN pip install -r requirements.txt 
EXPOSE 8080

ENTRYPOINT ["/py-reminders/py-reminders.py"]
