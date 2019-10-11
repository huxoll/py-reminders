# Copyright 2015-2019 VMware, Inc. All Rights Reserved.
# Author: Tom Hite (thite@vmware.com)
#
# SPDX-License-Identifier: https://spdx.org/licenses/MIT.html
#

# Check that the container name that gets build is defined.
ifndef CONTAINER
$(error CONTAINER, which specifies the docker container name to build, is not set)
endif

default: container

all: container

container:
	cd build/docker; ./build.sh 
.PHONY: container

container.nopush:
	cd build/docker; ./build.sh nopush
.PHONY: container.nopush

prereqs:
	pip install -r requirements.txt
.PHONY: prereqs

lint: prereqs
	find . -name \*.py | xargs pylint
.PHONY: lint

test: lint
	pytest
.PHONY: test

clean:
	rm -f *.pyc
.PHONY: clean

run:
	docker run --name py-reminders -d -p 9090:8080 $(CONTAINER) /py-reminders/py-reminders.py -a 172.16.78.227
.PHONY: run

stop:
	-killall py-reminders
	-docker stop py-reminders
	-docker rm py-reminders
.PHONY: stop
