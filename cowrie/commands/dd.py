# Copyright (c) 2009 Upi Tamminen <desaster@gmail.com>
# See the COPYRIGHT file for more information

import os

from twisted.python import log

from cowrie.core.honeypot import HoneyPotCommand
from cowrie.core.fs import *

commands = {}


class command_dd(HoneyPotCommand):
    """
    """

    def call(self):
        """
        """
        if len(self.args) < 2:
                self.write('0+0 records in\n')
                self.write('0+0 records out\n')
                self.write('0 bytes (0 B) copied, 0.729481 s, 0.0 kB/s\n')
                return

        self.write('0+0 records in\n')
        self.write('0+0 records out\n')
        self.write('0 bytes (0 B) copied, 0.729481 s, 0.0 kB/s\n')

commands['/bin/dd'] = command_dd
commands['dd'] = command_dd

# vim: set sw=4 et:
