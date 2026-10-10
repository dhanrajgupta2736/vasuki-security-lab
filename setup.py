"""Build hook verifies repository code executes without network interfaces."""
import os
from pathlib import Path
from setuptools import setup

if Path('/sys/class/net').is_dir():
    assert {path.name for path in Path('/sys/class/net').iterdir()} == {'lo'}, 'Repository code executed with network access'
    assert os.geteuid() != 0, 'Repository code executed as root'
    print('Verified offline repository installation and build: loopback only, non-root user')

setup()
