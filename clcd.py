class Vehicles:
        
    def __init__(self, registration, weight):
        self.registration = registration
        self.weight = weight
        
    def calculate_fee(weight):
        if weight == 1590:
            return 5
        elif weight > 8000:
            return 15
        return 3
    
class Motorbike(Vehicles):
    
    def __init__(self, registration, weight):
        Vehicles.__init__(self, registration, weight)
        
    def calculate_fee(self):
        return 3

class Car(Vehicles):
    
    def __init__(self, registration, weight):
        Vehicles.__init__(self, registration, weight)

class Lorry(Vehicles):
    
    def __init__(self, registration, weight):
        Vehicles.__init__(self, registration, weight)