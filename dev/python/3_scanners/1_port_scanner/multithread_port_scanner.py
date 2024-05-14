import socket
import threading
import argparse

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def worker(host, ports, results):
    while True:
        port = ports.get()
        if port is None:
            break
        if scan_port(host, port):
            results.append(port)

def run_port_scanner(host, port_range, num_threads):
    ports = list(range(port_range[0], port_range[1] + 1))
    results = []

    thread_pool = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(host, ports, results))
        thread.start()
        thread_pool.append(thread)

    for thread in thread_pool:
        thread.join()

    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-threaded Port Scanner")
    parser.add_argument("host", help="Target host")
    parser.add_argument("start_port", type=int, help="Start of port range")
    parser.add_argument("end_port", type=int, help="End of port range")
    parser.add_argument("--threads", type=int, default=4, help="Number of threads")
    args = parser.parse_args()

    host = args.host
    port_range = (args.start_port, args.end_port)
    num_threads = args.threads

    open_ports = run_port_scanner(host, port_range, num_threads)

    print("Open ports:")
    print(open_ports)
