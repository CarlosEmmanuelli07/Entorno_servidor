## 7. Filtra los correos electrónicos válidos (contienen @).
l = ["paco@manolo.lagos", "pijas@RD.org", "pacodelugia@yahoo.dh", "hippie", "Weed"]

def CheckEmail(element):
    return element.find("@") > 0

l2 = filter(CheckEmail, l)
print(list(l2))