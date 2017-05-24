import sys
idaapi.autoWait()
sys.stdout = open('/tmp/bnida.log', 'w')
funcs = []
for func in Functions():
    if SegName(func) != 'extern':
        funcs.append(func)
print "idafunctions = ", funcs
Exit(0)