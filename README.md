# 🏠 Marcus Nguyen's Home Lab Documentation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Proxmox](https://img.shields.io/badge/Proxmox-VE-orange)](https://www.proxmox.com/)
[![Splunk](https://img.shields.io/badge/Splunk-9.0.1-blue)](https://www.splunk.com/)
[![Documentation](https://img.shields.io/badge/Documentation-Wiki-green)](https://github.com/marcusnguyen/homelab/wiki)

> A comprehensive documentation repository for my personal IT home lab, featuring Proxmox virtualization, Splunk logging, and cybersecurity learning environments.

## 📋 Table of Contents

- [Overview](#overview)
- [Lab Architecture](#lab-architecture)
- [Hardware Specifications](#hardware-specifications)
- [Documentation](#documentation)
- [Technologies Used](#technologies-used)
- [Future Plans](#future-plans)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

**The Beginning: A Laptop's Limit**

My passion for IT, especially networking and servers, started small – on my laptop. But those early days were frustrating. Trying to run networking simulations with over 10 virtual devices would consistently crash my machine. It quickly became clear: if I wanted to truly learn and grow in server and networking administration, I needed a real solution.

**Proxmox was that solution.** It was a game-changer! I transitioned to mini PCs (Intel i3, i5, i7) to host my VM servers. Proxmox provided the stability and resources for complex environments, letting me master Linux and NGINX and freely experiment without hardware limitations. Crucially, I also set up VPN services (Tailscale) to securely access my servers remotely from anywhere, making my lab truly flexible. I also used it to practice all the labs given from the USCC challenge program, where I'm trained on SANS Institute courses to deepen my cybersecurity skills and knowledge.

![VPN Setup](https://github.com/user-attachments/assets/e055a04e-3304-4321-92f4-e51dcfc64f45)

## 🏗️ Lab Architecture

My Proxmox VE instance is now the heart of my home lab. It's a flexible and powerful platform where I experiment with different operating systems, applications, and network services, constantly honing my skills.

### Proxmox Virtualization Environment

![Proxmox HomeLab](https://github.com/user-attachments/assets/fe9b62c5-e91e-4915-82b3-fa8d7b254c00)

![Proxmox Resources](https://github.com/user-attachments/assets/b1325df5-3198-48b2-bc30-1d8d3dded4)

![Proxmox HomeLab-2](https://github.com/user-attachments/assets/4c74c940-ed07-41dd-a01f-3ba6deb3798e)

![Proxmox Resources-2](https://github.com/user-attachments/assets/d554d7a4-0fd0-4975-81c7-e8b468f508a3)

### Proxmox Backup Server (PBS): My Safety Net

A solid backup strategy is non-negotiable. My Proxmox Backup Server securely stores all critical data from my Proxmox VE host and its VMs, ensuring peace of mind.

![PBS Dashboard](https://github.com/user-attachments/assets/8ba5f535-eabd-4d9c-84a6-4c238916b801)

My PBS uses similar Intel Core i5 hardware with ample RAM. Its dedicated datastore is actively used but still has significant space, ensuring my valuable lab data is always protected.

**Backup Configuration:**
- Weekly backups of critical VMs to Proxmox-DataStore
- Retention policies set to keep 60 days of weekly backups
- Automated backup scheduling

**Network Architecture:**
My home lab runs on a segmented network, with VMs on various VLANs for better isolation and security. I can add specific IP ranges and VLAN details here if needed and not sensitive.

## 💻 Hardware Specifications

### Proxmox VE Host
- **CPU**: Intel Core i5
- **RAM**: Ample memory for virtualization
- **Storage**: Sufficient storage for VMs and containers
- **Status**: Running smoothly with plenty of resources to spare

### Proxmox Backup Server (PBS)
- **CPU**: Intel Core i5 (similar to main host)
- **RAM**: Ample RAM for backup operations
- **Storage**: Dedicated datastore with significant available space
- **Backup Policy**: Weekly backups with 60-day retention

### Network Configuration
- **Network**: Segmented network with VLANs for isolation and security
- **VPN**: Tailscale for secure remote access
- **Firewall**: Planning dedicated firewall VM (pfSense/OPNsense)

## 📚 Documentation

This repository contains comprehensive documentation for various aspects of my home lab:

### 📄 Available Documentation

| Document | Description |
|----------|-------------|
| [`README.md`](./README.md) | Main project overview and architecture |
| [`SplunkServer.md`](./SplunkServer.md) | Complete Splunk server installation and configuration guide |
| [`SplunkUniversalForwarder.md`](./SplunkUniversalForwarder.md) | Universal forwarder setup for Windows and Linux |
| [`Network Design_Volunteer work__Marcus Nguyen.pkt`](./Network%20Design_Volunteer%20work__Marcus%20Nguyen.pkt) | Packet Tracer network design file |

### 🖼️ Screenshots
- Proxmox dashboard and resource monitoring
- PBS backup server interface
- VPN configuration screenshots

## 🛠️ Technologies Used

### Virtualization & Infrastructure
- **Proxmox VE** - Primary hypervisor platform
- **Proxmox Backup Server (PBS)** - Backup and disaster recovery
- **Tailscale** - VPN for secure remote access

### Operating Systems & Distributions
- **Linux**: Ubuntu, Fedora, Arch, Kali Linux
- **Windows**: Various Windows Server versions
- **Specialized**: pfSense, OpenWRT

### Security & Monitoring
- **Splunk** - Log management and SIEM
- **Sysmon** - Windows system monitoring
- **MITRE ATT&CK** - Threat modeling and detection

### Networking Tools
- **pfSense** - Firewall and routing
- **OpenWRT** - Network device management
- **Cisco Packet Tracer** - Network simulation

## 🚀 Future Plans

Here are some things I'm planning for the lab:

- [ ] Setting up a dedicated firewall VM (like pfSense or OPNsense) for even stronger network security
- [ ] Exploring Kubernetes for container orchestration
- [ ] Adding more storage to the PBS as my needs grow
- [ ] Automating VM/CT deployments using tools like Ansible or Terraform
- [ ] Building out a monitoring stack (Prometheus, Grafana)
- [ ] Implementing network segmentation with VLANs
- [ ] Adding more cybersecurity training environments

## 🤝 Contributing

This repo is mainly for my personal documentation and learning. But if you have suggestions or improvements, feel free to:

1. **Open an issue** - Report bugs, suggest improvements, or ask questions
2. **Submit a pull request** - Contribute documentation improvements or new guides
3. **Share feedback** - Your insights are always welcome!

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**About the Author**: Marcus Nguyen - IT enthusiast passionate about networking, virtualization, and cybersecurity. Currently training with SANS Institute courses through the USCC challenge program.

*Last updated: December 2024*