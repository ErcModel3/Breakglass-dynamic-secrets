import socketserver

class SyslogHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} sent:".format(self.client_address[0]))
        print(self.data)

# For tcp server
# with socketserver.TCPServer(("10.0.0.91", 1515), SyslogHandler) as server:
#     print("... listening for Syslog messages ...")
#     server.serve_forever()

class UdpSyslogHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        syslog = data.decode(errors="replace")
        meep = syslog.split()

        device_ip, device_port = self.client_address
        print(f'{device_ip}:{device_port} sent: {data.decode(errors="replace")}')

        print(f' Reading this: {meep[5]} and {meep[7]}')

        if meep[5].rstrip(":") == "UI_LOGIN_EVENT":
            print("MAHORAHA HELP ME HELP ME")



# For udp server
with socketserver.UDPServer(("10.0.0.91", 1515), UdpSyslogHandler) as server:
    print("... listening for Syslog messages ...")
    server.serve_forever()
