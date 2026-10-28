product_1_naam = "Brood"
product_1_prijs = 2.50
product_1_aantal_verkocht = 5

product_2_naam = "Melk"
product_2_prijs = 1.80
product_2_aantal_verkocht = 10

product_3_naam = "Appels"
product_3_prijs = 0.75
product_3_aantal_verkocht = 20

totale_omzet = (
    product_1_prijs * product_1_aantal_verkocht
    + product_2_prijs * product_2_aantal_verkocht
    + product_3_prijs * product_3_aantal_verkocht
)

print(f"{product_1_naam}: EUR {product_1_prijs:.2f} per stuk, {product_1_aantal_verkocht} verkocht")
print(f"{product_2_naam}: EUR {product_2_prijs:.2f} per stuk, {product_2_aantal_verkocht} verkocht")
print(f"{product_3_naam}: EUR {product_3_prijs:.2f} per stuk, {product_3_aantal_verkocht} verkocht")
print(f"Totale omzet: EUR {totale_omzet:.2f}")