# Ansible role: chrony
---

Ansible role that installs chrony as a client or server.

## Main actions

* Install Chrony package.
* Configure Chrony service as a client or server.
* (Optional) Set up logrotate for Chrony.
* Upgrade Chrony package.
* Test if Chrony is synchronized with declared server(s).

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

MIT

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