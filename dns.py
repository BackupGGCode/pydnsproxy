# -*- encoding: utf-8 -*-
from SocketServer import ThreadingUDPServer, BaseRequestHandler, UDPServer
from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM, timeout
import sys, os
from common import *

gl_remote_server = None

class LocalDNSHandler(BaseRequestHandler):
    def setup(self):
        global gl_remote_server
        if not gl_remote_server:
            remote_server = DEF_REMOTE_SERVER
        else:
            remote_server = gl_remote_server
        self.dnsserver = (remote_server, DEF_PORT)
        self.tcp_socket = None 

    def handle(self):
        data, client_socket = self.request
        cache = self.server.cache
            resp = cache.get(data)
            if not resp:
                resp = self._getResponse(data)
                cache[data] = resp
        try:
          client_socket.sendto(resp, self.client_address)
        except StandardError as err:
          print err

    def _getResponse(self, data):
        "Send client's DNS request (data) to remote DNS server, and return its response."
        sock = socket(AF_INET, SOCK_DGRAM) # socket for the remote DNS server
        sock.connect(self.dnsserver)
        sock.sendall(data)
        sock.settimeout(5)
        try:
            rspdata = sock.recv(65535)
        except Exception, e:
            print e, 'ignored.'
            return 1
        # "delicious food" for GFW:
        while 1:
            sock.settimeout(DEF_TIMEOUT)
            try:
                rspdata = sock.recv(65535)
            except timeout:
                break
        sock.close()
        return rspdata

class LocalDNSServer(ThreadingUDPServer):
    cache = {}

def main():
    global gl_remote_server
    try:
        if hasattr(sys, 'frozen'):
            dir = os.path.dirname(sys.executable)
        else:
            dir = os.path.dirname(__file__)
        confFile = os.path.join(dir, DEF_CONF_FILE)
        f = open(confFile, 'r')
        dns = f.read().split('=')
        f.close()
        if len(dns) == 2:
            if dns[0].strip().lower() == 'dns':
                gl_remote_server = dns[1].strip()
            else:
                pass
    except:
        pass
    dnsserver = LocalDNSServer((DEF_LOCAL_HOST, DEF_PORT), LocalDNSHandler)
    dnsserver.serve_forever()

if __name__ == '__main__':
    main()
