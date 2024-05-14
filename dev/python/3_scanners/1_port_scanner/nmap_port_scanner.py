import nmap

def scan_ports(target_ip, ports):
    nm = nmap.PortScanner()
    
    for port in ports:
        result = nm.scan(target_ip, port)
        
        if nm[target_ip]['tcp'][port]['state'] == 'open':
            print(f"Port {port} is open")

if __name__ == "__main__":
    target_ip = "51.159.186.212"
    ports_to_scan = "1-5000"

    scan_ports(target_ip, ports_to_scan)
