# /bin/sh

# 大文字を小文字に変換
sudo sed -i 's/.\+/\L\0/g' $1 
