#./scripts/freeze.sh

echo "Enter commit message: "
read commitMessage

git add .
git commit -m $commitMessage
git push origin master
