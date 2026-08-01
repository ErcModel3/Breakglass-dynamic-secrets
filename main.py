import socketserver
from rotate import rotate_breakglass_user
from rich.console import Console

console = Console()

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
        syslog = data.decode(errors="replace").split()

        device_ip, device_port = self.client_address
        print(f'{device_ip}:{device_port} sent: {data.decode(errors="replace")}')

        print(f' Reading this: {syslog[5]} and {syslog[7]}')

        if syslog[5].rstrip(":") == "UI_LOGIN_EVENT":
                if "bg" in syslog[7].lower():
                    console.print("Breakglass user login detected...", style="yellow")
                    rotate_breakglass_user()

# For udp server
with socketserver.UDPServer(("10.0.0.91", 1515), UdpSyslogHandler) as server:
    print("... listening for Syslog messages ...")
    server.serve_forever()
