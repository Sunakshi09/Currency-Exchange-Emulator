class Currency:

currencies = {
    'CHF': 0.930023,  #swiss franc 
    'CAD': 1.264553,  #canadian dollar
    'GBP': 0.737414,  #british pound
    'JPY': 111.019919,  #japanese yen
    'EUR': 0.862361,  #euro
    'USD': 1.0  #us dollar
}

def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit