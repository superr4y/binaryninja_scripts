Brings [amoco](https://github.com/bdcht/amoco) to Binary Ninja.

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
See examples section and the end of __init__.py 

# Examples

## Import and get amoco basic block object
![amoco_basic_block](/images/amoco_basic_blocks.png)

## Get amoco mapper object
![amoco_mapper](/images/amoco_mapper.png)

## Get amoco memory area object
![amoco_memory_area](/images/amoco_memory_area.png)


# TODO
- [ ] Create html/plain report 
- [ ] Add comments option to Binary Ninja view
- [ ] Export CFG info's


