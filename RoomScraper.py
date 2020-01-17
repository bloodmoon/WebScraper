import requests

roomID = ['DL']

session = requests.session()

r = session.post("https://courses.osu.edu/psp/csosuct/EMPLOYEE/PUB/c/OSR_CUSTOM_MENU.OSR_ROOM_MATRIX.GBL?", data="DL")

print(str(r.text))
file = open("output", 'w')
file.write(str(r.text))
