#!/bin/bash
# Post a json data from a file
curl -sX "POST" -H "Content-Type: application/json" -d @"$2" "$1" 
