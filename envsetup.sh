#! /bin/bash
if [-d "env"]
then
    echo "Python Virtual env exist"
else
    python3 -m venv env
fi
echo $pwd
echo "envstup finish"