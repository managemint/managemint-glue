#
# hansible_glue/__init__.py
#
#  Copyright (C) 2022 Jonas Gunz, Konstantin Grabmann, Paul Trojahn
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#

import os

from ansible.cli.playbook import PlaybookCLI
from ansible.release import __version__

def version_ok():
    return __version__.startswith('2.12')

def run_playbook(_pb, _limit = None, _tags = None):
    if not version_ok():
        print('Ansible version not OK!')
        return -1

    pbcli = PlaybookCLI(['ansible-playbook', _pb])
    return pbcli.run()

if __name__ == '__main__':
    run_playbook('pb.yml')
