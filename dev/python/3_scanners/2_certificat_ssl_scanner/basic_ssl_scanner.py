import nmap

def scan_ssl_certificates(target_ip, ports):
    nm = nmap.PortScanner()

    for port in ports:
        result = nm.scan(target_ip, arguments=f"-p {port} --script ssl-cert")
        
        if 'ssl-cert' in nm[target_ip]['tcp'][port]['script']:
            certificate_info = nm[target_ip]['tcp'][port]['script']['ssl-cert']
            print(f"SSL certificate information for port {port}:")
            print(f"Subject: {certificate_info['subject']}")
            print(f"Issuer: {certificate_info['issuer']}")
            print(f"Valid From: {certificate_info['validity']['start']}")
            print(f"Valid Until: {certificate_info['validity']['end']}")
            print()

if __name__ == "__main__":
    target_ip = "example.com"  # Replace with the target IP address or domain
    ports_to_scan = "443"      # Replace with the port(s) you want to scan

    scan_ssl_certificates(target_ip, ports_to_scan)
