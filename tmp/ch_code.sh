#! /bin/sh

sed -i "s/__%%_title_%%__/$2/g" $1 | 
sed -i "s/__%%_emoji_%%__/$3/g" $1 |  
sed -i "s/__%%_type_%%__/$4/g" $1 | 
sed -i "s/__%%_topics_%%__/$5/g" $1
