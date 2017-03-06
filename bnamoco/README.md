Brings amoco [1] to Binary Ninja.


# Install
```bash
# copy plugin to plugin folder
git clone https://github.com/superr4y/binaryninja_scripts
cd binaryninja_scripts
cp -r amoco ~/.binaryninja/plugins/amoco

# create venv and activate
virtualenv -p python2 amoco_venv
source amoco_venv/bin/activate

# install dependecies
pip install configparser

# install amoco
cd amoco_venv
git clone https://github.com/bdcht/amoco
cd amoco
python setup.py install


# run Binary Ninja from amoco_venv
```

# Usage
...

[1] https://github.com/bdcht/amoco
