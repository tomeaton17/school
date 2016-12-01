git clone "https://github.com/thomfur/school.git"
git clone "https://github.com/thomfur/school.git" temp
mv temp/.git .git
rm -rf temp
ls
git pull
ls
git diff origin/master
ls
git clone "https://github.com/thomfur/school.git" temp
ls temp
mv temp/questionStore.py questionStore.py
mv temp/radioactivedecay.py radioactivedecay.py
mv temp/suvat.py suvat.py
rm -rf temp
git commit
git config --global user.email "thomfurpwns@gmail.com"
git config --global user.name "Tom Eaton"
git commit
git add .
git commit
git push
