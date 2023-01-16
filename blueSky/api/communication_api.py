import logging
import MetaTrader5 as mt5
from blueSky.core import get_data_by_bar

logger = logging.getLogger(__name__)

class CommunicationApi():
    
    def disconnect(self):
        mt5.shutdown()
    
    def connect(self, logon_info):
        

    def get_historical(self, stock):

    