class Samochud:
    def __init__(self, _cena, _r_paliwa, _przebieg, _wlasciciel):
        self._cena = _cena
        self._r_paliwa = _r_paliwa
        self._przebieg = _przebieg
        self._wlasciciel = _wlasciciel
        self._wlasciciele = []
        self._wlasciciele.append(self._wlasciciel)

    def inf(self):
        print("*" * 50)
        print(f"Cena: {self._cena}\n"
              f"Rodzaj Paliwa: {self._r_paliwa}\n"
              f"Przebieg: {self._przebieg}\n"
              f"Wlasciciel: {self._wlasciciel}")

    def edit_cena(self, nowa_cena):
        print("*" * 50)
        try:
            cena = int(nowa_cena)
            self._cena = cena
        except ValueError:
            print("To nie liczba")

    def edit_r_paliwa(self, nove_p):
        if nove_p.lower() == "benzyna" or nove_p.lower() == "gaz" or nove_p.lower() == "prand" or nove_p.lower() == "dyzel":
            self._r_paliwa = nove_p
        else:
            print("nie ma takiego rodzaju")

    def edit_przebieg(self, nowy_przebieg):
        print("*" * 50)
        try:
            nowy_p = int(nowy_przebieg)
            self._przebieg = nowy_p
        except ValueError:
            print("To nie liczba")

    def edit_wlasciciel(self, n_wl):
        self._wlasciciel = n_wl
        self._wlasciciele.append(self._wlasciciel)


def edit(ob: object) -> None:
    while True:
        ob.inf()
        print("*" * 50)
        inp = input("Co chcesz edukowac:\n"
                    "Cena - 1\n"
                    "Rodzaj Paliwa - 2\n"
                    "Przebieg - 3\n"
                    "Wlasciciel - 4\n"
                    "wyjsc - 5\n"
                    "Odp: ")
        if inp == "1":
            inp = input("Nowa cena: ")
            ob.edit_cena(inp)
        elif inp == "2":
            inp = input("NOwe paliwo: ")
            ob.edit_r_paliwa(inp)
        elif inp == "3":
            inp = input("Nowy przebieg: ")
            ob.edit_przebieg(inp)
        elif inp == "4":
            inp = input("Nowy wlasciciel: ")
            ob.edit_wlasciciel(inp)
        elif inp == "5":
            break
        else:
            print("Nie ma takiej opcji")
        ob.inf()


s = Samochud(300, "Benzyna", 300, "P W ")
edit(s)
