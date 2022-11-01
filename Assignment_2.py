#python code for getting temperature and humidity value and detect alarm
from random import randint
def generating_tempvalue():
    return randint(1,150)
def generating_humidityvalue():
    return randint(1,150)
random_temvalue=generating_temvalue()
print("The value of temperature is:",random_temvalue)
random_humidityvalue=generating_humidityvalue()
print("The value of humidity is:",random_humidityvalue)
if random_temvalue>80:
    print(High humidity\n********ALERT SIGNAL*******")
          else:
          print("High temperature detected")
          elif random_temvalue==80:
          print("Temperature is at maximum level")
          else:
          print("Normal")
