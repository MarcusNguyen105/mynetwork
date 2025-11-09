# 3rd Party Services Analysis for Flag Finding

## Nmap Scan Summary
- **Target**: 10.12.0.136 (Windows system)
- **Flag Found**: CSEC-3961-QOTD (on port 17/QOTD)
- **Hint**: "This looks like a new, fully patched system. Maybe there is a vulnerable, 3rd party service installed instead."

## Common 3rd Party Services on Windows Systems

### Web Servers
- **IIS** (IIS): Ports 80, 443, 8080, 8443
- **Apache**: Ports 80, 443, 8080
- **Nginx**: Ports 80, 443, 8080
- **Tomcat**: Ports 8080, 8443, 8009

### Database Services
- **MySQL**: Port 3306
- **PostgreSQL**: Port 5432
- **MongoDB**: Port 27017
- **MS SQL Server**: Ports 1433, 1434
- **Oracle**: Ports 1521, 5500
- **Redis**: Port 6379

### File Transfer Services
- **FTP**: Ports 21, 2121
- **SFTP/SSH**: Port 22
- **FTPS**: Port 990
- **SMB/CIFS**: Ports 139, 445

### Application Servers
- **Jenkins**: Ports 8080, 50000
- **GitLab**: Ports 80, 443, 22
- **Jira**: Ports 8080, 8443
- **Confluence**: Ports 8090, 8443

### Remote Access
- **SSH**: Port 22
- **VNC**: Ports 5900-5910
- **TeamViewer**: Ports 5938, 80, 443

### Other Common Services
- **Elasticsearch**: Port 9200
- **Kibana**: Port 5601
- **Splunk**: Ports 8000, 8089
- **Docker**: Port 2375, 2376
- **Kubernetes API**: Port 6443

## Recommended Next Steps

1. **Full Port Scan**: Run a comprehensive scan to find all open ports
   ```bash
   nmap -p- -sV -sC 10.12.0.136
   ```

2. **Common Ports Scan**: Specifically check common 3rd party service ports
   ```bash
   nmap -p 21,22,80,443,3306,5432,8080,8443,1433,27017,9200,5601,8000,8089 10.12.0.136
   ```

3. **UDP Scan**: Some services run on UDP
   ```bash
   nmap -sU --top-ports 100 10.12.0.136
   ```

4. **Service Enumeration**: Once you find open ports, enumerate the services
   ```bash
   nmap -sV -sC -p <PORT> 10.12.0.136
   ```

5. **Version Detection**: Check for known vulnerabilities in identified services
   ```bash
   nmap --script vuln -p <PORT> 10.12.0.136
   ```

## Note
The current scan shows 993 filtered ports, which means many ports may be open but not responding to the scan. A more aggressive scan or different scan techniques may be needed to discover the 3rd party service mentioned in the hint.
