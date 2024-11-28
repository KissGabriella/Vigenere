class Vigenere:
    def __init__(self, kulcs):
        self.kulcs = kulcs.lower()

    def titkositas(self, szoveg):
        titkositott_szoveg = [] # Eltolással módosított karakterek listája
        kulcs_index = 0 # A kulcsszót kisbetűssé alakítása
        for karakter in szoveg: # végigmegyünk a szöveg karakterein
            if karakter.isalpha(): # karakterek vizsgálata, betű-e vagy nem
                alap = ord('A') if karakter.isupper() else ord('a') # Eltolás kiinduló pontjának meghatározása
                eltol = ord(self.kulcs[kulcs_index % len(self.kulcs)]) - ord('a') # Eltolás értékének kiszámítása
                titkositott_szoveg.append(chr((ord(karakter) - alap + eltol) % 26 + alap)) # Eltolás elvégzése ->eltolt karakter
                kulcs_index += 1 # Kulcsindex növelése
            else:
                titkositott_szoveg.append(karakter) # Eltolt karaktert hozzáadja a listáhosoz
        return ''.join(titkositott_szoveg) # Összefűzi a lista elemeit elválsztókarakter nélkül

    def visszafejtes(self, szoveg):
        visszafejtett_szoveg = []
        kulcs_index = 0
        for karakter in szoveg:
            if karakter.isalpha():
                alap = ord('A') if karakter.isupper() else ord('a')
                eltol = ord(self.kulcs[kulcs_index % len(self.kulcs)]) - ord('a')
                visszafejtett_szoveg.append(chr((ord(karakter) - alap - eltol) % 26 + alap)) # Eltolás elvégzése -> eredeti karakter
                kulcs_index += 1
            else:
                visszafejtett_szoveg.append(karakter)
        return ''.join(visszafejtett_szoveg)
