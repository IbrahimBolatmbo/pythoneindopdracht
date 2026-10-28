boodschappenlijst = ["brood", "melk", "eieren", "kaas", "appels"]

boodschappenlijst.append("bananen")
boodschappenlijst.append("pasta")

boodschappenlijst.remove("kaas")

print(f"Aantal producten: {len(boodschappenlijst)}")
print("Boodschappenlijst:", boodschappenlijst)

if "melk" in boodschappenlijst:
    print("Melk staat op de boodschappenlijst.")
else:
    print("Melk staat niet op de boodschappenlijst.")