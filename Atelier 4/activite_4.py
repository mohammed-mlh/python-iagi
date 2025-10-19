# Atelier 4 - Activite 4(TAF)
with open("Table_de_multiplication.txt", "w") as file:
    
    for i in range(1, 11):
        file.write(f"La table de multiplication de {i:02d}\n")
        for j in range(1, 11):
            product = i * j
            line = f"{i:02d} x {j:02d} = {product}\n" # pour afficher les nombre en 2 chiffre, par exemple "3" => "03"
            file.write(line)
        file.write("\n") 
