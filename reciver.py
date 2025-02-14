from SX127x.LoRa import *
from SX127x.board_config import BOARD

BOARD.setup()

class MyLoRa(LoRa):

  def __init__(self, verbose=False):
    super(MyLoRa, self).__init__(verbose)
    self.set_freq(433.0) #wkleić częstotliwość
    self.set_mode(MODE.STDBY)
    
    

  def listening_mode(self):
    while True:
        payload = self.read_payload(nocheck=True) 
        print(payload)

LoRa_listener = MyLoRa()
LoRa_listener.listening_mode()
