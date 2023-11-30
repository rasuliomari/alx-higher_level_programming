#!/bin/bash

# Use curl to send a DELETE request to the specified URL and display the body
curl -s "$1" -X DELETE
