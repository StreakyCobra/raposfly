#!/bin/bash

# Log file
LOG=/var/log/cron.log

# Number of backups to keep
N=32

# Copy from:
FROM=/var/lib/raposfly

# Copy to:
TO=/var/lib/raposfly/backups

# From name:
F_NAME=db.sqlite3

# To name:
T_NAME=$(date +%Y-%m-%d"_"%H-%M-%S).sqlite3

# Create the backup directory if it doesn't exists
mkdir -p "${TO}"

# Do the copy
cp -a "${FROM}/${F_NAME}" "${TO}/${T_NAME}" 2>>${LOG} && echo "Backup saved to ${T_NAME}" >> ${LOG}

# Get the list of backups to remove
REMOVE=$(comm -23 <(ls -d ${TO}/*) <(ls -dtr ${TO}/* | head -n ${N} | sort) 2>>${LOG})

# Remove extra backups
[ -n "${REMOVE}" ] && echo "${REMOVE}" | xargs rm -rf 2>>${LOG} && echo "Backups removed: ${REMOVE}" >> ${LOG}
