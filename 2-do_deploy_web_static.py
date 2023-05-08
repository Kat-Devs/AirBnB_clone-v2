#!/usr/bin/python3
'''
Script  to compresses a folder
'''

from datetime import datetime
from fabric.api import *
import shlex
import os


env.hosts = ['52.86.156.220', '54.146.85.195']
env.user = "ubuntu"


def do_deploy(archive_path):
    '''
    Deploys site
    '''
    if not os.path.exists(archive_path):
        return False
    try:
        fname = archive_path.replace('/', ' ')
        fname = shlex.split(name)
        fname = name[-1]

        wname = fname.replace('.', ' ')
        wname = shlex.split(wname)
        wname = wname[0]

        releases_path = "/data/web_static/releases/{}/".format(wname)
        tmp_path = "/tmp/{}".format(fname)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except:
        return False
