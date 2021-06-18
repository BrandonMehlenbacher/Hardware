import socket
import json
import numpy as np
import matplotlib.pyplot as plt

BUFFSIZE = 4096

class MSquaredLaser:
    def __init__(self,host,port):
        self._socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self._socket.settimeout(None)
        self._socket.connect((host,port))
        self._message ={
                            "message":{
                                    "transmission_id":[999],
                                    "op":"start_link",
                                    "parameters":{
                                                            "ip_address":"photothermal-2.chem.wisc.edu"
                                    }
                            }
                        }
        
        
    def _write(self, message):
        json_string  = json.dumps(message)
        self._socket.sendall(bytes(message,"utf-8"))
        
    def _read(self):
        returnedJSON = self._socket.recv(BUFFSIZE)

    def initialize(self):
        pass

    def set_wavlength(self):
        pass

    def get_wavelegnth(self):
        pass

    def set_scan_speed(self):
        pass

    def set_power(self):
        pass
    
    def get_power(self):
        pass


if __name__ == "__main__":
    pass
