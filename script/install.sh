cd  $(dirname "$0")
cd ..
path=$(pwd)
cd ~/
echo '

export PATH=$PATH:"'$path'/src"' >> .bashrc