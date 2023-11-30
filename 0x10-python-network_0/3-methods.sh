#!/bin/bash


# Use curl to send an OPTIONS request to the specified URL and display allowed methods
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
