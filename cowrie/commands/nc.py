# Copyright (c) 2009 Upi Tamminen <desaster@gmail.com>
# See the COPYRIGHT file for more information

import os

from twisted.python import log

from cowrie.core.honeypot import HoneyPotCommand
from cowrie.core.fs import *

commands = {}


class command_nc(HoneyPotCommand):
    """
    """

    def call(self):
        """
        """
        if len(self.args) < 2:
            self.write('Ncat: You must specify a host to connect to. QUITTING.\n')
            return

        return

commands['/bin/nc'] = command_nc
commands['nc'] = command_nc

# vim: set sw=4 et:
