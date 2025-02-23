# Ansible role: chrony

|Lint|Molecule|Version|
|------|-------|-------|
|[![Build Status](https://github.com/grzegorzfranus/chrony/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/grzegorzfranus/chrony/actions)|[![Build Status](https://github.com/grzegorzfranus/chrony/actions/workflows/ansible-molecule.yml/badge.svg)](https://github.com/grzegorzfranus/chrony/actions)|[![Version](https://img.shields.io/github/v/release/grzegorzfranus/chrony)](https://github.com/grzegorzfranus/chrony/releases)|

[![Repository License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)

## Overview

Ansible role that installs chrony as a client or server.

chronyd is a daemon for synchronisation of the system clock. It can synchronise the clock with NTP servers, reference clocks (e.g. a GPS receiver), and manual input using wristwatch and keyboard via chronyc. It can also operate as an NTPv4 (RFC 5905) server and peer to provide a time service to other computers in the network.

## Main actions

* Install Chrony package.
* Configure Chrony service as a client or server.
* Set up logrotate for Chrony (optional).
* Upgrade Chrony package.
* Test if Chrony is synchronized with declared server(s).

## Version

- `v1.0.0` - initial version  

## Requirements

#### Ansible version

Ansible >= 2.15

#### Python version

Python >= 3.9

#### Setup module
The role uses facts gathered by Ansible on the remote host. If you disable the Setup module in your playbook, the role will not work properly.

#### Root access
This role requires root access, so either configure it in your inventory files, run it in a playbook with a global `become: true` or invoke the role in your playbook like:
> site.yml:
```yaml
- hosts: servers
  become: true
  roles:
    - role: chrony
```

## Role Variables

All variables for this role are declared in the following files:
```yaml
  - default/main.yml
  - vars/*.yml
```

## Dependencies

This role has no dependencies.

## Licenses

[Apache-2.0](https://github.com/grzegorzfranus/chrony/blob/main/LICENSE).

## Example Playbook

Using the role is fairly straightforward:
> site.yml:
```yaml
- hosts: servers
  become: true
  roles:
    - role: chrony
      vars:
        chrony_role_action: "all" 
        chrony_ntp_servers:
          - 169.254.169.254
```

## Author Information

**Grzegorz Franus**