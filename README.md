Proxmox HomeLab and Backup Server

This repository documents the setup and configuration of my Proxmox-based home lab environment, including a Proxmox VE (Virtual Environment) server for hosting virtual machines and containers, and a Proxmox Backup Server (PBS) for robust data backup and recovery.
Table of Contents

    Proxmox HomeLab

        Hardware Specifications

        Current Status

        Virtual Machines and Containers

    Proxmox Backup Server (PBS)

        Hardware Specifications

        Storage Configuration

        Backup Strategy

    Network Configuration

    Future Plans

    Contributing

    License

Proxmox HomeLab

My Proxmox VE instance serves as the core of my home lab, providing a flexible and powerful platform for experimenting with various operating systems, applications, and network services.
Hardware Specifications

    CPU: 4 x Intel(R) Core(TM) i5-6500T CPU @ 2.50GHz (1 Socket)

    RAM: 31.23 GiB (1.85 GiB currently in use)

    Storage: 1.71 TiB (638.48 GiB currently in use)

    Kernel: Linux 6.8.12-9-pve (2025-03-16T19:10Z)

    Boot Mode: EFI

    Manager Version: pve-manager/8.4.0/dec58e45e1fbc02ac

    Uptime: (As of latest screenshot) Approximately 1 day, 11 hours

Current Status

The Proxmox VE server (pve) is currently operational with low CPU usage and sufficient RAM and disk space available.
Virtual Machines and Containers

The following virtual machines (VMs) and containers (CTs) are part of this home lab environment:

VM/CT ID
	

Type
	

Description
	

Tags
	

Notes

100
	

qemu
	

VM (VM 102)
	


	


102
	

netbox
	

netbox
	


	


103
	

qemu
	

docker
	


	


104
	

qemu
	

Ubuntu
	

community-script
	


105
	

qemu
	

Security-Workstation
	


	


106
	

qemu
	

FedoraVM
	


	


107
	

qemu
	

DEVASC-LABVM
	


	


108
	

qemu
	

Windows-Server-2025
	


	


109
	

qemu
	

Windows-Server-2022
	


	


110
	

qemu
	

Windows-Server-2019
	


	


115
	

DockerHost-Ubuntu22.04
	

Docker Host Ubuntu 22.04
	


	


116
	

Arch-Linux-VM
	

Arch Linux VM
	


	


117
	

openwrtvm
	

OpenWRT VM
	


	


120
	

qemu
	

PiSense
	


	


121
	

qemu
	

Kali-trai
	


	


122
	

Metasploitable2-Linux
	

Metasploitable2 Linux
	


	


123
	

Window7
	

Windows 7
	


	


150
	

CML 7.2
	

Cisco Modeling Lab 7.2
	


	


151
	

Windows-Server-2025
	

Windows Server 2025
	


	


152
	

Windows-Server-2022
	

Windows Server 2022
	


	


153
	

Windows-Server-2019
	

Windows Server 2019
	


	


198
	

WIN11-AEI-2022
	

Windows 11 AEI 2022
	


	


200
	

HackingLive
	

HackingLive VM
	


	


201
	

PAC2025
	

PAC2025 VM
	


	


202
	

USCC-PAC2025
	

USCC PAC2025
	


	


202
	

USCC-East-2025-Day1
	

USCC East 2025 Day 1
	

linux-cpe
	


202
	

USCC-Win-XP-SP3
	

USCC Windows XP SP3
	


	


210
	

Kali-trai
	

Kali Linux
	


	


9001
	

ubuntu-test
	

Ubuntu Test Template
	


	


9000
	

ubuntu-2204-template
	

Ubuntu 22.04 Template
	


	


Note: Some VMs/CTs may not be currently running based on the screenshot, or are templates.
Proxmox Backup Server (PBS)

The Proxmox Backup Server is dedicated to securely storing backups of all critical data from the Proxmox VE host and its virtual machines.
Hardware Specifications

    CPU: 4 x Intel(R) Core(TM) i5-6500T CPU @ 2.50GHz (1 Socket)

    RAM: 15.41 GiB (914.89 MiB currently in use)

    Storage (root): 980.56 GiB (670.96 GiB currently in use, 68.43% utilized)

    Kernel: Linux 6.8.12-11-pve (2025-05-27T09:30Z)

    Boot Mode: EFI

    Uptime: (As of latest screenshot) Approximately 7 days, 8 hours

Storage Configuration

    Datastore: Proxmox-DataStore

        Size: 930.67 GiB

        Used: 670.96 GiB

        Available: 259.71 GiB

        Usage %: 72.09%

        Estimated Full: In 7 days 3h 19m (at current rate)

Backup Strategy

[You can elaborate on your backup strategy here. For example: "Daily backups of critical VMs are performed to the Proxmox-DataStore. Retention policies are set to keep X days of daily backups, Y weeks of weekly backups, and Z months of monthly backups."]
Network Configuration

[Briefly describe your network setup. For example: "The home lab operates on a segmented network, with VMs configured on various VLANs for isolation and security. Specific details of IP ranges and VLANs may be added here if desired and not sensitive."]
Future Plans

[List any future enhancements, additions, or changes you plan for your home lab. For example:]

    Implement a dedicated firewall VM (e.g., pfSense or OPNsense) for enhanced network security.

    Explore Kubernetes for container orchestration.

    Add more storage to the PBS as needed.

    Automate VM/CT deployments using Ansible or Terraform.

    Set up a monitoring stack (e.g., Prometheus, Grafana).

Contributing

This repository is primarily for my personal documentation. However, if you have suggestions or improvements, feel free to open an issue or pull request.
License

[You can choose a license for your documentation, e.g., MIT, Apache 2.0, etc. If no specific license, you can state "All rights reserved." or similar.]
