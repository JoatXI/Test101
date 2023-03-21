class Vehicles:
        
    def __init__(self, registration, weight):
        self.registration = registration
        self.weight = weight
        
    def calculate_fee(self):
        pass
    
class Motorbike(Vehicles):
    
    def __init__(self, registration, weight):
        Vehicles.__init__(self, registration, weight)

class Car(Vehicles):
    
    def __init__(self, registration, weight):
        Vehicles.__init__(self, registration, weight)

class Lorry(Vehicles):
    
    def __init__(self, registration, weight):
        Vehicles.__init__(self, registration, weight)