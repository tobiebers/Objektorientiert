class Artikel:
    __artikelnummer = ""
    __preis = ""
    __bezeichnung = ""
    __menge = ""
    __mwst_satz = ""
    artikel = []

    def __init__(self):
        ("Konstruktor Kunde wurde aufgerufen")
        
    def addArtikel(self, artikel):
        self.__artikel.append(artikel)

    def set_artikelnummer(self, __artikelnummer):
        self.__artikelnummer = __artikelnummer

    def set_preis (self, __preis):
        self.__preis = __preis

    def set_bezeichnung (self, __bezeichnung):
        self.__bezeichnung = __bezeichnung

    def set_menge (self, __menge):
        self.__menge = __menge

    def set_mwst (self, __mwst_satz):
        self.__mwst_satz = __mwst_satz

#-------------------------

    def get_artikelnummer(self):
        return self.__artikelnummer

    def get_preis(self):
        return self.__preis

    def get_bezeichnung(self):
        return self.__bezeichnung

    def get_menge(self):
        return self.__menge

    def get_mwst_satz(self):
        return self.__mwst_satz
