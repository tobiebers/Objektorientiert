from wirtschaft import Bestellung
from wirtschaft import Kunde


bestellung_1 = Bestellung()
bestellung_1.setMenge(5)
bestellung_1.setPreis(5)
bestellung_1.setVersandkosten(5)
bestellung_1.setBestellnummer(5)
bestellung_1.setBezeichnung("Artikel")

print(bestellung_1.getBezeichnung())


kunde_1 = Kunde()
kunde_1.setVorname("test")
kunde_1.addBestellung(bestellung_1)

bestellung_2 = Bestellung()
bestellung_2.setMenge(4)
bestellung_2.setPreis(4)
bestellung_2.setVersandkosten(4)
bestellung_2.setBestellnummer(4)
bestellung_2.setBezeichnung("Artikel 2")

kunde_1.addBestellung(bestellung_2)

print(kunde_1.getBestellungen())