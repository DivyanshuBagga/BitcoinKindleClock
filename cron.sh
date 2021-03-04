#!/bin/bash

dir=$(cd `dirname $0` && pwd)
cd $dir

python3 -m  server.update
google-chrome --headless --screenshot="screenshot.png" 'http://divyanshubagga.s3-website.us-east-2.amazonaws.com/display.html' --window-size=600,800
pngcrush -c 0 screenshot.png display.png >> /dev/null
aws s3 cp ./display.png s3://divyanshubagga/
