from binaryninja import plugin, PluginCommand

class bnlink_task(plugin.BackgroundTaskThread):
    def __init__(self, bv):
        plugin.BackgroundTaskThread.__init__(self, "bnlink", True)
        self.bv = bv

    def run(self):
        from rpyc.core import SlaveService
        from rpyc.utils.server import ThreadedServer
        ThreadedServer(SlaveService, port=6666).start()

def run_task(bv):
    bnlink_task(bv).start()

PluginCommand.register(
    "Start bnlink", "Run's rpc service on port 6666", run_task
)
