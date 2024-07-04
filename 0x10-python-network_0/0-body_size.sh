#!/bin/bash
# Displays the size of the body of response
curl -sI "$1" | grep "Length" | cut -c 17-
