#!/bin/sh

A=$1
B="qiita"
C="zenn"
GIT_DIR="/home/tmp_github"
tools="${GIT_DIR}/tools"
memo="${GIT_DIR}/memo"
qiita="${GIT_DIR}/qiita-sync"
zenn="${GIT_DIR}/zenn-content"


# qiita
if [ $A = $B ]; then
    echo "qiita"
    	sudo python3 "${tools}/cg-exemple.py" < "${qiita}/memo" > "${tools}/article.log" && sudo cp -p "${tools}/article.log" "${qiita}/articles/$2"

elif [ $A = $C ]; then
    echo "zenn"
    	sudo python3 "${tools}/cg-exemple.py" < "${memo}/test1.md" > "${tools}/article.log" && sudo cp -p "${tools}/article.log" "${zenn}/articles/$2"
#        sudo python3 /home/tmp_github/tools/cg-exemple.py < /home/tmp_github/memo/test1.md > /home/tmp_github/tools/article.log &&
#        sudo cp -p /home/tmp_github/tools/article.log /home/tmp_github/zenn-content/articles/$2

else
    echo "error"
fi


