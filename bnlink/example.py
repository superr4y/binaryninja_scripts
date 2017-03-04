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
