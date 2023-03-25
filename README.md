# Ansible Playbook to Configure Debian 11 Server

## This playbook automates the configuration of a Debian 11 server. 

Some handy links:
* [Vagrant documentation](https://developer.hashicorp.com/vagrant/docs).
* [Ansible documentation](https://docs.ansible.com/).
* [Using collections via Ansible](https://docs.ansible.com/ansible/latest/collections_guide/index.html).
* [Docker with Ansible](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html).
* [How to use roles with Ansible](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html).
* [Protecting sensitive data with Ansible vault](https://docs.ansible.com/ansible/latest/vault_guide/index.html).
* [Information about systemd services](https://linuxhandbook.com/create-systemd-services/).

### Prerequisites

VirtualBox:

[Link how to install it](https://phoenixnap.com/kb/install-virtualbox-on-ubuntu).

Vagrant:

`$ sudo apt-get install vagrant`

Pip package manager:

`$ sudo apt-get install python-pip`

Ansible:

`$ pip install ansible`

NOTE: Latest version of Ansible mostly accessible via pip. So You need to install with it!

Docker, if you want to create your own image:

[Docker installation](https://docs.docker.com/engine/install/debian/).

### The project performs the following tasks:

* Create a VM via Vagrant.
* Changes the root password
* Updates and upgrades all apt packages
* Installs tools:
    1. sudo
    1. Midnight Commander
    1. htop
    1. nginx
    1. iptables
    1. AdoptOpenJDK 8
    1. OpenJDK 11
    1. git
* Sets the default Java version to 8
* Changes the SSH port to 2222
* Enables PEM-based authentication and block password authentication.
* Installs fail2ban and configures it to ban IPs after 3 failed SSH login attempts
* Installs mariadb container from docker-hub
* Installs a simple flask application from docker-hub


### Usage

Modify ansible.cfg and inventory.ini files for your setup!

Run the following command inside the same directory as the `Vagrantfile`:

`$ vagrant up`

Then run the playbook from the same folder as the `sites.yml`:

`$ ansible-playbook sites.yml`

**IMPORTANT NOTE:** Once you run the playbooks you have to forward guest's `port 2222` to host's `port 2222`, because the playbook modify the default ssh port!!!

>### Scripts for the given tasks:

**1.** [Creating MySQL Dump](https://gist.github.com/Maarsupilami/943893bcdeec2e24111334f79d2253ee).

>Set to run daily at 2 am using the cron job scheduling utility.
>>```bash
>>$ crontab -e
>>```

Then add this line to the file `0 2 * * * ~/mysql_dump.sh`

**2.** [Lists the three most recently modified files in the `/var/log` directory](https://gist.github.com/Maarsupilami/f249eaf4b6a5188d7fed3891675b8ede).

**3.** [Lists all the files that have been modified in the last five days in the `/var/log/*` directories](https://gist.github.com/Maarsupilami/f249eaf4b6a5188d7fed3891675b8ede).

**4.** [Reads the 15-minute load average from the `/proc/loadavg` file](https://gist.github.com/Maarsupilami/09e0d7ca2fefb0d8a9fa055af0f8de88).

**5.** [Replaces a string](https://gist.github.com/Maarsupilami/9cc535b24064617cea56f3d54d9a2e2f).

>>> :wq :) :) :)