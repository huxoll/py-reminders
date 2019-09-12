# Copyright 2015-2019 VMware, Inc. All Rights Reserved.
# Author: Tom Hite (thite@vmware.com)
#
# SPDX-License-Identifier: https://spdx.org/licenses/MIT.html
#

# Check that the container name that gets build is defined.
ifndef CONTAINER
$(error CONTAINER, which specifies the docker container name to build, is not set)
endif

default: cmd/py-reminders/py-reminders cmd/py-reminders/py-reminders-darwin

all: container

container: cmd/py-reminders/py-reminders
	cd build/docker; ./build.sh
.PHONY: container

go.mod:
	go mod init github.com/vmware/py-reminders
	for m in $$(cat forcemodules); do go get "$$m"; done

test:
	go test ./...
.PHONY: test

clean:
	rm -f *.pyc
.PHONY: clean

run:
	docker run --name py-reminders -d -p 8080:8080 $(CONTAINER) /py-reminders -a 172.16.78.227
.PHONY: run

stop:
	-killall py-reminders
	-docker stop py-reminders
	-docker rm py-reminders
.PHONY: stop
