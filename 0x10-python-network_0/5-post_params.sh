#!/bin/bash
# sends a POST request and returns body of response
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
