#! /bin/bash

# This is to clean sp3 input files.
# It is set in crontab:
# 0 20 * * * sh /home/ubuntu/src/misctools/clean_files.sh > /tmp/clean_out.txt

date

echo "cleaning /data/inputs/local"
find /data/inputs/local -type f -mtime +7 -exec rm -f {} ';'
find /data/inputs/local -type d -mtime +7 -exec rm -r {} ';'

echo "cleaning /data/inputs/users"
find /data/inputs/users -type f -mtime +14 -exec rm -f {} ';'
find /data/inputs/users -type d -mtime +14 -exec rm -r {} ';'

echo "cleaning /data/inputs/ena"
find /data/inputs/ena -type f -mtime +14 -exec rm -f {} ';'
find /data/inputs/ena -type d -mtime +14 -exec rm -r {} ';'

echo "Completed cleaning"

date
