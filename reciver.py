from SX127x.LoRa import *
from SX127x.board_config import BOARD

class MyLoRa(LoRa):

  def __init__(self, verbose=False):
    BOARD.setup()
    lora.set_freq(433.0) 
    lora = LoRa()
    lora.set_mode(MODE.STDBY)
    super(MyLoRa, self).__init__(verbose)
    

  def on_rx_done(self):
    while True:
        payload = self.read_payload(nocheck=True) 
        print(payload)