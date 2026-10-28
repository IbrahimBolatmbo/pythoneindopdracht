cijfer_nederlands = 5
cijfer_engels = 6
cijfer_wiskunde = 5

gemiddelde = (cijfer_nederlands + cijfer_engels + cijfer_wiskunde) / 3

if (
    cijfer_nederlands < 4
    or cijfer_engels < 4
    or cijfer_wiskunde < 4
):
    print("Gezakt!")
elif gemiddelde >= 5.5:
    print("Geslaagd!")
else:
    print("Gezakt!")
