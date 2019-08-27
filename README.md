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
* ansible 2.8+
  
Role Variables
--------------


| variable         | default           |
| ---------------- | ----------------- |
| `_ubnt_version_` | `5.11.39`         |
| `_time_zone_`    | `America/Chicago` |

Variables can be changed in the `group_vars/all.yml` file

Run Playbook for install
=========================

1. download the repo
2. update the variables to reflect your environment
3. modify the `production` file with your environment ip (localhost or remote)
4. to run the playbook type `ansible-playbook -i production site.yml`   

Run Playbook for update
=======================

1. udpate the `_ubnt_version_` in the `group_vars/all.yml` file
2. to run the playbook to update the controller type `ansible-playbook -i production update.yml`


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
