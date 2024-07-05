#!/bin/bash
# displays the allowed https methods
curl -sI "$1" | grep "Allow" | cut -c 8-
