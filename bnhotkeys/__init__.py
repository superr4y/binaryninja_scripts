import sys
sys.path.append('/home/user/bin/binaryninja/python')
reload(sys)
sys.setdefaultencoding("utf-8")
# TODO: can't find a way to set encoding from Popen, this works for now :-P
# fuck encoding

import pickle
from pynput import keyboard
from subprocess import Popen, PIPE
import re, os

DEBUG = False

try:
    import binaryninja as bn
    bn.BinaryViewType
except:
    sys.path.append('../bnlink')
    import bnlink
    bnlink_connection = bnlink.connect()
    bn = bnlink_connection.root.getmodule('binaryninja')


class UserTask:

    def __init__(self, bv, hotkey):
        self.bv = bv
        self.hotkey = hotkey

    def test_task(self):
        bn.log.log_alert(hex(self.bv.offset))

    def run_bnlink(self):
        import pbnlink
        pbnlink.run_task(self.bv)

    def reload_config(self):
        self.hotkey.load_config(os.path.expanduser("~/.binaryninja/plugins/bnhotkeys/config.conf"))





class bnhotkeys_task(bn.plugin.BackgroundTaskThread):
    def __init__(self, bv):
        bn.plugin.BackgroundTaskThread.__init__(self, "bnhotkeys", True)
        self.bv = bv
        self.conf = None
        self.task = UserTask(self.bv, self)
        self.keys = ""

    def get_active_window_title(self):
        # from: http://stackoverflow.com/questions/3983946/get-active-window-title-in-x
        root = Popen(['xprop', '-root', '_NET_ACTIVE_WINDOW'], stdout=PIPE)

        for line in root.stdout:
            m = re.search('^_NET_ACTIVE_WINDOW.* ([\w]+)$', line)
            if m != None:
                id_ = m.group(1)
                id_w = Popen(['xprop', '-id', id_, 'WM_NAME'], stdout=PIPE)
                break

        if id_w != None:
            for line in id_w.stdout:
                match = re.match("WM_NAME\(\w+\) = (?P<name>.+)$", line)
                if match != None:
                    return match.group("name")

        return "Active window not found"

    def load_config(self, conf_name):
        #self.config = {"Key.ctrl+1": "test_task"}
        with open(conf_name, "r") as conf:
        #    # config = "{hotkey: func_name, ...}"
            self.config = eval(conf.read())

    def on_press(self, key):
        title = self.get_active_window_title().encode('utf-8', 'ignore')
        bn_title_pattern = ".*Binary Ninja"

        m = re.match(bn_title_pattern, title)
        if not m:
            return

        if isinstance(key, keyboard._xorg.KeyCode):
            key = str(key).encode('utf-8', 'ignore')[2:-1] # have not found a better way to get the plain char
            #import pdb; pdb.set_trace()
        else:
            key = str(key)
        if len(self.keys) == 0:
            # first key
            self.keys = key
        else:
            self.keys += "+{}".format(key)

        if DEBUG:
            print "{} title={}".format(self.keys, title)
        func_name = self.config.get(self.keys, False)
        if func_name:
            try:
                getattr(self.task, func_name)()
            except:
                bn.log.log_alert("command {} not found".format(func_name))

    def on_release(self, key):
        self.keys = ""

    def run(self):
        # TODO: maybe ask user for the filename
        self.load_config(os.path.expanduser("~/.binaryninja/plugins/bnhotkeys/config.conf"))
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

def run_task(bv):
    bnhotkeys_task(bv).start()

bn.PluginCommand.register("Start bnHotkeys", "Start bnHotkeys", run_task)
