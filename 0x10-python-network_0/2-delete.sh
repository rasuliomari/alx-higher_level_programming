#!/bin/bash

# Use curl to send a DELETE request to the specified URL and display the body
curl -s -X DELETE "$1" -w "\n"
