from lib import *
import time


class Satellite(SpaceEntity):
    def __init__(self, name, distance_from_earth):
        super().__init__(name, distance_from_earth)

    def receive_signal(self, packet):
        print(f"{self.name} Received: {packet}")

class BrokenConnectionError(CommsError):
    pass
def attempt_transmission(packet):
    while True:
        try:
            network.send(packet)
            break
        except TemporalInterferenceError:
            print("Interference, waiting...")
            time.sleep(2)
        except DataCorruptedError:
            print("corrupted data, retrying...")
        except LinkTerminatedError:
            print("link lost")
            raise BrokenConnectionError
        except OutOfRangeError:
            print("target out of range")
            raise BrokenConnectionError

network = SpaceNetwork(3)
sat1 = Satellite("sat1", 100)
sat2 = Satellite("sat2", 200)
pac1 = Packet("hello", sat1, sat2)
try:
    attempt_transmission(pac1)
except BrokenConnectionError:
    print("Transmission failed")