import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_glusterfs_server_is_installed(host):
    gluster = host.package("glusterfs-server")
    assert gluster.is_installed


def test_gluster_running_and_enabled(host):
    gluster_service = host.service("glusterd")
    assert gluster_service.is_running
    assert gluster_service.is_enabled
