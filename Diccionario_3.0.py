telefono1 = {
    "Marca": "Apple",
    "Modelo": "Iphone SE 2daGeneracion",
    "Precio": "10,500"}
telefono2 = {
    "Marca": "Apple",
    "Modelo": "Iphone 13",
    "Precio": "25,500"}

telefono1.pop("Modelo")
del telefono1["Precio"]
telefono1.clear()

telefono3 = ("Marca","Modelo","Precio")
vacio = "Valor vacio"

telefono3= dict.fromkeys(telefono3,vacio)

vistaTelefono = telefono2.keys()

telefono2.update({"Color": "Negro"})

print(telefono1)
print(telefono3)
print(vistaTelefono)
print(telefono2)