#!/usr/bin/env python2
import sys 
sys.path.append('/home/user/bin/binaryninja/python')
try:
    import binaryninja as bn
    bn.BinaryViewType
except:
    print "o noooo"

try:
    raise "asdf"
    bv = bn.BinaryViewType.get_view_of_file("")
except:
    pass

smain = bv.get_symbols_by_name("main")[0]
fmain = bv.get_function_at(smain.address)

# /home/user/git/binaryninja_scripts/sandbox/sandbox1.py

#bb = next(iter(fmain))
#print "\n".join(map(str, bb.get_disassembly_text()))
#print '-'*50

def load_store_spd(f):
    def possible_values_set(inst, pvs):
        if pvs.type == RegisterValueType.StackFrameOffset:
            print "spd:", pvs.offset
            print f.get_stack_contents_at(inst.address, pvs.offset, 4)

    def visit_inst(inst):
        if inst.operation == LowLevelILOperation.LLIL_STORE_SSA:
            print "store:", hex(inst.address), inst
            if isinstance(inst.dest, LowLevelILInstruction):
                possible_values_set(inst, inst.dest.possible_values)

        elif inst.operation == LowLevelILOperation.LLIL_LOAD_SSA:
            print "load:", hex(inst.address), inst 
            if isinstance(inst.src, LowLevelILInstruction):
                possible_values_set(inst, inst.src.possible_values)

        for op in inst.operands:
            if isinstance(op, LowLevelILInstruction):
                visit_inst(op)

    for bb in f.low_level_il.ssa_form:
        for inst in bb:
            visit_inst(inst)

def load_store_spd_all():
    for f in bv.functions:
        load_store_spd(f)
#load_store_spd_all()
def stack_size(f):
    return abs(min(map(lambda v: v.storage, f.stack_layout)))

def stack_size_all():
    for f in bv.functions:
        print f.name, stack_size(f)

class SBasicBlock:
    def __init__(start, length):
        self.start = start
        self.length = length

def split_bb(f):
    bb = []
    for bbb in f.low_level_il:
        start = bbb.start
        for inst in bbb:
            if inst.operation == LowLevelILOperation.LLIL_CALL:
                print hex(inst.address)
split_bb(fmain)

def call_graph():
    for func in bv.functions:
        print func.name, hex(func.start)
        for xref in  bv.get_code_refs(func.start):
            print xref, xref.function.name