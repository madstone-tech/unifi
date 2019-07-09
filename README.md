# Install UniFi Controller


Role Name
=========

The following roles runs through the following tasks

### Common

1. enable epel repo
2. install and configure fail2ban
3. install and setups firewalld rules
4. install ntp
5. setups timezone
6. install and start yum-cron
7. update all packages

### ubnt

1. Install java-1.8.0-openjdk
2. install mongodb
3. create an ubnt user
4. download unifi package
5. setups the unifi.service
6. start unifi.service

### update

1. stop mongo service
2. stop unifi service
3. upgrade all packages
4. rename UniFi folder
5. download new UniFi package
6. copy dta and config to new install
7. start mongo service
8. start unifi service


Requirements
------------

* Amazon-linux-2
  
Role Variables
--------------


| variable         | default           |
| ---------------- | ----------------- |
| `_ubnt_version_` | `5.10.25`         |
| `_time_zone_`    | `America/Chicago` |


File Directory
==============


```
├── dev
├── group_vars
│   └── all.yml
├── production
├── README.md
├── roles
│   ├── common
│   │   ├── files
│   │   │   └── unifi.xml
│   │   └── tasks
│   │       └── main.yml
│   ├── ubnt
│   │   ├── files
│   │   │   └── unifi.service
│   │   └── tasks
│   │       └── main.yml
│   └── update
│       └── tasks
│           └── main.yml
├── site.yml
├── update.yml
├── Vagrantfile

```

License
-------

BSD

Author Information
------------------

Andhi Jeannot
[MADSTONE TECHNOLOGY][2]

[2]: https://madstone.io