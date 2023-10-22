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
    self.unit = 
  def changeTo(self, new_unit):
    self.value = (self.value / Currency.currencies[self.unit] *
                  Currency.currencies[new_unit])
    self.unit = new_unit

  #add magic methods here
  def __repr__(self):
    return f"{round(self.value, 2)} {self.unit}"

  def __str__(self):
    return f"{round(self.value, 2)} {self.unit}"

  def __add__(self, other):
    if isinstance(other, Currency):
        new_currency = Currency(other.value, other.unit)
        new_currency.changeTo(self.unit)
        return f"{round(self.value + new_currency.value, 2)} {self.unit}"
    elif type(other) == int or float:
        result = Currency(other, 'USD')
        result.changeTo(self.unit)
        return f"{round(self.value + result.value, 2)} {self.unit}"
    else:
        return "Submit a currency or number value."

  def __radd__(self, other):
  new_currency = Currency(self.value, self.unit)
  new_currency.changeTo('USD')
  return f"{round(new_currency.value + other, 2)} {new_currency.unit}"

  def __sub__(self, other):
    if isinstance(other, Currency):
        new_currency = Currency(other.value, other.unit)
        new_currency.changeTo(self.unit)
        return f"{round(self.value - new_currency.value, 2)} {self.unit}"
    elif type(other) == int or float:
        result = Currency(other, 'USD')
        result.changeTo(self.unit)
        return f"{round(self.value - result.value, 2)} {self.unit}"
    else:
        return "Submit a currency or number value."

  def __rsub__(self, other):
  new_currency = Currency(other, 'USD')
  new_currency.changeTo(self.unit)
  return f"{round(new_currency.value - self.value, 2)} {self.unit}"

  v1 = Currency(23.43, "EUR")
  v2 = Currency(19.97, "USD")

  print(v1 + v2)
  print(v2 + v1)
  print(v1 + 3)  # an int or a float is considered to be a USD value
  print(3 + v1)
  print(v1 - 3) # an int or a float is considered to be a USD value
  print(30 - v2)