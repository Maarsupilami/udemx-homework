Vagrant.configure("2") do |config|
  config.vm.box = "debian/bullseye64"
  config.vm.hostname = "debian-server-test"
   
  # Customize the VM
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
    vb.name = "debian-based-server"
  end
  
  # Set up private network with IP
  config.vm.network "private_network", ip: "192.168.56.1"

  # Forward ports from guest to host
  config.vm.network "forwarded_port", guest: 80, host: 10000

  # Set Ansible provisioning
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "server-init.yml"
    ansible.ask_vault_pass = true
  end
end
