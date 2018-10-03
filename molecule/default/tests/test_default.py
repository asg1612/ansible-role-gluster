import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_glusterfs_server_is_installed(host):
    gluster = host.package("glusterfs-server")
    assert gluster.is_installed


def test_nginx_running_and_enabled(host):
    gluster = host.service("glusterd")
    assert gluster.is_running
    assert gluster.is_enabled
