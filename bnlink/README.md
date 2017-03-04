# bnlink
 
This script is inspired by idalink [1] and could be usefull for Binary Ninja personal user.
With the plugin you can access the Binary Ninja API from all your python script.
If you search for something stable and fast, please consider buying a enterprise license. This
is neither stable nor fast ;-)

# Install

```
git clone https://github.com/superr4y/binaryninja_scripts
cd binaryninja_scripts/bnlink
cp pbnlink.py ~/.binaryninja/plugins/ 
```

# Usage

First go to the Binary Ninja GUI and start the plugin (Tools->Start bnlink).
In you script import bnlink like following:
```python
#!/usr/bin/env python2
import sys
sys.path.append('.')
sys.path.append('/my/install/path/binaryninja/python')
import bnlink
try:
    import binaryninja as bn
    bn.BinaryViewType
except:
    bnlink_connection = bnlink.connect()
    bn = bnlink_connection.root.getmodule('binaryninja')

bv = bn.BinaryViewType.get_view_of_file("/usr/bin/cat")
for f in bv.functions:
    print f.name
```

[1] https://github.com/zardus/idalink
