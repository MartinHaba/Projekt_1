'''
#Slicing
print("Prvních 5 písmen:")
print("indexování"[:5])
print("Posledních 5 písmen:")
print("indexování"[-5:])
print("Každé 3. písmeno (počínaje prvním) od 'i':")
print("indexování"[::3])
'''

'''
#Převodník
#Převodní poměry
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

#Počty hodnot
kg_pocet = 80
km_pocet = 54
l_pocet = 5

kg_vysledek = kg_lb * kg_pocet
km_vysledek = km_mile * km_pocet
l_vysledek = l_gal * l_pocet

print(str(kg_pocet) + " kg je " + str(kg_vysledek) + " lb")
print(str(km_pocet) + " km je " + str(km_vysledek) + " mil")
print(str(l_pocet) + "  l je " + str(l_vysledek) + " gal")
#print(kg_pocet, 'kg je', kg_vysledek, 'lb')
#print(km_pocet, 'km je', km_vysledek, 'mil')
#print(l_pocet, 'l je', l_vysledek, 'gal')
'''

'''
#Auta a ceny
mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000

sleva_merc = 5000
cena_2_merc = mercedes * 2
cena_merc_a_rolls = mercedes + rolls_royce
cena_2_rolls_s_vybavou = rolls_royce * 2 + vybava * 2
cena_merc_s_vybavou = mercedes + vybava
merc_se_slevou = mercedes - sleva_merc

print("Sleva na Mercedes:", sleva_merc)
print("Cena za dva Mercedesy je:", cena_2_merc)
print("Cena za Mercedes a Rolls-Royce:", cena_merc_a_rolls)
print("Cena za dva Rolls-Royce s příplatkovou výbavou:", cena_2_rolls_s_vybavou)
print("Cena za Mercedes s příplatkovou výbavou:", cena_merc_s_vybavou)
print("Cena za Mercedes po slevě:", merc_se_slevou)
'''

#Hrátky se jménem
jmeno = "Lukáš"
prijmeni = "Dvořák"

cele_jmeno = jmeno + " " + prijmeni
delka_jmena = len(cele_jmeno)

print("Celé jméno:", cele_jmeno)
print("Délka jména:", delka_jmena)
print("=" * delka_jmena)
print(cele_jmeno)
print("=" * delka_jmena)

