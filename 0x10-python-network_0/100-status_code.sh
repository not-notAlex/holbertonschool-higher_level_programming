#!/bin/bash
# sends request to URL and posts status
curl -o /dev/null -w '%{http_code}' -sLI "$1"
