class Kunde:
    __vorname = ""
    __nachname = ""
    __email = ""
    __tel_nr = ""
    __strasse = ""
    __haus_nr = ""
    __plz = ""
    __ort = ""
    __bestellungen = []




    def __init__(self):
        ("Konstruktor Kunde wurde aufgerufen")

    def addBestellung(self, bestellung):
        self.__bestellungen.append(bestellung)

    def stornoAlle(self):
        self.__bestellungen.clear()

    def getBestellungen(self):
        return self.__bestellungen


    def setTel_nr(self, __tel_nr):
        self.__tel_nr = __tel_nr

    def setStrasse (self, __strasse):
        self.__strasse = __strasse

    def setemail (self, __email):
        self.__email = __email

    def setNachname (self, __nachname):
        self.__nachname = __nachname

    def setVorname (self, __vorname):
        self.__vorname = __vorname

    def setHaus_nr (self, __haus_nr):
        self.__haus_nr = __haus_nr

    def setPlz (self, __Plz):
        self.__Plz = __Plz

    def setOrt (self, __ort):
        self.__ort = __ort

#-------------------------

    def getTel_nr(self):
        return self.__tel_nr

    def getStrasse(self):
        return self.__strasse

    def getEmail(self):
        return self.__email

    def getNachname(self):
        return self.__nachname

    def getVorname(self):
        return self.__vorname

    def getHaus_nr(self):
        return self.__haus_nr

    def getPlz(self):
        return self.__plz

    def getOrt(self):
        return self.__ort