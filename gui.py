import tkinter as tk
from tkinter import filedialog, messagebox
from vigenere import Vigenere

class VigenereApp:
    def __init__(self):
        self.ablak = tk.Tk()
        self.ablak.title("App")
        self.ablak.geometry("500x400")
        self.ablak.wm_minsize(500, 400)
        self.ablak.resizable(False, False)
        self.ablak.configure()

        tk.Label(self.ablak, text="Adja meg a szöveget:").pack(pady=5)
        self.szoveg_bemenet = tk.Text(self.ablak, height=5, width=50)
        self.szoveg_bemenet.pack()

        tk.Label(self.ablak, text="Adja meg a kulcsszót:").pack(pady=5)
        self.kulcs_bemenet = tk.Entry(self.ablak, width=30)
        self.kulcs_bemenet.pack()

        gomb_keret = tk.Frame(self.ablak)
        gomb_keret.pack(pady=10)
        tk.Button(gomb_keret, text="Titkosítás", command=self.titkositas_gomb).pack(side=tk.LEFT, padx=5)
        tk.Button(gomb_keret, text="Visszafejtés", command=self.visszafejtes_gomb).pack(side=tk.LEFT, padx=5)
        tk.Button(gomb_keret, text="Mentés fájlba", command=self.mentes_fajlba).pack(side=tk.LEFT, padx=5)

        tk.Label(self.ablak, text="Eredmény:").pack(pady=5)
        self.eredmeny_kimenet = tk.Text(self.ablak, height=5, width=50)
        self.eredmeny_kimenet.pack()

    def titkositas_gomb(self):
        szoveg = self.szoveg_bemenet.get("1.0", tk.END).strip()
        kulcs = self.kulcs_bemenet.get().strip()

        if not szoveg or not kulcs:
            messagebox.showwarning("Figyelmeztetés", "Adja meg a szöveget és a kulcsszót!")
            return

        if not kulcs.isalpha():
            messagebox.showerror("Hiba", "A kulcsszónak csak betüket kell tartalmaznia!")
            return

        vigenere = Vigenere(kulcs)
        eredmeny = vigenere.titkositas(szoveg)
        self.eredmeny_kimenet.delete("1.0", tk.END)
        self.eredmeny_kimenet.insert(tk.END, eredmeny)
        self.eredmeny_kimenet.config(state="disabled")


    def visszafejtes_gomb(self):
        szoveg = self.szoveg_bemenet.get("1.0", tk.END).strip()
        kulcs = self.kulcs_bemenet.get().strip()

        if not szoveg or not kulcs:
            messagebox.showwarning("Figyelmeztetés", "Adja meg a szöveget és a kulcsszót!")
            return

        if not kulcs.isalpha():
            messagebox.showerror("Hiba", "A kulcsszónak csak betüket kell tartalmaznia!")
            return

        vigenere = Vigenere(kulcs)
        eredmeny = vigenere.visszafejtes(szoveg)
        self.eredmeny_kimenet.delete("1.0", tk.END)
        self.eredmeny_kimenet.insert(tk.END, eredmeny)
        self.eredmeny_kimenet.config(state="disabled")


    def mentes_fajlba(self):
        kulcs = self.kulcs_bemenet.get().strip()
        eredeti_szoveg = self.szoveg_bemenet.get("1.0", tk.END).strip()
        eredmeny_szoveg = self.eredmeny_kimenet.get("1.0", tk.END).strip()

        if not kulcs or not eredeti_szoveg or not eredmeny_szoveg:
            messagebox.showwarning("Figyelmeztetés", "Nincs elég adat a fájl mentéséhez!")
            return

        fajlnev = filedialog.asksaveasfilename(
            initialfile=f"{kulcs}.txt", # Alapértelmezett fájlnév, f-string formázás
            defaultextension=".txt", # Kiterjesztés hozzáadása, ha nincs megadva
            filetypes=[("Szövegfájlok", "*.txt"), ("Minden fájl", "*.*")] # Fájl típusok szűrője
        )

        if fajlnev:
            try:
                with open(fajlnev, "a", encoding="utf-8") as fajl:
                    fajl.write(f"Eredeti szöveg:\n{eredeti_szoveg}\n")
                    fajl.write(f"Eredmény:\n{eredmeny_szoveg}\n\n")
                messagebox.showinfo("Sikeres mentés", f"A fájl mentve: {fajlnev}")
            except Exception as e:
                messagebox.showerror("Hiba", f"A fájl mentése nem sikerült: {e}")

    def futtat(self):
        self.ablak.mainloop()