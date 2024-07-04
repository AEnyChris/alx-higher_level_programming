#!/bin/bash
# displays the allowed https methods
curl -sI "$1" | grep "^Allowed: .*" | cut -d " " -f 2-
