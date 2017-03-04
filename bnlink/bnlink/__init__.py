import rpyc

def connect():
    # Getting: ReferenceError('weakly-referenced object no longer exists') if a module is returned
    # For now just do basically nothing :-P
    c = rpyc.classic.connect("127.0.0.1", 6666)
    return c
