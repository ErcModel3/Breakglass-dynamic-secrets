import socketserver

class SyslogHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(f"Received: {self.data}")
        self.request.sendall(self.data.upper())


def main():
    print("Hello from breakglass-dynamic-secrets!")

if __name__ == "__main__":
    main()
