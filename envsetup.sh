#! /bin/bash
if [-d "env"]
then
    echo "Python Virtual env exist"
else
    python3 -m venv env
fi
echo $pwd
source env/bin/activate
pip3 install -r requirements.txt
echo "envstup finish"