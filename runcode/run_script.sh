#!/bin/sh
ls | while read file
do
    sleep 1
    python $file
done