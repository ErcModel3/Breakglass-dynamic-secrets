import socketserver

class SyslogHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} sent:".format(self.client_address[0]))
        print(self.data)

with socketserver.UDPServer(("10.0.0.91", 1515), SyslogHandler) as server:
    print("... listening for Syslog messages ...")
    server.serve_forever()
