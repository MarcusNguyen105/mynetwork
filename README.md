**The Beginning: A Laptop's Limit**

My passion for IT, especially networking and servers, started small – on my laptop. But those early days were frustrating. Trying to run networking simulations with over 10 virtual devices would consistently crash my machine. It quickly became clear: if I wanted to truly learn and grow in server and networking administration, I needed a real solution.

Proxmox was that solution. It was a game-changer! I transitioned to mini PCs (Intel i3, i5, i7) to host my VM servers. Proxmox provided the stability and resources for complex environments, letting me master Linux and NGINX and freely experiment without hardware limitations. Crucially, I also set up VPN services to securely access my servers remotely from anywhere, making my lab truly flexible. I also used it to practice all the labs given from the USCC challenge program, where I'm trained on SANS Institute courses to deepen my cybersecurity skills and knowledge.

My Proxmox VE instance is now the heart of my home lab. It's a flexible and powerful platform where I experiment with different operating systems, applications, and network services, constantly honing my skills. My Proxmox VE server is powered by an Intel Core i5 CPU and a good amount of RAM and storage, providing a stable and efficient environment for virtualization. It's currently running smoothly with plenty of resources to spare.

I host a variety of VMs and containers for different projects and learning opportunities. This includes various Linux distributions (like Ubuntu, Fedora, Arch, Kali), Windows Server versions, specialized networking tools (like PfSense, OpenWRT, Splunk), and other lab-specific instances for security and development. Each one helps me explore new IT horizons.


<img width="1907" height="821" alt="Proxmox HomeLab" src="https://github.com/user-attachments/assets/fe9b62c5-9e76-4915-82b3-fa8d7b254c00" />

<img width="1906" height="587" alt="Proxmox- Resources" src="https://github.com/user-attachments/assets/b1325df5-3198-48b2-bc30-1c898d9dded4" />


<img width="1916" height="846" alt="Proxmox HomeLab-2" src="https://github.com/user-attachments/assets/4c74c940-ed07-41dd-a01f-3ba6deb3798e" />

<img width="1901" height="637" alt="Proxmox- Resources-2" src="https://github.com/user-attachments/assets/d554d7a4-0fd0-4975-81c7-e8b468f508a3" />




Proxmox Backup Server (PBS): My Safety Net



A solid backup strategy is non-negotiable. My Proxmox Backup Server securely stores all critical data from my Proxmox VE host and its VMs, ensuring peace of mind.

<img width="1912" height="871" alt="PBS" src="https://github.com/user-attachments/assets/8ba5f535-eabd-4d9c-84a6-4c238916b801" />

My PBS uses similar Intel Core i5 hardware with ample RAM. Its dedicated datastore is actively used but still has significant space, ensuring my valuable lab data is always protected.

Weekly backups of critical VMs are performed to the Proxmox-DataStore. Retention policies are set to keep 60 days of weekly backups.

My home lab runs on a segmented network, with VMs on various VLANs for better isolation and security. I can add specific IP ranges and VLAN details here if needed and not sensitive.


Here are some things I'm planning for the lab:
- Setting up a dedicated firewall VM (like pfSense or OPNsense) for even stronger network security.
- Exploring Kubernetes for container orchestration.
- Adding more storage to the PBS as my needs grow.
- Automating VM/CT deployments using tools like Ansible or Terraform.
- Building out a monitoring stack (Prometheus, Grafana).

This repo is mainly for my personal documentation and learning. But if you have suggestions or improvements, feel free to open an issue or pull request. Your insights are always welcome!

