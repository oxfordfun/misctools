#! /bin/bash

# This is to clean sp3 input files.
# It is set in crontab:
# 0 20 * * * sh /home/ubuntu/src/misctools/clean_files.sh > /tmp/clean_out.txt

date
du -kh /data/inputs/local --max-depth=0
echo "=============cleaning /data/inputs/local"
find /data/inputs/local -type f -mtime +5 -exec rm -f {} ';'
find /data/inputs/local -type d -mtime +5 -exec rm -r {} ';'
du -kh /data/inputs/local --max-depth=0

du -kh /data/inputs/users --max-depth=0
echo "=============cleaning /data/inputs/users"
find /data/inputs/users -type f -mtime +14 -exec rm -f {} ';'
find /data/inputs/users -type d -mtime +14 -exec rm -r {} ';'
du -kh /data/inputs/users --max-depth=0

du -kh /data/inputs/ena --max-depth=0
echo "=============cleaning /data/inputs/ena"
find /data/inputs/ena -type f -mtime +14 -exec rm -f {} ';'
find /data/inputs/ena -type d -mtime +14 -exec rm -r {} ';'
du -kh /data/inputs/ena --max-depth=0

echo "Completed cleaning"

date
