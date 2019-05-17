# -*- encoding: utf-8 -*-

# Author: Savenko Mike
from core import Plugin, Instance


class Miner(Plugin):
    name = ""
    wnd_state = Instance.SW_HIDE

    def __init__(self, name="", wnd_state=Instance.SW_HIDE):
        super().__init__()
        if not name:
            name = self._get_class_name()
        self.name = name
        self.wnd_state = wnd_state
        self.instance = Instance(self.name, self.wnd_state)

    def start_mining(self):
        if not self.instance.is_running():
            self.instance.start()
        return self.instance.is_running()

    def stop_mining(self):
        self.instance.kill()
