class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


class Server:
    count = 0

    def __init__(self):
        self.buffer = []
        Server.count += 1
        self.ip = Server.count
        self.rout = None

    def send_data(self, data: Data):
        self.rout.buffer.append(data)

    def get_data(self) -> list:
        temp = self.buffer.copy()
        self.buffer = []
        return temp

    def get_ip(self) -> int:
        return self.ip


class Router:
    def __init__(self):
        self.servers = []
        self.buffer = []

    def link(self, server: Server):
        self.servers.append(server)
        server.rout = self

    def unlink(self, server: Server):
        self.servers.remove(server)
        server.rout = None

    def send_data(self):
        for data in self.buffer:
            for server in self.servers:
                if server.ip == data.ip:
                    server.buffer.append(data)
        self.buffer = []
