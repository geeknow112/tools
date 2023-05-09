#!/bin/sh

# qiita
A=$1
B="qiita"

if [ $A = $B ]; then
    echo "qiita"
	sudo python3 /home/tmp_github/tools/cg-exemple.py < /home/tmp_github/qiita-sync/memo > /home/tmp_github/tools/article.log && 
	sudo cp -p /home/tmp_github/tools/article.log /home/tmp_github/qiita-sync/articles/$2
else
    echo "error"
fi

# zenn
A=$1
B="zenn"

if [ $A = $B ]; then
    echo "zenn"
	sudo python3 /home/tmp_github/tools/cg-exemple.py < /home/tmp_github/memo/test1.md > /home/tmp_github/tools/article.log && 
	sudo cp -p /home/tmp_github/tools/article.log /home/tmp_github/zenn-content/articles/$2
else
    echo "error"
fi

