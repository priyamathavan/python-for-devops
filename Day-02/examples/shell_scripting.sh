#!/bin/bash
set -x
$2  
status_code=$?
echo $1 $status_code
exit 0

