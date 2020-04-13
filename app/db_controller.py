from py2neo import Graph


class DBController:
    # TODO: connection refused of db
    graph = None

    def __init__(self, ip_address, password):
        self.__connect(ip_address, password)

    def __connect(self, ip_address, password):
        self.graph = Graph(ip_address, password=password)
