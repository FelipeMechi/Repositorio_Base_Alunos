codigo_convite = "vip"
convite = input("Você tem um convite válido? : ").strip().lower()
if codigo_convite == convite:
    print("Entrada permitida")
else:
    print("Entrada negada")