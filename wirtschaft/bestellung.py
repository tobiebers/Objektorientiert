class Bestellung:
    __bezeichnung = ""
    __bestellnummer = ""
    __preis = ""
    __menge = ""
    __versandkosten = ""

    def __init__(self):
        print("Object createt")

    def setMenge (self, menge):
        self.__menge = menge

    def setVersandkosten (self, versandkosten):
        self.__versandkosten = versandkosten

    def setPreis (self, preis):
        self.__preis = preis

    def setBestellnummer (self, bestellnummer):
        self.__bestellnummer = bestellnummer

    def setBezeichnung (self, bezeichnung):
        self.__bezeichnung = bezeichnung

#-------------------------

    def getMenge(self):
        return self.__menge

    def getVersandkosten(self):
        return self.__versandkosten

    def getPreis(self):
        return self.__preis

    def getBestellnummer(self):
        return self.__bestellnummer

    def getBezeichnung(self):
        return self.__bezeichnung

