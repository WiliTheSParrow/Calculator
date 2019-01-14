#   -----------------
# |   HAZI FELADAT   |
#   -----------------

# Szamologep reszeinek osztalyba sorolasa

from csv import DictWriter, DictReader
import xml.etree.ElementTree as ET
import json
import pickle
import shelve


class Szamolas:
    """A Számolás szülőosztály tartalmazza a statisztikához tartozó kezdeti változók értékeinek beállítását valamint a
    számoláshoz műveleteinek elvégzéséhez szükséges metódusokat."""
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

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def osszeadas_muvelete(self, osszeadas_kijott_eredmenyek, osszead_elso_ertek, osszeadas_masodik_ertek):
        osszeadas = self.a + self.b
        osszeadas_kijott_eredmenyek.append(osszeadas)
        osszead_elso_ertek.append(self.a)
        osszeadas_masodik_ertek.append(self.b)

        print(str(self.a), ' + ', str(self.b), ' = ', str(osszeadas))

    def kivonas_muvelete(self, kivonas_kijott_eredmenyek, kivonas_elso_ertek, kivonas_masodik_ertek):
        kivonas = self.a - self.b
        kivonas_kijott_eredmenyek.append(kivonas)
        kivonas_elso_ertek.append(self.a)
        kivonas_masodik_ertek.append(self.b)

        print(str(self.a), ' - ', str(self.b), ' = ', str(kivonas))

    def osztas_muvelete(self, osztas_kijott_eredmenyek, osztas_elso_ertek, osztas_masodik_ertek):
        osztas = self.a / self.b
        osztas_kijott_eredmenyek.append(osztas)
        osztas_elso_ertek.append(self.a)
        osztas_masodik_ertek.append(self.b)

        print(str(self.a), ' / ', str(self.b), ' = ', str(osztas))

    def szorzas_muvelete(self, szorzas_kijott_eredmenyek, szorzas_elso_ertek, szorzas_masodik_ertek):
        szorzas = self.a * self.b
        szorzas_kijott_eredmenyek.append(szorzas)
        szorzas_elso_ertek.append(self.a)
        szorzas_masodik_ertek.append(self.b)

        print(str(self.a), ' * ', str(self.b), ' = ', str(szorzas))


class Statisztika(Szamolas):
    """A Statisztika gyermekosztály a Számolás szülőosztályból örökli a tulajdonságokat.
    Tartalmazza a páros/páratlan és a tíznél nagyobb számok meghatározásához szükséges metódusokat."""

    def __init__(self):
        super().__init__()

    def tiznelnagyobbak(eredmenyek_omlesztve):
        for i in eredmenyek_omlesztve:  # Mennyi 10-nel nagyobb szam jott ki.
            if i > 10:
                Szamolas.tiznel_nagyobb_szamok += 1

    def parosok(eredmenyek_omlesztve):
        for i in eredmenyek_omlesztve:  # Mennyi paros vagy paratlan szam volt.
            if i % 2 == 0:
                Szamolas.paros_szamok += 1

    def paratlanok(eredmenyek_omlesztve):
        for i in eredmenyek_omlesztve:  # Mennyi paros vagy paratlan szam volt.
            if i % 2 != 0:
                Szamolas.paratlan_szamok += 1


class Mentesek:
    """A Mentések osztály felel a számológép során megadott értékek file-okba történő írásáért.
    Tartalmazza a file-ba írás metódusait és a file-okból történő statisztika kiírásért felelős metódusokat.
    File formátumok:
    -	CSV
    -	XML
    -	JSON
    -	PICKLE
    -	SHELVE
    """

    def __init__(self, sum_osszeadas, osszead_eredm, osszead_elso, osszead_masodik, sum_kivonas, kivonas_eredm,
                 kivonas_elso, kivonas_masodik, sum_osztas, osztas_eredm, osztas_elso, osztas_masodik, sum_szorzas,
                 szorzas_eredm, szorzas_elso, szorzas_masodik, paros_sz, paratlan_sz, tiznel_nagyobb_sz):
        self.sum_osszeadas = sum_osszeadas
        self.osszead_eredm = osszead_eredm
        self.osszead_elso = osszead_elso
        self.osszead_masodik = osszead_masodik
        self.sum_kivonas = sum_kivonas
        self.kivonas_eredm = kivonas_eredm
        self.kivonas_elso = kivonas_elso
        self.kivonas_masodik = kivonas_masodik
        self.sum_osztas = sum_osztas
        self.osztas_eredm = osztas_eredm
        self.osztas_elso = osztas_elso
        self.osztas_masodik = osztas_masodik
        self.sum_szorzas = sum_szorzas
        self.szorzas_eredm = szorzas_eredm
        self.szorzas_elso = szorzas_elso
        self.szorzas_masodik = szorzas_masodik
        self.paros_sz = paros_sz
        self.paratlan_sz = paratlan_sz
        self.tiznel_nagyobb_sz = tiznel_nagyobb_sz

    def csv_mentes(self, sum_osszeadas, osszead_eredm, osszead_elso, osszead_masodik, sum_kivonas, kivonas_eredm,
                   kivonas_elso, kivonas_masodik, sum_osztas, osztas_eredm, osztas_elso, osztas_masodik, sum_szorzas,
                   szorzas_eredm, szorzas_elso, szorzas_masodik, paros_sz, paratlan_sz, tiznel_nagyobb_sz):
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
            csvWriter.writerow({"Osszeadas muvelete osszesen": sum_osszeadas,
                                "Osszeadas eredmenye(i)": osszead_eredm,
                                "Osszeadasnal megadott elso ertek(ek)": osszead_elso,
                                "Osszeadasnal megadott masodik ertek(ek)": osszead_masodik,
                                "Kivonas muvelete osszesen": sum_kivonas,
                                "Kivonas eredmenye(i)": kivonas_eredm,
                                "Kivonasnal megadott elso ertek(ek)": kivonas_elso,
                                "Kivonasnal megadott masodik ertek(ek)": kivonas_masodik,
                                "Osztas muvelete osszesen": sum_osztas,
                                "Osztas eredmenye(i)": osztas_eredm,
                                "Osztasnal megadott elso ertek(ek)": osztas_elso,
                                "Osztasnal megadott masodik ertek(ek)": osztas_masodik,
                                "Szorzas muvelete osszesen": sum_szorzas,
                                "Szorzas eredmenye(i)": szorzas_eredm,
                                "Szorzasnal megadott elso ertek(ek)": szorzas_elso,
                                "Szorzasnal megadott masodik ertek(ek)": szorzas_masodik,
                                "Osszes paros szam": paros_sz,
                                "Osszes paratlan szam": paratlan_sz,
                                "Tiznel nagyobb szamok": tiznel_nagyobb_sz})

    def xml_mentes(self, sum_osszeadas, osszead_eredm, osszead_elso, osszead_masodik, sum_kivonas, kivonas_eredm,
                   kivonas_elso, kivonas_masodik, sum_osztas, osztas_eredm, osztas_elso, osztas_masodik, sum_szorzas,
                   szorzas_eredm, szorzas_elso, szorzas_masodik, paros_sz, paratlan_sz, tiznel_nagyobb_sz):
        szamologepAdatok = ET.Element('szamolasi_statisztika')

        osszeadasElem = ET.SubElement(szamologepAdatok, 'osszeadas_statisztika')
        elem1 = ET.SubElement(osszeadasElem, 'Adat1')
        elem1.set('sum_osszeadas', 'elem1')
        elem1.text = str(stat_szamok.statisztika_osszeadas)
        elem2 = ET.SubElement(osszeadasElem, 'Adat2')
        elem2.set('osszead_eredm', 'elem2')
        elem2.text = str(stat_szamok.osszeadas_kijott_eredmenyek)
        elem3 = ET.SubElement(osszeadasElem, 'Adat3')
        elem3.set('osszead_elso', 'elem3')
        elem3.text = str(stat_szamok.osszead_elso_ertek)
        elem4 = ET.SubElement(osszeadasElem, 'Adat4')
        elem4.set('osszead_masodik', 'elem4')
        elem4.text = str(stat_szamok.osszeadas_masodik_ertek)

        kivonasElem = ET.SubElement(szamologepAdatok, 'kivonas_statisztika')
        elem5 = ET.SubElement(kivonasElem, 'Adat5')
        elem5.set('sum_kivonas', 'elem5')
        elem5.text = str(stat_szamok.statisztika_kivonas)
        elem6 = ET.SubElement(kivonasElem, 'Adat6')
        elem6.set('kivonas_eredm', 'elem6')
        elem6.text = str(stat_szamok.kivonas_kijott_eredmenyek)
        elem7 = ET.SubElement(kivonasElem, 'Adat7')
        elem7.set('kivonas_elso', 'elem7')
        elem7.text = str(stat_szamok.kivonas_elso_ertek)
        elem8 = ET.SubElement(kivonasElem, 'Adat8')
        elem8.set('kivonas_masodik', 'elem8')
        elem8.text = str(stat_szamok.kivonas_masodik_ertek)

        osztasElem = ET.SubElement(szamologepAdatok, 'osztas_statisztika')
        elem9 = ET.SubElement(osztasElem, 'Adat9')
        elem9.set('sum_osztas', 'elem9')
        elem9.text = str(stat_szamok.statisztika_osztas)
        elem10 = ET.SubElement(osztasElem, 'Adat10')
        elem10.set('osztas_eredm', 'elem10')
        elem10.text = str(stat_szamok.osztas_kijott_eredmenyek)
        elem11 = ET.SubElement(osztasElem, 'Adat11')
        elem11.set('osztas_elso', 'elem11')
        elem11.text = str(stat_szamok.osztas_elso_ertek)
        elem12 = ET.SubElement(osztasElem, 'Adat12')
        elem12.set('osztas_masodik', 'elem12')
        elem12.text = str(stat_szamok.osztas_masodik_ertek)

        szorzasElem = ET.SubElement(szamologepAdatok, 'szorzas_statisztika')
        elem13 = ET.SubElement(szorzasElem, 'Adat13')
        elem13.set('sum_szorzas', 'elem13')
        elem13.text = str(stat_szamok.statisztika_szorzas)
        elem14 = ET.SubElement(szorzasElem, 'Adat14')
        elem14.set('szorzas_eredm', 'elem14')
        elem14.text = str(stat_szamok.szorzas_kijott_eredmenyek)
        elem15 = ET.SubElement(szorzasElem, 'Adat15')
        elem15.set('szorzas_elso', 'elem15')
        elem15.text = str(stat_szamok.szorzas_elso_ertek)
        elem16 = ET.SubElement(szorzasElem, 'Adat16')
        elem16.set('szorzas_masodik', 'elem16')
        elem16.text = str(stat_szamok.szorzas_masodik_ertek)

        egyebElem = ET.SubElement(szamologepAdatok, 'egyeb_statisztika')
        elem17 = ET.SubElement(egyebElem, 'Adat17')
        elem17.set('paros_sz', 'elem17')
        elem17.text = str(stat_szamok.paros_szamok)
        elem18 = ET.SubElement(egyebElem, 'Adat18')
        elem18.set('paratlan_sz', 'elem18')
        elem18.text = str(stat_szamok.paratlan_szamok)
        elem19 = ET.SubElement(egyebElem, 'Adat19')
        elem19.set('tiznel_nagyobb_sz', 'elem19')
        elem19.text = str(stat_szamok.tiznel_nagyobb_szamok)

        # Az összekészített struktúrát xml fájlba tesszük
        adataink = ET.tostring(szamologepAdatok, encoding="unicode")
        fajl = open("szamologep.xml", "w", encoding="utf-8")
        fajl.write(adataink)
        fajl.close()

    def json_mentesek(self, sum_osszeadas, osszead_eredm, osszead_elso, osszead_masodik, sum_kivonas, kivonas_eredm,
                      kivonas_elso, kivonas_masodik, sum_osztas, osztas_eredm, osztas_elso, osztas_masodik, sum_szorzas,
                      szorzas_eredm, szorzas_elso, szorzas_masodik, paros_sz, paratlan_sz, tiznel_nagyobb_sz):
        szamologep = {}
        szamologep['szamologepStatisztika'] = []
        szamologep['szamologepStatisztika'].append({
            'osszes': "Osszeadas muvelete osszesen: " + str(sum_osszeadas),
            'eredmeny': "Osszeadas eredmenye(i): " + str(osszead_eredm),
            'elsoertek': "Osszeadasnal megadott elso ertek(ek): " + str(osszead_elso),
            'masodikertek': "Osszeadasnal megadott masodik ertek(ek): " + str(osszead_masodik),
            'osszes1': "Kivonas muvelete osszesen: " + str(sum_kivonas),
            'eredmeny1': "Kivonas eredmenye(i): " + str(kivonas_eredm),
            'elsoertek1': "Kivonasnal megadott elso ertek(ek): " + str(kivonas_elso),
            'masodikertek1': "Kivonasnal megadott masodik ertek(ek)" + str(kivonas_masodik),
            'osszes2': "Osztas muvelete osszesen: " + str(sum_osztas),
            'eredmeny2': "Osztas eredmenye(i): " + str(osztas_eredm),
            'elsoertek2': "Osztasnal megadott elso ertek(ek): " + str(osztas_elso),
            'masodikertek2': "Osztasnal megadott masodik ertek(ek): " + str(osztas_masodik),
            'osszes3': "Szorzas muvelete osszesen: " + str(sum_szorzas),
            'eredmeny3': "Szorzas eredmenye(i): " + str(szorzas_eredm),
            'elsoertek3': "Szorzasnal megadott elso ertek(ek): " + str(szorzas_elso),
            'masodikertek3': "Szorzasnal megadott masodik ertek(ek): " + str(szorzas_masodik),
            'paros': "Osszes paros szam: " + str(paros_sz),
            'paratlan': "Osszes paratlan szam: " + str(paratlan_sz),
            'tiznelnagyobb': "Tiznel nagyobb szamok: " + str(tiznel_nagyobb_sz)
        })

        with open("szamologep.json", "w", encoding="utf-8") as fajl:
            json.dump(szamologep, fajl)

    def pickle_mentesek(self, sum_osszeadas, osszead_eredm, osszead_elso, osszead_masodik, sum_kivonas, kivonas_eredm,
                        kivonas_elso, kivonas_masodik, sum_osztas, osztas_eredm, osztas_elso, osztas_masodik,
                        sum_szorzas,
                        szorzas_eredm, szorzas_elso, szorzas_masodik, paros_sz, paratlan_sz, tiznel_nagyobb_sz):
        fajl = open('szamologep.pickle', 'wb')
        ###
        pickle.dump(sum_osszeadas, fajl)
        pickle.dump(osszead_eredm, fajl)
        pickle.dump(osszead_elso, fajl)
        pickle.dump(osszead_masodik, fajl)
        ###
        pickle.dump(sum_kivonas, fajl)
        pickle.dump(kivonas_eredm, fajl)
        pickle.dump(kivonas_elso, fajl)
        pickle.dump(kivonas_masodik, fajl)
        ###
        pickle.dump(sum_osztas, fajl)
        pickle.dump(osztas_eredm, fajl)
        pickle.dump(osztas_elso, fajl)
        pickle.dump(osztas_masodik, fajl)
        ###
        pickle.dump(sum_szorzas, fajl)
        pickle.dump(szorzas_eredm, fajl)
        pickle.dump(szorzas_elso, fajl)
        pickle.dump(szorzas_masodik, fajl)
        ###
        pickle.dump(paros_sz, fajl)
        pickle.dump(paratlan_sz, fajl)
        pickle.dump(tiznel_nagyobb_sz, fajl)
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

    def shelve_mentesek(self, sum_osszeadas, osszead_eredm, osszead_elso, osszead_masodik, sum_kivonas, kivonas_eredm,
                        kivonas_elso, kivonas_masodik, sum_osztas, osztas_eredm, osztas_elso, osztas_masodik,
                        sum_szorzas,
                        szorzas_eredm, szorzas_elso, szorzas_masodik, paros_sz, paratlan_sz, tiznel_nagyobb_sz):
        s = shelve.open("szamologep.dat")
        s["osszeadas_ertekek"] = [
            sum_osszeadas,
            osszead_eredm,
            osszead_elso,
            osszead_masodik
        ]
        s["kivonas_ertekek"] = [
            sum_kivonas,
            kivonas_eredm,
            kivonas_elso,
            kivonas_masodik
        ]
        s["osztas_ertekek"] = [
            sum_osztas,
            osztas_eredm,
            osztas_elso,
            osztas_masodik
        ]
        s["szorzas_ertekek"] = [
            sum_szorzas,
            szorzas_eredm,
            szorzas_elso,
            szorzas_masodik
        ]
        s["egyeb_ertekek"] = [
            paros_sz,
            paratlan_sz,
            tiznel_nagyobb_sz
        ]
        s.close()

    def csv_kiiratas(self):
        print("-" * 50)
        print("CSV file-ból kiiratva a statisztika")
        print("-" * 50)
        with open("szamologep.csv", encoding='utf-8', newline='') as fajl:
            csvOlvas = DictReader(fajl)
            for sor in csvOlvas:
                print(sor)

    def xml_kiiratas(self):
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

    def json_kiiratas(self):
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

    def pickle_kiiratas(self, osszead01, osszead02, osszead03, osszead04, kivon01, kivon02, kivon03, kivon04, osztas01,
                        osztas02, osztas03, osztas04, szorzas01, szorzas02, szorzas03, szorzas04, paros00, paratlan00,
                        tiznelnagyobbszamok00):
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

    def shelve_kiiratas(self):
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
        print("Szorzas kijott eredmeny(ek): " + str(o["szorzas_ertekek"][1]))
        print("Szorzas elso ertek(ek): " + str(o["szorzas_ertekek"][2]))
        print("Szorzas masodik ertek(ek): " + str(o["szorzas_ertekek"][3]))
        ###
        print("Paros szam(ok): " + str(o["egyeb_ertekek"][0]) + "db")
        print("Paratlan szam(ok): " + str(o["egyeb_ertekek"][1]) + "db")
        print("Tiznel nagyobb szam(ok): " + str(o["egyeb_ertekek"][2]) + "db")
        ###
        o.close()


# <editor-fold desc="A szamologep">

# Elso kerdes arrol, hogy szeretne-e a felhasznalo szamolasi muveleteket vegezni:
kerdes = input("Szeretne szamolasokat vegezni (Igen/Nem)? ").lower()

while kerdes == 'igen':  # A ciklus addig fut le, amig igenekkel valaszol a felhasznalo.

    # Bekerjük a szamokat es a muveletet a felhasznalotol, amikkel szeretne dolgozni:
    muvelet_bekerese = input("Kerem adjon meg egy muveletet (+ / - / / / *): ")
    megadott_szamok = Szamolas(a=int(input("Kerem adja meg az elso erteket: ")),
                               b=int(input("Kerem adja meg a masodik erteket: ")))

    if muvelet_bekerese == '+':
        osszeadogatok = Szamolas
        osszeadogatok.osszeadas_muvelete(megadott_szamok,
                                         megadott_szamok.osszeadas_kijott_eredmenyek,
                                         megadott_szamok.osszead_elso_ertek, megadott_szamok.osszeadas_masodik_ertek,
                                         )
        osszeadogatok.statisztika_osszeadas += 1

        kerdes = input("Szeretne meg szamolasokat vegezni (Igen/Nem)? ").lower()

    elif muvelet_bekerese == '-':
        kivonogatok = Szamolas
        kivonogatok.kivonas_muvelete(megadott_szamok, megadott_szamok.kivonas_kijott_eredmenyek,
                                     megadott_szamok.kivonas_elso_ertek, megadott_szamok.kivonas_masodik_ertek,
                                     )
        kivonogatok.statisztika_kivonas += 1
        kerdes = input("Szeretne meg szamolasokat vegezni (Igen/Nem)? ").lower()

    elif muvelet_bekerese == '/':
        osztogatok = Szamolas
        osztogatok.osztas_muvelete(megadott_szamok, megadott_szamok.osztas_kijott_eredmenyek,
                                   megadott_szamok.osztas_elso_ertek, megadott_szamok.osztas_masodik_ertek,
                                   )
        osztogatok.statisztika_osztas += 1
        kerdes = input("Szeretne meg szamolasokat vegezni (Igen/Nem)? ").lower()

    elif muvelet_bekerese == '*':
        szorozgatok = Szamolas
        szorozgatok.szorzas_muvelete(megadott_szamok, megadott_szamok.szorzas_kijott_eredmenyek,
                                     megadott_szamok.szorzas_elso_ertek, megadott_szamok.szorzas_masodik_ertek,
                                     )
        szorozgatok.statisztika_szorzas += 1
        kerdes = input("Szeretne meg szamolasokat vegezni (Igen/Nem)? ").lower()

kerdes2 = input("Szeretne a statisztikai adatokat megjeleniteni (Igen/Nem)? ").lower()

# </editor-fold>osztalyokba_sorolas_04.py

# <editor-fold desc="Eredmenyek ertekelese">
stat_szamok = Szamolas
eredmenyek_omlesztve = stat_szamok.osszeadas_kijott_eredmenyek + stat_szamok.kivonas_kijott_eredmenyek + stat_szamok.osztas_kijott_eredmenyek + stat_szamok.szorzas_kijott_eredmenyek
stat_stat = Statisztika
stat_stat.tiznelnagyobbak(eredmenyek_omlesztve)
stat_stat.paratlanok(eredmenyek_omlesztve)
stat_stat.parosok(eredmenyek_omlesztve)

# </editor-fold>

# <editor-fold desc="Eredmenyek eltarolasa file-okba">
fileba_mentes = Mentesek
fileba_mentes.csv_mentes(stat_szamok, stat_szamok.statisztika_osszeadas, stat_szamok.osszeadas_kijott_eredmenyek,
                         stat_szamok.osszead_elso_ertek, stat_szamok.osszeadas_masodik_ertek,
                         stat_szamok.statisztika_kivonas, stat_szamok.kivonas_kijott_eredmenyek,
                         stat_szamok.kivonas_elso_ertek, stat_szamok.kivonas_masodik_ertek,
                         stat_szamok.statisztika_osztas, stat_szamok.osztas_kijott_eredmenyek,
                         stat_szamok.osztas_elso_ertek, stat_szamok.osztas_masodik_ertek,
                         stat_szamok.statisztika_szorzas, stat_szamok.szorzas_kijott_eredmenyek,
                         stat_szamok.szorzas_elso_ertek, stat_szamok.szorzas_masodik_ertek, stat_szamok.paros_szamok,
                         stat_szamok.paratlan_szamok, stat_szamok.tiznel_nagyobb_szamok)
fileba_mentes.xml_mentes(stat_szamok, stat_szamok.statisztika_osszeadas, stat_szamok.osszeadas_kijott_eredmenyek,
                         stat_szamok.osszead_elso_ertek, stat_szamok.osszeadas_masodik_ertek,
                         stat_szamok.statisztika_kivonas, stat_szamok.kivonas_kijott_eredmenyek,
                         stat_szamok.kivonas_elso_ertek, stat_szamok.kivonas_masodik_ertek,
                         stat_szamok.statisztika_osztas, stat_szamok.osztas_kijott_eredmenyek,
                         stat_szamok.osztas_elso_ertek, stat_szamok.osztas_masodik_ertek,
                         stat_szamok.statisztika_szorzas, stat_szamok.szorzas_kijott_eredmenyek,
                         stat_szamok.szorzas_elso_ertek, stat_szamok.szorzas_masodik_ertek, stat_szamok.paros_szamok,
                         stat_szamok.paratlan_szamok, stat_szamok.tiznel_nagyobb_szamok)
fileba_mentes.json_mentesek(stat_szamok, stat_szamok.statisztika_osszeadas, stat_szamok.osszeadas_kijott_eredmenyek,
                            stat_szamok.osszead_elso_ertek, stat_szamok.osszeadas_masodik_ertek,
                            stat_szamok.statisztika_kivonas, stat_szamok.kivonas_kijott_eredmenyek,
                            stat_szamok.kivonas_elso_ertek, stat_szamok.kivonas_masodik_ertek,
                            stat_szamok.statisztika_osztas, stat_szamok.osztas_kijott_eredmenyek,
                            stat_szamok.osztas_elso_ertek, stat_szamok.osztas_masodik_ertek,
                            stat_szamok.statisztika_szorzas, stat_szamok.szorzas_kijott_eredmenyek,
                            stat_szamok.szorzas_elso_ertek, stat_szamok.szorzas_masodik_ertek, stat_szamok.paros_szamok,
                            stat_szamok.paratlan_szamok, stat_szamok.tiznel_nagyobb_szamok)
fileba_mentes.pickle_mentesek(stat_szamok, stat_szamok.statisztika_osszeadas, stat_szamok.osszeadas_kijott_eredmenyek,
                              stat_szamok.osszead_elso_ertek, stat_szamok.osszeadas_masodik_ertek,
                              stat_szamok.statisztika_kivonas, stat_szamok.kivonas_kijott_eredmenyek,
                              stat_szamok.kivonas_elso_ertek, stat_szamok.kivonas_masodik_ertek,
                              stat_szamok.statisztika_osztas, stat_szamok.osztas_kijott_eredmenyek,
                              stat_szamok.osztas_elso_ertek, stat_szamok.osztas_masodik_ertek,
                              stat_szamok.statisztika_szorzas, stat_szamok.szorzas_kijott_eredmenyek,
                              stat_szamok.szorzas_elso_ertek, stat_szamok.szorzas_masodik_ertek,
                              stat_szamok.paros_szamok,
                              stat_szamok.paratlan_szamok, stat_szamok.tiznel_nagyobb_szamok)
fileba_mentes.shelve_mentesek(stat_szamok, stat_szamok.statisztika_osszeadas, stat_szamok.osszeadas_kijott_eredmenyek,
                              stat_szamok.osszead_elso_ertek, stat_szamok.osszeadas_masodik_ertek,
                              stat_szamok.statisztika_kivonas, stat_szamok.kivonas_kijott_eredmenyek,
                              stat_szamok.kivonas_elso_ertek, stat_szamok.kivonas_masodik_ertek,
                              stat_szamok.statisztika_osztas, stat_szamok.osztas_kijott_eredmenyek,
                              stat_szamok.osztas_elso_ertek, stat_szamok.osztas_masodik_ertek,
                              stat_szamok.statisztika_szorzas, stat_szamok.szorzas_kijott_eredmenyek,
                              stat_szamok.szorzas_elso_ertek, stat_szamok.szorzas_masodik_ertek,
                              stat_szamok.paros_szamok,
                              stat_szamok.paratlan_szamok, stat_szamok.tiznel_nagyobb_szamok)

# </editor-fold>

# <editor-fold desc="Eredmenyek kiiratasa a file-okbol">
if kerdes2 == 'igen':
    fileba_mentes.csv_kiiratas(stat_szamok)
    fileba_mentes.xml_kiiratas(stat_szamok)
    fileba_mentes.json_kiiratas(stat_szamok)
    fileba_mentes.pickle_kiiratas(stat_szamok, stat_szamok.statisztika_osszeadas,
                                  stat_szamok.osszeadas_kijott_eredmenyek,
                                  stat_szamok.osszead_elso_ertek, stat_szamok.osszeadas_masodik_ertek,
                                  stat_szamok.statisztika_kivonas, stat_szamok.kivonas_kijott_eredmenyek,
                                  stat_szamok.kivonas_elso_ertek, stat_szamok.kivonas_masodik_ertek,
                                  stat_szamok.statisztika_osztas, stat_szamok.osztas_kijott_eredmenyek,
                                  stat_szamok.osztas_elso_ertek, stat_szamok.osztas_masodik_ertek,
                                  stat_szamok.statisztika_szorzas, stat_szamok.szorzas_kijott_eredmenyek,
                                  stat_szamok.szorzas_elso_ertek, stat_szamok.szorzas_masodik_ertek,
                                  stat_szamok.paros_szamok,
                                  stat_szamok.paratlan_szamok, stat_szamok.tiznel_nagyobb_szamok)
    fileba_mentes.shelve_kiiratas(stat_szamok)


else:
    print("Akkor viszlat!")
# </editor-fold>

input('')
