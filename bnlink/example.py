#!/usr/bin/env python2
import sys
sys.path.append(".")
import bnlink

c = bnlink.connect()
bn = c.root.getmodule("binaryninja")
bv = bn.BinaryViewType.get_view_of_file("/usr/bin/cat")
for f in bv.functions:
    print f.name

