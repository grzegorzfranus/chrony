# Ansible role: chrony

|Version|Tests|License|Code style|
|------|-------|-------|-------|
|[![Version](https://img.shields.io/github/v/release/grzegorzfranus/chrony)](https://github.com/grzegorzfranus/chrony/releases)|[![tests](https://github.com/grzegorzfranus/chrony/actions/workflows/tests.yml/badge.svg)](https://github.com/grzegorzfranus/chrony/actions)|[![Repository License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)|[![Python Black Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)|

## Overview

Ansible role that installs chrony as a client or server.

Chronyd is a daemon for synchronisation of the system clock.

## Main actions

* Install Chrony package.
* Configure Chrony service.
* Set up logrotate (optional).
* Upgrade Chrony package (optional).
* Test if Chrony is synchronized with declared server(s).

## Version

- `v1.0.0` - initial version  

## Requirements

### Ansible version

Ansible >= 2.15

### Python version

Python >= 3.9

### Setup module
The role uses facts gathered by Ansible on the remote host. If you disable the Setup module in your playbook, the role will not work properly.

### Root access
This role requires root access for some tasks. Make sure that you are using a user with root privileges.

## Role Variables

### Main variables

* aaaa
* aaaa
* aaaa
* aaaa

### Chrony Configuration

* aaaa
* aaaa
* aaaa
* aaaa

## Dependencies

This role has no dependencies.

## Example Playbook

Using the role is fairly straightforward:
> site.yml:
```yaml
- hosts: server
  roles:
    - role: chrony
      vars:
        chrony_role_action: "all"
        chrony_service_enabled: true
        chrony_configure_logrotate: true
        chrony_ntp_source_mode: "pool"
        chrony_ntp_servers:
          - 169.254.169.254
```

## Licenses

The [MIT](https://github.com/grzegorzfranus/chrony/blob/main/LICENSE) License.

If you have some other use in mind, contact me.

## Author Information

This role was created by **[Grzegorz Franus](https://github.com/grzegorzfranus)**.