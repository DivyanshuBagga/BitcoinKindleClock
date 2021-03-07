#!/bin/bash

dir=$(cd `dirname $0` && pwd)
cd $dir

python3 -m  server.update
google-chrome --headless --screenshot="screenshot.png" 'display.html' --window-size=600,800
pngcrush -c 0 screenshot.png display.png >> /dev/null
aws s3 cp ./display.png s3://divyanshubagga/
