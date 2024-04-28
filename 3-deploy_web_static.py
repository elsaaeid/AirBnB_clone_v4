#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
"""

from fabric.api import env, run, put, local
from datetime import datetime
from os.path import exists

env.hosts = ['54.144.149.138', '35.168.1.145']

def do_pack():
    """
    Generates a .tgz archive from the web_static folder
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """
    Uploads the archive to the web servers, uncompress it,
    and updates the symbolic links
    """
    if not exists(archive_path):
        return False

    file_name = archive_path.split('/')[-1]
    archive_no_ext = file_name.split('.')[0]

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(archive_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_name, archive_no_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(archive_no_ext, archive_no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive_no_ext))
        return True
    except:
        return False


def deploy():
    """
    Creates and distributes an archive to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False

    result = do_deploy(archive_path)
    return result
