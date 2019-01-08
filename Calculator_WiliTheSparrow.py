#   -----------------
# |   HAZI FELADAT   |
#   -----------------

from csv import DictWriter, DictReader
import xml.etree.ElementTree as ET
import json
import pickle
import shelve


class Szamolas:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def osszeadas_muvelete(a, b):
        osszeadas = a + b
        osszeadas_kijott_eredmenyek.append(osszeadas)
        osszead_elso_ertek.append(a)
        osszeadas_masodik_ertek.append(b)
        print(str(a), ' + ', str(b), ' = ', str(osszeadas))

    def kivonas_muvelete(a, b):
        kivonas = a - b
        kivonas_kijott_eredmenyek.append(kivonas)
        kivonas_elso_ertek.append(a)
        kivonas_masodik_ertek.append(b)
        print(str(a), ' - ', str(b), ' = ', str(kivonas))

    def osztas_muvelete(a, b):
        osztas = a / b
        osztas_kijott_eredmenyek.append(osztas)
        osztas_elso_ertek.append(a)
        osztas_masodik_ertek.append(b)
        print(str(a), ' / ', str(b), ' = ', str(osztas))

    def szorzas_muvelete(a, b):
        szorzas = a * b
        szorzas_kijott_eredmenyek.append(szorzas)
        szorzas_elso_ertek.append(a)
        szorzas_masodik_ertek.append(b)
        print(str(a), ' * ', str(b), ' = ', str(szorzas))


# <editor-fold desc="Kezdeti ertekek beallitasa a statisztikahoz">
statisztika_osszeadas = 0
osszeadas_kijott_eredmenyek = []
osszead_elso_ertek = []
osszeadas_masodik_ertek = []

statisztika_kivonas = 0
kivonas_kijott_eredmenyek = []
kivonas_elso_ertek = []
kivonas_masodik_ertek = []

statisztika_osztas = 0
osztas_kijott_eredmenyek = []
osztas_elso_ertek = []
osztas_masodik_ertek = []

statisztika_szorzas = 0
szorzas_kijott_eredmenyek = []
szorzas_elso_ertek = []
szorzas_masodik_ertek = []

paros_szamok = 0
paratlan_szamok = 0
tiznel_nagyobb_szamok = 0

# </editor-fold>

# <editor-fold desc="A szamologep">

# Elso kerdes arrol, hogy szeretne-e a felhasznalo szamolasi muveleteket vegezni:
kerdes = input("Szeretne szamolasokat vegezni (Igen/Nem)? ").lower()

while kerdes == 'igen':  # A ciklus addig fut le, amig igenekkel valaszol a felhasznalo.

    # Bekerjük a szamokat es a muveletet a felhasznalotol, amikkel szeretne dolgozni:
    muvelet_bekerese = input("Kerem adjon meg egy muveletet (+ / - / / / *): ")
    megadott_szamok = Szamolas(a=int(input("Kerem adja meg az elso erteket: ")), b=int(input("Kerem adja meg a masodik erteket: ")))

    if muvelet_bekerese == '+':
        osszeadogatok = Szamolas
        osszeadogatok.osszeadas_muvelete(megadott_szamok.a, megadott_szamok.b)
        statisztika_osszeadas += 1
        kerdes = input("Szeretne meg szamolasokat vegezni (Igen/Nem)? ").lower()

    elif muvelet_bekerese == '-':
        kivonogatok = Szamolas
        kivonogatok.kivonas_muvelete(megadott_szamok.a, megadott_szamok.b)
        statisztika_kivonas += 1
        kerdes = input("Szeretne meg szamolasokat vegezni (Igen/Nem)? ").lower()

    elif muvelet_bekerese == '/':
        osztogatok = Szamolas
        osztogatok.osztas_muvelete(megadott_szamok.a, megadott_szamok.b)
        statisztika_osztas += 1
        kerdes = input("Szeretne meg szamolasokat vegezni (Igen/Nem)? ").lower()

    elif muvelet_bekerese == '*':
        szorozgatok = Szamolas
        szorozgatok.szorzas_muvelete(megadott_szamok.a, megadott_szamok.b)
        statisztika_szorzas += 1
        kerdes = input("Szeretne meg szamolasokat vegezni (Igen/Nem)? ").lower()

kerdes2 = input("Szeretne a statisztikai adatokat megjeleniteni (Igen/Nem)? ").lower()

# </editor-fold>

# <editor-fold desc="Eredmenyek ertekelese">
eredmenyek_omlesztve = osszeadas_kijott_eredmenyek + kivonas_kijott_eredmenyek + osztas_kijott_eredmenyek + szorzas_kijott_eredmenyek

for i in eredmenyek_omlesztve:  # Mennyi paros vagy paratlan szam volt.
    if i % 2 == 0:
        paros_szamok += 1
    else:
        paratlan_szamok += 1

for i in eredmenyek_omlesztve:  # Mennyi 10-nel nagyobb szam jott ki.
    if i > 10:
        tiznel_nagyobb_szamok += 1
# </editor-fold>

# <editor-fold desc="Eredmenyek eltarolasa file-okba">
# <editor-fold desc="CSV">
with open('szamologep.csv', 'w', encoding='utf-8', newline='') as fajl:
    fejlec = [
        "Osszeadas muvelete osszesen",
        "Osszeadas eredmenye(i)",
        "Osszeadasnal megadott elso ertek(ek)",
        "Osszeadasnal megadott masodik ertek(ek)",
        "Kivonas muvelete osszesen",
        "Kivonas eredmenye(i)",
        "Kivonasnal megadott elso ertek(ek)",
        "Kivonasnal megadott masodik ertek(ek)",
        "Osztas muvelete osszesen",
        "Osztas eredmenye(i)",
        "Osztasnal megadott elso ertek(ek)",
        "Osztasnal megadott masodik ertek(ek)",
        "Szorzas muvelete osszesen",
        "Szorzas eredmenye(i)",
        "Szorzasnal megadott elso ertek(ek)",
        "Szorzasnal megadott masodik ertek(ek)",
        "Osszes paros szam",
        "Osszes paratlan szam",
        "Tiznel nagyobb szamok"
    ]
    csvWriter = DictWriter(fajl, fieldnames=fejlec)
    csvWriter.writeheader()
    csvWriter.writerow({
        "Osszeadas muvelete osszesen": statisztika_osszeadas,
        "Osszeadas eredmenye(i)": osszeadas_kijott_eredmenyek,
        "Osszeadasnal megadott elso ertek(ek)": osszead_elso_ertek,
        "Osszeadasnal megadott masodik ertek(ek)": osszeadas_masodik_ertek,
        "Kivonas muvelete osszesen": statisztika_kivonas,
        "Kivonas eredmenye(i)": kivonas_kijott_eredmenyek,
        "Kivonasnal megadott elso ertek(ek)": kivonas_elso_ertek,
        "Kivonasnal megadott masodik ertek(ek)": kivonas_masodik_ertek,
        "Osztas muvelete osszesen": statisztika_osztas,
        "Osztas eredmenye(i)": osztas_kijott_eredmenyek,
        "Osztasnal megadott elso ertek(ek)": osztas_elso_ertek,
        "Osztasnal megadott masodik ertek(ek)": osztas_masodik_ertek,
        "Szorzas muvelete osszesen": statisztika_szorzas,
        "Szorzas eredmenye(i)": szorzas_kijott_eredmenyek,
        "Szorzasnal megadott elso ertek(ek)": szorzas_elso_ertek,
        "Szorzasnal megadott masodik ertek(ek)": szorzas_masodik_ertek,
        "Osszes paros szam": paros_szamok,
        "Osszes paratlan szam": paratlan_szamok,
        "Tiznel nagyobb szamok": tiznel_nagyobb_szamok
    })

# </editor-fold>

# <editor-fold desc="XML">
szamologepAdatok = ET.Element('szamolasi_statisztika')

osszeadasElem = ET.SubElement(szamologepAdatok, 'osszeadas_statisztika')
elem1 = ET.SubElement(osszeadasElem, 'Adat1')
elem1.set('osszesen_elvegzett_osszeadas', 'elem1')
elem1.text = str(statisztika_osszeadas)
elem2 = ET.SubElement(osszeadasElem, 'Adat2')
elem2.set('osszeadas_kijott_eredmenyek', 'elem2')
elem2.text = str(osszeadas_kijott_eredmenyek)
elem3 = ET.SubElement(osszeadasElem, 'Adat3')
elem3.set('osszeadas_elso_ertekek', 'elem3')
elem3.text = str(osszead_elso_ertek)
elem4 = ET.SubElement(osszeadasElem, 'Adat4')
elem4.set('osszeadas_masodik_ertekek', 'elem4')
elem4.text = str(osszeadas_masodik_ertek)

kivonasElem = ET.SubElement(szamologepAdatok, 'kivonas_statisztika')
elem5 = ET.SubElement(kivonasElem, 'Adat5')
elem5.set('osszesen_elvegzett_kivonas', 'elem5')
elem5.text = str(statisztika_kivonas)
elem6 = ET.SubElement(kivonasElem, 'Adat6')
elem6.set('kivonas_kijott_eredmenyek', 'elem6')
elem6.text = str(kivonas_kijott_eredmenyek)
elem7 = ET.SubElement(kivonasElem, 'Adat7')
elem7.set('kivonas_elso_ertekek', 'elem7')
elem7.text = str(kivonas_elso_ertek)
elem8 = ET.SubElement(kivonasElem, 'Adat8')
elem8.set('kivonas_masodik_ertekek', 'elem8')
elem8.text = str(kivonas_masodik_ertek)

osztasElem = ET.SubElement(szamologepAdatok, 'osztas_statisztika')
elem9 = ET.SubElement(osztasElem, 'Adat9')
elem9.set('osszesen_elvegzett_osztas', 'elem9')
elem9.text = str(statisztika_osztas)
elem10 = ET.SubElement(osztasElem, 'Adat10')
elem10.set('osztas_kijott_eredmenyek', 'elem10')
elem10.text = str(osztas_kijott_eredmenyek)
elem11 = ET.SubElement(osztasElem, 'Adat11')
elem11.set('osztas_elso_ertekek', 'elem11')
elem11.text = str(osztas_elso_ertek)
elem12 = ET.SubElement(osztasElem, 'Adat12')
elem12.set('oszztas_masodik_ertekek', 'elem12')
elem12.text = str(osztas_masodik_ertek)

szorzasElem = ET.SubElement(szamologepAdatok, 'szorzas_statisztika')
elem13 = ET.SubElement(szorzasElem, 'Adat13')
elem13.set('osszesen_elvegzett_szorzas', 'elem13')
elem13.text = str(statisztika_szorzas)
elem14 = ET.SubElement(szorzasElem, 'Adat14')
elem14.set('szorzas_kijott_eredmenyek', 'elem14')
elem14.text = str(szorzas_kijott_eredmenyek)
elem15 = ET.SubElement(szorzasElem, 'Adat15')
elem15.set('szorzas_elso_ertekek', 'elem15')
elem15.text = str(szorzas_elso_ertek)
elem16 = ET.SubElement(szorzasElem, 'Adat16')
elem16.set('szorzas_masodik_ertekek', 'elem16')
elem16.text = str(szorzas_masodik_ertek)

egyebElem = ET.SubElement(szamologepAdatok, 'egyeb_statisztika')
elem17 = ET.SubElement(egyebElem, 'Adat17')
elem17.set('paros_szamok', 'elem17')
elem17.text = str(paros_szamok)
elem18 = ET.SubElement(egyebElem, 'Adat18')
elem18.set('paratlan_szamok', 'elem18')
elem18.text = str(paratlan_szamok)
elem19 = ET.SubElement(egyebElem, 'Adat19')
elem19.set('tiznelnagyobbak', 'elem19')
elem19.text = str(tiznel_nagyobb_szamok)

# Az összekészített struktúrát xml fájlba tesszük
adataink = ET.tostring(szamologepAdatok, encoding="unicode")
fajl = open("szamologep.xml", "w", encoding="utf-8")
fajl.write(adataink)
fajl.close()

# </editor-fold>

# <editor-fold desc="JSON">
szamologep = {}
szamologep['szamologepStatisztika'] = []
szamologep['szamologepStatisztika'].append({
    'osszes': "Osszeadas muvelete osszesen: " + str(statisztika_osszeadas),
    'eredmeny': "Osszeadas eredmenye(i): " + str(osszeadas_kijott_eredmenyek),
    'elsoertek': "Osszeadasnal megadott elso ertek(ek): " + str(osszead_elso_ertek),
    'masodikertek': "Osszeadasnal megadott masodik ertek(ek): " + str(osszeadas_masodik_ertek),
    'osszes1': "Kivonas muvelete osszesen: " + str(statisztika_kivonas),
    'eredmeny1': "Kivonas eredmenye(i): " + str(kivonas_kijott_eredmenyek),
    'elsoertek1': "Kivonasnal megadott elso ertek(ek): " + str(kivonas_elso_ertek),
    'masodikertek1': "Kivonasnal megadott masodik ertek(ek)" + str(kivonas_masodik_ertek),
    'osszes2': "Osztas muvelete osszesen: " + str(statisztika_osztas),
    'eredmeny2': "Osztas eredmenye(i): " + str(osztas_kijott_eredmenyek),
    'elsoertek2': "Osztasnal megadott elso ertek(ek): " + str(osztas_elso_ertek),
    'masodikertek2': "Osztasnal megadott masodik ertek(ek): " + str(osztas_masodik_ertek),
    'osszes3': "Szorzas muvelete osszesen: " + str(statisztika_szorzas),
    'eredmeny3': "Szorzas eredmenye(i): " + str(szorzas_kijott_eredmenyek),
    'elsoertek3': "Szorzasnal megadott elso ertek(ek): " + str(szorzas_elso_ertek),
    'masodikertek3': "Szorzasnal megadott masodik ertek(ek): " + str(szorzas_masodik_ertek),
    'paros': "Osszes paros szam: " + str(paros_szamok),
    'paratlan': "Osszes paratlan szam: " + str(paratlan_szamok),
    'tiznelnagyobb': "Tiznel nagyobb szamok: " + str(tiznel_nagyobb_szamok)
})

with open("szamologep.json", "w", encoding="utf-8") as fajl:
    json.dump(szamologep, fajl)

# </editor-fold>

# <editor-fold desc="PICKLE">
fajl = open('szamologep.pickle', 'wb')
###
pickle.dump(statisztika_osszeadas, fajl)
pickle.dump(osszeadas_kijott_eredmenyek, fajl)
pickle.dump(osszead_elso_ertek, fajl)
pickle.dump(osszeadas_masodik_ertek, fajl)
###
pickle.dump(statisztika_kivonas, fajl)
pickle.dump(kivonas_kijott_eredmenyek, fajl)
pickle.dump(kivonas_elso_ertek, fajl)
pickle.dump(kivonas_masodik_ertek, fajl)
###
pickle.dump(statisztika_osztas, fajl)
pickle.dump(osztas_kijott_eredmenyek, fajl)
pickle.dump(osztas_elso_ertek, fajl)
pickle.dump(osztas_masodik_ertek, fajl)
###
pickle.dump(statisztika_szorzas, fajl)
pickle.dump(szorzas_kijott_eredmenyek, fajl)
pickle.dump(szorzas_elso_ertek, fajl)
pickle.dump(szorzas_masodik_ertek, fajl)
###
pickle.dump(paros_szamok, fajl)
pickle.dump(paratlan_szamok, fajl)
pickle.dump(tiznel_nagyobb_szamok, fajl)
###
fajl.close()

olvas = open("szamologep.pickle", "rb")
###
osszead01 = pickle.load(olvas)
osszead02 = pickle.load(olvas)
osszead03 = pickle.load(olvas)
osszead04 = pickle.load(olvas)
###
kivon01 = pickle.load(olvas)
kivon02 = pickle.load(olvas)
kivon03 = pickle.load(olvas)
kivon04 = pickle.load(olvas)
###
osztas01 = pickle.load(olvas)
osztas02 = pickle.load(olvas)
osztas03 = pickle.load(olvas)
osztas04 = pickle.load(olvas)
###
szorzas01 = pickle.load(olvas)
szorzas02 = pickle.load(olvas)
szorzas03 = pickle.load(olvas)
szorzas04 = pickle.load(olvas)
###
paros00 = pickle.load(olvas)
paratlan00 = pickle.load(olvas)
tiznelnagyobbszamok00 = pickle.load(olvas)
###
olvas.close()

# </editor-fold>

# <editor-fold desc="SHELVE">
s = shelve.open("szamologep.dat")
s["osszeadas_ertekek"] = [
    statisztika_osszeadas,
    osszeadas_kijott_eredmenyek,
    osszead_elso_ertek,
    osszeadas_masodik_ertek
]
s["kivonas_ertekek"] = [
    statisztika_kivonas,
    kivonas_kijott_eredmenyek,
    kivonas_elso_ertek,
    kivonas_masodik_ertek
]
s["osztas_ertekek"] = [
    statisztika_osztas,
    osztas_kijott_eredmenyek,
    osztas_elso_ertek,
    osztas_masodik_ertek
]
s["szorzas_ertekek"] = [
    statisztika_szorzas,
    szorzas_kijott_eredmenyek,
    szorzas_elso_ertek,
    szorzas_masodik_ertek
]
s["egyeb_ertekek"] = [
    paros_szamok,
    paratlan_szamok,
    tiznel_nagyobb_szamok
]
s.close()

# </editor-fold>
# </editor-fold>

# <editor-fold desc="Eredmenyek kiiratasa a file-okbol">
if kerdes2 == 'igen':

    # <editor-fold desc="CSV kiir">
    print("-" * 50)
    print("CSV file-ból kiiratva a statisztika")
    print("-" * 50)
    with open("szamologep.csv", encoding='utf-8', newline='') as fajl:
        csvOlvas = DictReader(fajl)
        for sor in csvOlvas:
            print(sor)
    # </editor-fold>

    # <editor-fold desc="XML kiir">
    fa = ET.parse('szamologep.xml')
    gyoker = fa.getroot()
    print("-" * 50)
    print("XML file-ból kiiratva a statisztika")
    print("-" * 50)

    print("Osszeadas muvelete osszesen:")
    print(gyoker[0][0].text)
    print("Osszeadas eredmenye(i):")
    print(gyoker[0][1].text)
    print("Osszeadasnal megadott elso ertek(ek):")
    print(gyoker[0][2].text)
    print("Osszeadasnal megadott masodik ertek(ek):")
    print(gyoker[0][3].text)

    print("Kivonas muvelete osszesen:")
    print(gyoker[1][0].text)
    print("Kivonas eredmenye(i):")
    print(gyoker[1][1].text)
    print("Kivonasnal megadott elso ertek(ek):")
    print(gyoker[1][2].text)
    print("Kivonasnal megadott masodik ertek(ek):")
    print(gyoker[1][3].text)

    print("Osztas muvelete osszesen:")
    print(gyoker[2][0].text)
    print("Osztas eredmenye(i):")
    print(gyoker[2][1].text)
    print("Osztasnal megadott elso ertek(ek):")
    print(gyoker[2][2].text)
    print("Osztasnal megadott masodik ertek(ek):")
    print(gyoker[2][3].text)

    print("Szorzas muvelete osszesen:")
    print(gyoker[3][0].text)
    print("Szorzas eredmenye(i):")
    print(gyoker[3][1].text)
    print("Szorzasnal megadott elso ertek(ek):")
    print(gyoker[3][2].text)
    print("Szorzasnal megadott masodik ertek(ek):")
    print(gyoker[3][3].text)

    print("Osszes paros szam:")
    print(gyoker[4][0].text)
    print("Osszes paratlan szam:")
    print(gyoker[4][1].text)
    print("Tiznel nagyobb szamok:")
    print(gyoker[4][2].text)
    # </editor-fold>

    # <editor-fold desc="JSON">
    print("-" * 50)
    print("JSON file-ból kiiratva a statisztika")
    print("-" * 50)

    with open("szamologep.json", "r", encoding="utf-8") as olvas:
        szamologep = json.load(olvas)
        for t in szamologep['szamologepStatisztika']:
            print(t['osszes'])
            print(t['eredmeny'])
            print(t['elsoertek'])
            print(t['masodikertek'])
            print("*" * 30)
            print(t['osszes1'])
            print(t['eredmeny1'])
            print(t['elsoertek1'])
            print(t['masodikertek1'])
            print("*" * 30)
            print(t['osszes2'])
            print(t['eredmeny2'])
            print(t['elsoertek2'])
            print(t['masodikertek2'])
            print("*" * 30)
            print(t['osszes3'])
            print(t['eredmeny3'])
            print(t['elsoertek3'])
            print(t['masodikertek3'])
            print("*" * 30)
            print(t['paros'])
            print(t['paratlan'])
            print(t['tiznelnagyobb'])
    # </editor-fold>

    # <editor-fold desc="PICKLE">
    print("-" * 50)
    print("PICKLE file-ból kiiratva a statisztika")
    print("-" * 50)

    print("Osszeadas muvelete osszesen: ", osszead01)
    print("Osszeadas eredmenye(i): ", osszead02)
    print("Osszeadasnal megadott elso ertek(ek): ", osszead03)
    print("Osszeadasnal megadott masodik ertek(ek): ", osszead04)
    ###
    print("Kivonas muvelete osszesen: ", kivon01)
    print("Kivonas eredmenye(i): ", kivon02)
    print("Kivonasnal megadott elso ertek(ek): ", kivon03)
    print("Kivonasnal megadott masodik ertek(ek): ", kivon04)
    ###
    print("Osztas muvelete osszesen: ", osztas01)
    print("Osztas eredmenye(i): ", osztas02)
    print("Osztasnal megadott elso ertek(ek): ", osztas03)
    print("Osztasnal megadott masodik ertek(ek): ", osztas04)
    ###
    print("Szorzas muvelete osszesen: ", szorzas01)
    print("Szorzas eredmenye(i): ", szorzas02)
    print("Szorzasnal megadott elso ertek(ek): ", szorzas03)
    print("Szorzasnal megadott masodik ertek(ek): ", szorzas04)
    ###
    print("Osszes paros szam: ", paros00)
    print("Osszes paratlan szam: ", paratlan00)
    print("Tiznel nagyobb szamok: ", tiznelnagyobbszamok00)
    # </editor-fold>

    # <editor-fold desc="SHELVE">
    print("-" * 50)
    print("SHELVE file-ból kiiratva a statisztika")
    print("-" * 50)

    o = shelve.open("szamologep.dat")
    ###
    print("Osszeadas muvelet(ei): " + str(o["osszeadas_ertekek"][0]) + "db")
    print("Osszeadas kijott eredmeny(ek): " + str(o["osszeadas_ertekek"][1]))
    print("Osszeadas elso ertek(ek): " + str(o["osszeadas_ertekek"][2]))
    print("Osszeadas masodik ertek(ek): " + str(o["osszeadas_ertekek"][3]))
    ###
    print("Kivonas muvelet(ei): " + str(o["kivonas_ertekek"][0]) + "db")
    print("Kivonas kijott eredmeny(ek): " + str(o["kivonas_ertekek"][1]))
    print("Kivonas elso ertek(ek): " + str(o["kivonas_ertekek"][2]))
    print("Kivonas masodik ertek(ek): " + str(o["kivonas_ertekek"][3]))
    ###
    print("Osztas muvelet(ei): " + str(o["osztas_ertekek"][0]) + "db")
    print("Osztas kijott eredmeny(ek): " + str(o["osztas_ertekek"][1]))
    print("Osztas elso ertek(ek): " + str(o["osztas_ertekek"][2]))
    print("Osztas masodik ertek(ek): " + str(o["osztas_ertekek"][3]))
    ###
    print("Szorzas muvelet(ei): " + str(o["szorzas_ertekek"][0]) + "db")
    print("Szorzas kijott eredmeny(ek): " + str(o["szorzas_ertekek"][1]) + "db")
    print("Szorzas elso ertek(ek): " + str(o["szorzas_ertekek"][2]))
    print("Szorzas masodik ertek(ek): " + str(o["szorzas_ertekek"][3]))
    ###
    print("Paros szam(ok): " + str(o["egyeb_ertekek"][0]) + "db")
    print("Paratlan szam(ok): " + str(o["egyeb_ertekek"][1]) + "db")
    print("Tiznel nagyobb szam(ok): " + str(o["egyeb_ertekek"][2]) + "db")
    ###
    o.close()
    # </editor-fold>

else:
    print("Akkor viszlat!")

input('')
# </editor-fold>
