#!/bin/bash

# Number of backup to keep
N=100

# Name of the file
NAME=db.sqlite3

# Copy from place
FROM=/app

# Copy to place
TO=/mnt

# Do the copy
cp -a "${FROM}/${NAME}" "${TO}/$(date +%Y-%m-%d"_"%H-%M-%S).sqlite3"

# Keep only the last N backups
comm -23 <(ls) <(ls -dtr * | tail -n -${N}) | xargs rm -rf
