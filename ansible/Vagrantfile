# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.


Vagrant.configure("2") do |config|
    config.vm.box = "gbailey/amzn2"
    config.ssh.insert_key = true
  
    config.vm.define "ubnt", primary: true do |config|
      config.vm.provider "virtualbox" do |v|
          v.customize ["modifyvm", :id, "--memory", "4096", "--cpus", "2"]
      end
      config.vm.network :private_network, ip: "192.168.44.10"
      config.vm.hostname = "ubnt"
      config.vm.network :forwarded_port, guest: 22, host: 2222
        
      config.vm.provision "ansible" do |ansible|
        ansible.inventory_path = "dev"
        ansible.playbook = "site.yml"
        ansible.verbose = "vv" 
      end
    end
    
  end