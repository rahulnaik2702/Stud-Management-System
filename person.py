from abc import ABC,abstractmethod

class Persons(ABC):

    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @staticmethod  
    def validate_number(number):
        if len(number)==10:
            return True
        else:
            return False