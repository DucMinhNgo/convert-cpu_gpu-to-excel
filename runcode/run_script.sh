#!/bin/sh
ls | while read file
do
    python $file
done