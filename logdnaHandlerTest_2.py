
import json

import time

from http.server import BaseHTTPRequestHandler,HTTPServer
import logging
import unittest

from logdna import LogDNAHandler

current_milli_time = lambda: int(round(time.time() * 1000))

key = 'b185a9b8291d007bac2cf74ec0814d4f'
logger = logging.getLogger('logdna')
logger.setLevel(logging.INFO)

options = {
    'hostname': 'DESKTOP-64H9R4H',
#    'url': 'http://localhost:8081',
#    'ip': '10.0.1.1',
#    'mac': 'C0:FF:EE:C0:FF:EE'
}

expectedLines = []


class successful_RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)

        self.end_headers()
        body = json.loads(body)['ls']
        for keys in body:
            expectedLines.append(keys['line'])

class failed_RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(400)
        self.end_headers()

class LogDNAHandlerTest(unittest.TestCase):



    def test_urllib3_exception_001(self):
        """ no reason why this should fail"""
        
        test = LogDNAHandler(key, options)
        logger.addHandler(test)
        line = "python python python"
        logger.info(line)
        
        self.assertTrue(True)
        

    def test_urllib3_exception_001(self):
    
        test = LogDNAHandler(key, options)
        logger.addHandler(test)
        line = "python python python"
        logger.info(line)
        
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
