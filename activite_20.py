adresses_ip = ["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1", "169.254.0.1"]
print(f"Liste originale : {adresses_ip}")

# Q1
print(f"La première : {adresses_ip[0]}")

# Q2
print(f"La dernière : {adresses_ip[-1]}")

# Q3
print(f"La troisième : {adresses_ip[2]}")

# Q4
adresses_ip.append("172.31.0.1")

# Q5
adresses_ip.remove("200.100.50.1")
print(f"La liste actuelle : {adresses_ip}")

# Q6
print(f"Le nombre d'adresses est {len(adresses_ip)}")

# Q7
if "192.168.0.1" in adresses_ip:
    print("192.168.0.1 est dans la liste")
else:
    print("192.168.0.1 n'est pas dans la liste")

# Dictionnaire des classes
classes_ip = {
    "192.168.0.1": "classe A",
    "10.0.0.1": "classe B",
    "172.16.0.1": "classe C",
    "200.100.50.1": "adresse ip publique",
    "169.254.0.1": "adresse ip de lien local (APIPA)"
}

# Q8
print(f"La classe de 10.0.0.1 : {classes_ip['10.0.0.1']}")

# Q9
adresses_ip.sort()
print(f"La liste ordonnée : {adresses_ip}")

# Q10
for el in classes_ip:
    if classes_ip[el] == "classe C":
        print(f"L'élément {el} est dans la classe C.")
    else:
        print(f"L'élément {el} n'est pas dans la classe C.")

# Q11
c = 0
for el in classes_ip:
    if classes_ip[el] == "adresse ip publique":
        c += 1

print(f"Le nombre d'éléments avec adresse IP publique est {c}")
