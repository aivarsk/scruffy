#!/bin/bash

DIR=tests
result=0

for sequence in `ls $DIR/sequence*.suml`;
do
    base=${sequence%.*}
    suml --sequence < $base.suml > $base.tmp
    diff $base.pic $base.tmp > /dev/null
    if [ $? -ne 0 ];
    then
        result=-1
        echo "Changes for $base.suml -> $base.pic:"
        diff -up $base.pic $base.tmp
    else
        rm -f $base.tmp
    fi
done

for class in `ls $DIR/class*.suml`;
do
    base=${class%.*}
    suml --class < $base.suml > $base.tmp
    diff $base.dot $base.tmp > /dev/null
    if [ $? -ne 0 ];
    then
        result=-1
        echo "Changes for $base.suml -> $base.dot:"
        diff -up $base.dot $base.tmp
        rm -f $base.tmp
    fi
done

exit $result
