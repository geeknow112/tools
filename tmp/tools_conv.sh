# /bin/sh

custom_url=$1
#custom_url=${custom_url%.md}

sudo sed -e 's/^---//g' $1 | 
sudo sed -e 's/^emoji:.*$//g' | 
sudo sed -e 's/^type:.*$//g' | 
sudo sed -e 's/published: true/'$custom_url'/g' | 

sudo sed -e 's/^title: "//g' | 
sudo sed -e 's/^topics: \["//g' | 
sudo sed -e 's/"\]$//g' | 
sudo sed -e 's/"$//g' | 
sudo sed -e 's/", "/,/g'
