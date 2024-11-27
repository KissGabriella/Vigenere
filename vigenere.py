class Vigenere:
    def __init__(self, kulcs):
        self.kulcs = kulcs.lower()

    def titkositas(self, szoveg):
        titkositott_szoveg = []
        kulcs_index = 0
        for karakter in szoveg:
            if karakter.isalpha():
                alap = ord('A') if karakter.isupper() else ord('a')
                eltol = ord(self.kulcs[kulcs_index % len(self.kulcs)]) - ord('a')
                titkositott_szoveg.append(chr((ord(karakter) - alap + eltol) % 26 + alap))
                kulcs_index += 1
            else:
                titkositott_szoveg.append(karakter)
        return ''.join(titkositott_szoveg)

    def visszafejtes(self, szoveg):
        visszafejtett_szoveg = []
        kulcs_index = 0
        for karakter in szoveg:
            if karakter.isalpha():
                alap = ord('A') if karakter.isupper() else ord('a')
                eltol = ord(self.kulcs[kulcs_index % len(self.kulcs)]) - ord('a')
                visszafejtett_szoveg.append(chr((ord(karakter) - alap - eltol) % 26 + alap))
                kulcs_index += 1
            else:
                visszafejtett_szoveg.append(karakter)
        return ''.join(visszafejtett_szoveg)
