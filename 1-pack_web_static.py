#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of an AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime
from fabric.api import local

def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.
    """
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    try:
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except:
        return None

