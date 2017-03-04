# bnlink
 
This script is inspired by idalink [1]
With this plugin the scripting api of Binary Ninja can be accessed from all your python scripts.
If you search for something stable and fast, please consider buying a enterprise license. This
is probably neither stable nor fast ;-)

# Install

```
cp pbnlink.py ~/.binaryninja/plugins/ 
```

# Use

First go to the Binary Ninja GUI and start the plugin (Tools->Start bnlink).
In you script import bnlink like following:
```python
import sys
sys.path.append(<path_to_bnlink_dir>)
import bnlink
c = bnlink.connect()
bn = c.root.getmodule("binaryninja")
bv = bn.BinaryViewType.get_view_of_file("....")
...
```

[1] https://github.com/zardus/idalink
