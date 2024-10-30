from abc import abstractmethod
from abc import ABC

#Lisa set up inventory system base class with group, trio-programming.
class Inventory(ABC):
    @abstractmethod
    def __init__(self):
       pass
    
    @abstractmethod
    def __str__(self):
        """Return a string representation of all items in the system."""
        pass  

    # load csv file Peter V help from professor
    @abstractmethod
    def load_data(self, item_information_file):
       pass

    # Gabriel Calderon
    @abstractmethod
    def get_satellites(self):
        pass
    
    # Gabriel Calderon
    @abstractmethod
    def search(self, attribute, value):
        pass
   
   # Lisa M.
    @abstractmethod
    def birthday_search(self, date):
        pass
    
    # Lisa M.
    @abstractmethod
    def delete(self, attribute, value):
        pass
    
    # Lisa M.
    @abstractmethod
    def write_back(self):
       pass
    
    # Peter V.
    @abstractmethod
    def add_satellite(self):
       pass

    @abstractmethod
    def search_function(self, search):  # Peter V. search function
        pass