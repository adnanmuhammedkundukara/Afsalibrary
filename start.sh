if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/adnanmuhammedkundukara/Afsalibrary.git /Afsalibrary
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Afsalibrary
fi
cd /Afsalibrary
pip3 install -U -r requirements.txt
echo "Starting Afsalibrary...."
python3 main.py
