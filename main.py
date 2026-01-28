from lib import *


class Satellite(SpaceEntity):
    def receive_signal(self, packet):
        print(f"{self.name} Received: {packet}")

network = SpaceNetwork(1)
sat1 = Satellite("sat1", 100)
sat2 = Satellite("sat2",200)
pac1 = Packet("hello",sat1,sat2)
network.send(pac1)