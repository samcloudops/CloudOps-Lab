#!/usr/bin/env bash

set -u

echo "=================================="
echo "       SAMCLOUD SYSTEM CHECK"
echo "=================================="

echo
echo "[ SYSTEM INFORMATION ]"
uname -a

echo
echo "[ UPTIME ]"
uptime

echo
echo "[ DISK USAGE ]"
df -h

echo
echo "[ MEMORY INFORMATION ]"
if command -v free >/dev/null 2>&1; then
    free -h
else
    echo "Memory command unavailable on this system."
fi

echo
echo "[ CURRENT USER ]"
whoami

echo
echo "=================================="
echo "       CHECK COMPLETED"
echo "=================================="
