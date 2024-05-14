import asyncio
import socket
import time
import unittest

async def scan_port(host, port, results):
    try:
        reader, writer = await asyncio.open_connection(host, port)
        results[port] = True
        writer.close()
    except (socket.timeout, ConnectionRefusedError):
        results[port] = False

async def run_port_scanner(host, ports):
    results = {}
    tasks = [scan_port(host, port, results) for port in ports]
    await asyncio.gather(*tasks)
    return results

class TestPortScanner(unittest.TestCase):
    def test_port_scanner(self):
        host = "51.159.186.212"
        ports = [22, 443, 8080, 5000]
        
        start_time = time.time()
        results = asyncio.run(run_port_scanner(host, ports))
        end_time = time.time()

        print("Port scanning results:")
        for port, is_open in results.items():
            print(f"Port {port} is {'open' if is_open else 'closed'}.")

        execution_time = end_time - start_time
        print(f"Port scanning took {execution_time:.4f} seconds.")

        # Add assertions based on your expectations
        self.assertTrue(22 in results)
        # self.assertTrue(443 in results)
        # self.assertTrue(8080 in results)

if __name__ == "__main__":
    unittest.main()
