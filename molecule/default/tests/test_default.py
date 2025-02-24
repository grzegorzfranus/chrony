import pytest
import testinfra.utils.ansible_runner
import re

def test_chrony_is_installed(host):
    chrony = host.package("chrony")
    assert chrony.is_installed
    print(chrony.version)

def test_logrotate_chrony_exists(host):
    logrotate = host.file("/etc/logrotate.d/chrony")
    assert logrotate.exists
    assert logrotate.user == "root"
    assert logrotate.group == "root"
    assert logrotate.mode == 0o644
