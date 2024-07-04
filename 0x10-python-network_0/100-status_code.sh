#!/bin/bash
# Returns the status code of request
curl -so /dev/null -w "%{http_code}" "$1"
