#!/usr/bin/env python2
import sys
sys.path.append('/home/user/bin/binaryninja/python')
import amoco
try:
    import binaryninja as bn
    bn.BinaryViewType
except:
    sys.path.append('../bnlink')
    import bnlink
    bnlink_connection = bnlink.connect()
    bn = bnlink_connection.root.getmodule('binaryninja')


class BNAmocoFunc:
    def __init__(self, bv, func):
        self.bv = bv
        self.func = func
        self.prog = amoco.system.loader.load_program(bv.file.filename)
        self.bb = dict()

    def _sequence(self,addr):
        p = self.prog
        try:
            m = p.initenv()
            #loc = m(p.cpu.PC())
        except (TypeError,ValueError):
            addr = 0
        while True:
            i = p.read_instruction(addr)
            if i is None: raise StopIteration
            addr += i.length
            yield i


    def get_basic_block_at(self, addr):
        abb = self.bb.get(addr, False)
        if not abb:
            bb = self.func.get_basic_block_at(addr)
            gen = self._sequence(bb.start)
            instr_list = []
            while True:
                instr = next(gen)
                if instr.address >= bb.end:
                    break
                instr_list.append(instr)
            abb = amoco.code.block(instr_list)
            abb.misc['cfi'] = instr
            abb = self.prog.codehelper(block=abb)
            self.bb[addr] = abb
        return abb

    def get_mapper_at(self, addr):
        return self.get_basic_block_at(addr).map

    def get_memory_at(self, addr):
        return self.get_basic_block_at(addr).map.memory()

    @property
    def basic_blocks(self):
        for bb in self.func.basic_blocks:
            abb = self.get_basic_block_at(bb.start)
            yield abb

    @property
    def mappers(self):
        for bb in self.basic_blocks:
            yield bb.map

if __name__ == '__main__':
    bv = bn.BinaryViewType.get_view_of_file("/home/user/amoco/framework/test/samples/s01_x86")
    main_addr = bv.get_symbols_by_name("main")[0].address
    main = bv.get_functions_at(main_addr)[0]

    afunc = BNAmocoFunc(bv, main)
    for bb in afunc.basic_blocks:
        print bb.misc

    for m in afunc.mappers:
        print m
    #bb = afunc.get_basic_block_at(0x804845a)
    #print bb
    #print afunc.get_mapper_at(0x804845a)
    #print afunc.get_memory_at(0x804845a)
