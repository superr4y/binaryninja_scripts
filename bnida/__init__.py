#from binaryninja import *
from subprocess import check_output
import sys
import os.path as path
import binaryninja as bn

class ida_task(bn.plugin.BackgroundTaskThread):
    def __init__(self, bv):
        bn.plugin.BackgroundTaskThread.__init__(self, "bnida", True)
        self.bv = bv

    def run(self):
        bv = self.bv
        try:
            arch = bv.arch.address_size*8
        except:
            arch = 32
        filename = bv.file.filename
        ida = 'idaq' if arch == 32 else 'idaq64'
        #ida_script = path.join(path.dirname(path.abspath(sys.argv[0])), "ida.py")
        ida_script = "/home/user/git/binaryninja_scripts/bnida/ida.py"


        check_output([ida, '-A', "-S%s"%(ida_script), filename])
        with open("/tmp/bnida.log", 'r') as ida_out:
            # will declare idafunctions list
            exec(ida_out.read())
        #print idafunctions
        print "found %d functions"%(len(idafunctions))
        for idafunction in idafunctions:
            bv.add_function(idafunction, plat=bv.platform)
	bv.reanalyze()

def spawn(bv):
    ida_task(bv).start()

bn.PluginCommand.register("IDA Pro", "import function list", spawn)


