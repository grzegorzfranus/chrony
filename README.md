# Ansible Role: Chrony

|Source|Version|CI|License|
|------|-------|-------|-------|
|[![Source Code](https://img.shields.io/badge/source-github-blue.svg)](https://github.com/grzegorzfranus/chrony)|[![Version](https://img.shields.io/github/v/release/grzegorzfranus/chrony)](https://github.com/grzegorzfranus/chrony/releases)|[![tests](https://github.com/grzegorzfranus/chrony/actions/workflows/ci.yml/badge.svg)](https://github.com/grzegorzfranus/chrony/actions)|[![Repository License](https://img.shields.io/badge/license-apache2.0-brightgreen.svg)](LICENSE)|

This Ansible role installs and configures Chrony, a versatile implementation of the Network Time Protocol (NTP). It provides a robust and secure time synchronization solution with features like NTP server/pool configuration, log rotation management, and service state control.

## Main Actions

- Install Chrony package
- Configure Chrony service
- Set up NTP servers/pools
- Configure log rotation
- Manage service state
- Handle system requirements (stop conflicting services)

## Requirements

### Supported operating systems
List of officially supported operating systems:
| OS Family | Version | Status |
|-----------|---------|---------|
| Ubuntu | 24.04 (Focal) | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| Ubuntu | 22.04 (Jammy) | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| Debian | 12 (Bookworm) | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| Debian | 11 (Bullseye) | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |
| Rocky Linux | 9 | ![✓](https://img.shields.io/badge/✓-brightgreen.svg) |

### Ansible version

Ansible >= 2.15

### Python version

Python >= 3.11

### Setup module
The role uses facts gathered by Ansible on the remote host. If you disable the Setup module in your playbook, the role will not work properly.

### Root access
This role requires root access for some tasks. Make sure that you are using a user with root privileges.

## Role Variables

### General Options

| Variable | Description | Default |
|----------|-------------|---------|
| `chrony_role_action` | Define which parts of the role to execute (Options: 'all', 'install', 'config') | `"all"` |
| `chrony_service_name` | Name of the Chrony service | `chrony` |
| `chrony_service_enabled` | Whether to enable Chrony service | `true` |
| `chrony_service_state` | Desired state of Chrony service | `started` |
| `chrony_configure_logrotate` | Enable/disable logrotate configuration for Chrony logs | `true` |
| `chrony_run_test` | Enable test mode (useful for debugging) | `false` |

### Package Options

| Variable | Description | Default |
|----------|-------------|---------|
| `chrony_package_name` | Name of the Chrony package to install | `"chrony"` |

### Configuration Options

| Variable | Description | Default |
|----------|-------------|---------|
| `chrony_config_path` | Path to Chrony configuration file | `/etc/chrony/chrony.conf` |
| `chrony_ntp_source_mode` | Define how this host should operate (Options: 'server', 'client') | `"server"` |
| `chrony_ntp_servers` | List of NTP servers to sync with (with options like iburst, minpoll, maxpoll) | `["0.pool.ntp.org iburst minpoll 4 maxpoll 8", "1.pool.ntp.org iburst minpoll 4 maxpoll 8", "2.pool.ntp.org iburst minpoll 4 maxpoll 8", "3.pool.ntp.org iburst minpoll 4 maxpoll 8"]` |
| `chrony_rtcsync_enable` | Enable kernel synchronization of the real-time clock (RTC) | `true` |
| `chrony_maxdistance` | Maximum allowed root distance in seconds | `3.0` |
| `chrony_ntsdumpdir` | Directory for storing NTS cookies and keys | `/var/lib/chrony` |
| `chrony_num_minsources` | Minimum number of sources required for synchronization | `1` |
| `chrony_maxupdateskew` | Maximum allowed skew for updates (in ppm) | `100.0` |
| `chrony_makestep` | Step clock if offset is larger than threshold (format: "<threshold> <limit>") | `"1.0 3"` |
| `chrony_logchange` | Log clock changes larger than specified seconds | `"0.5"` |
| `chrony_leapsectz` | Leap seconds timezone | `"right/UTC"` |
| `chrony_log_enable` | Enable logging | `true` |
| `chrony_logdir_path` | Directory for storing log files | `/var/log/chrony` |
| `chrony_log_options` | What information to log (options: measurements, statistics, tracking, rtc, refclocks, tempcomp) | `"measurements statistics tracking"` |
| `chrony_ntp_clients` | List of allowed NTP clients (commented out by default) | `[]` |

### Logrotate Options

| Variable | Description | Default |
|----------|-------------|---------|
| `chrony_logrotate_config_path` | Path to logrotate configuration file | `/etc/logrotate.d/chrony` |
| `chrony_logrotate_options.archive_directory_path` | Directory where archived logs will be stored | `/var/log/chrony` |
| `chrony_logrotate_options.frequency` | How often to rotate logs (options: hourly, daily, weekly, monthly) | `"daily"` |
| `chrony_logrotate_options.count` | Number of rotated log files to keep | `30` |
| `chrony_logrotate_options.missingok` | Don't error if log file is missing | `true` |
| `chrony_logrotate_options.compress` | Compress rotated logs using gzip | `true` |
| `chrony_logrotate_options.nocreate` | Don't create new empty log file | `true` |
| `chrony_logrotate_options.copytruncate` | Don't use copy+truncate - use default move | `false` |
| `chrony_logrotate_options.dateext` | Add date extension to rotated logs | `true` |

## Tags

- `chrony` - All tasks
- `chrony:install` - Installation tasks
- `chrony:configure` - Configuration tasks
- `chrony:service` - Service management tasks
- `chrony:logrotate` - Log rotation tasks
- `chrony:test` - Testing tasks

## Example Playbook

```yaml
---
- name: Configure Chrony
  hosts: all
  become: true
  roles:
    - role: grzegorzfranus.chrony
      vars:
        chrony_ntp_servers:
          - "pool.ntp.org"
          - "time.google.com"
        chrony_logrotate_options:
          frequency: "daily"
          count: 7
          compress: true
```

## Testing

This role includes Molecule tests for multiple platforms:

```bash
# Run tests for all platforms
molecule test

# Run tests for specific platform
molecule test -s ubuntu
molecule test -s default
```

## License

Apache-2.0

## Author Information

- Grzegorz Franus
- EWARE