# Binary Ninja Hotkeys
The plugin will listen for keyboard presses globally and if the title includes "Binary Ninja"
it will try to execute the configured commands.
Till Binary Ninja support user key bindings, this plugin could be useful *for linux users*.
The title matching is not perfect but I haven't found a better way to do this.


# Install
Make sure that xprop is installed and is reachable in PATH then install following python packages in
Binary Ninja's python environment:
```
# install dependencies 
pip install python-xlib
pip install pynput

# download the plugin
git clone github.com/superr4y/binaryninja_scripts
ln -s $(pwd)/binaryninja_scripts/bnhotkeys ~/.binaryninja/plugins/bnhotkeys
```



# Usage
Configure keys and commands in ~/.binaryninja/plugins/bnhotkeys/config.conf
The command matching must also be added to ~/binaryninja/plugins/bnhotkeys/__init__.conf:UserTask.
Just add a new method to the UserTask class, see existing examples.

Start the plugin over the context menu "Start bnHotkeys".

