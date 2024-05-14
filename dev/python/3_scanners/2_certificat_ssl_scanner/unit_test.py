import unittest
import time
from io import StringIO
import sys

# Import the function you want to test
from basic_ssl_scanner import scan_ssl_certificates

class TestSSLCertificateScanner(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements
        self.stdout_backup = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.stdout_backup

    def test_scan_ssl_certificates(self):
        target_ip = "example.com"
        ports_to_scan = "443"

        start_time = time.time()
        scan_ssl_certificates(target_ip, ports_to_scan)
        execution_time = time.time() - start_time

        # Check if the output contains the expected SSL certificate information
        output = sys.stdout.getvalue()
        self.assertIn("SSL certificate information for port 443:", output)
        self.assertIn("Subject:", output)
        self.assertIn("Issuer:", output)
        self.assertIn("Valid From:", output)
        self.assertIn("Valid Until:", output)

        print(f"\nExecution Time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    unittest.main()
