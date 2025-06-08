#! bin/sh

sudo git add $1 &&
sudo git commit -m "$2" ./$1 && 
sudo git push && 
sudo gh pr create
