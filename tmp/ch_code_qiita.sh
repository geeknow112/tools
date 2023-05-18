#! /bin/sh

sed -i "s/__%%_title_%%__/$2/g" $1 | 
sed -i "s/__%%_tags_%%__/$3/g" $1
