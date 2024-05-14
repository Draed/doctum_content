import socket
import threading

def scan_port(target_ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        sock.connect((target_ip, port))
        print(f"Port {port} is open")
    except socket.error:
        pass
    finally:
        sock.close()

def port_scanner(target_ip, start_port, end_port):
    print(f"Scanning ports on {target_ip}...\n")
    
    for port in range(start_port, end_port + 1):
        threading.Thread(target=scan_port, args=(target_ip, port)).start()

if __name__ == "__main__":
    target_ip = "51.159.186.212"  # Replace with the target IP address
    start_port = 1
    end_port = 10000

    port_scanner(target_ip, start_port, end_port)
