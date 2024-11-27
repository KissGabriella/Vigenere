import tkinter as tk
from tkinter import messagebox
from vigenere import Vigenere

class VigenereApp:
    def __init__(self):
        self.ablak = tk.Tk()
        self.ablak.title("Vigenere-titkositas")
        self.ablak.geometry("500x400")
        self.ablak.wm_minsize(500, 400)
       # self.ablak.wm_maxsize(500, 400)
        self.ablak.resizable(False, False)
        self.ablak.configure()

        # GUI elemek
        tk.Label(self.ablak, text="Adja meg a szoveget:").pack(pady=5)
        self.szoveg_bemenet = tk.Text(self.ablak, height=5, width=50)
        self.szoveg_bemenet.pack()

        tk.Label(self.ablak, text="Adja meg a kulcsszot:").pack(pady=5)
        self.kulcs_bemenet = tk.Entry(self.ablak, width=30)
        self.kulcs_bemenet.pack()

        gomb_keret = tk.Frame(self.ablak)
        gomb_keret.pack(pady=10)
        tk.Button(gomb_keret, text="Titkositas", command=self.titkositas_gomb).pack(side=tk.LEFT, padx=5)
        tk.Button(gomb_keret, text="Visszafejtes", command=self.visszafejtes_gomb).pack(side=tk.LEFT, padx=5)

        tk.Label(self.ablak, text="Eredmeny:").pack(pady=5)
        self.eredmeny_kimenet = tk.Text(self.ablak, height=5, width=50)
        self.eredmeny_kimenet.pack()

    def titkositas_gomb(self):
        szoveg = self.szoveg_bemenet.get("1.0", tk.END).strip()
        kulcs = self.kulcs_bemenet.get().strip()

        if not szoveg or not kulcs:
            messagebox.showwarning("Figyelmeztetes", "Adja meg a szoveget es a kulcsszot!")
            return

        if not kulcs.isalpha():
            messagebox.showerror("Hiba", "A kulcsszonak csak betuket kell tartalmaznia!")
            return

        vigenere = Vigenere(kulcs)
        eredmeny = vigenere.titkositas(szoveg)
        self.eredmeny_kimenet.delete("1.0", tk.END)
        self.eredmeny_kimenet.insert(tk.END, eredmeny)

    def visszafejtes_gomb(self):
        szoveg = self.szoveg_bemenet.get("1.0", tk.END).strip()
        kulcs = self.kulcs_bemenet.get().strip()

        if not szoveg or not kulcs:
            messagebox.showwarning("Figyelmeztetes", "Adja meg a szoveget es a kulcsszot!")
            return

        if not kulcs.isalpha():
            messagebox.showerror("Hiba", "A kulcsszonak csak betuket kell tartalmaznia!")
            return

        vigenere = Vigenere(kulcs)
        eredmeny = vigenere.visszafejtes(szoveg)
        self.eredmeny_kimenet.delete("1.0", tk.END)
        self.eredmeny_kimenet.insert(tk.END, eredmeny)

    def futtat(self):
        self.ablak.mainloop()