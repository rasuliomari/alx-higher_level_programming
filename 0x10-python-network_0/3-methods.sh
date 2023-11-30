#!/bin/bash
# Script that takes an URL and shows the Allowed OPTIONS
curl -sI "$1" | grep Allow | cut -d " " -f 2-
