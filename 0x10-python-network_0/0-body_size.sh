#!/bin/bash
# returns the length in bytes of body
curl -sI "$1" |awk '/Content-Length/{print $2}'
