import pytest
import testinfra.utils.ansible_runner
import re

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')

def get_chrony_package_name(host):
    os_family = host.system_info.distribution
    if os_family in ["debian", "ubuntu"]:
        return "chrony"
    elif os_family in ["centos", "rocky", "redhat"]:
        return "chrony"
    else:
        raise ValueError(f"Unsupported distribution: {os_family}")

def test_chrony_is_installed(host):
    package_name = get_chrony_package_name(host)
    chrony = host.package(package_name)
    assert chrony.is_installed
    print(chrony.version)

def test_logrotate_chrony_exists(host):
    logrotate = host.file("/etc/logrotate.d/chrony")
    assert logrotate.exists
    assert logrotate.user == "root"
    assert logrotate.group == "root"
    assert logrotate.mode == 0o644
