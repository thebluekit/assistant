from py2neo import Graph


class DBController:
    def __init__(self, ip_address, password):
        self.graph = Graph(ip_address, password=password)
