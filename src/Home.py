from tkinter import ttk, scrolledtext, messagebox, filedialog, Entry
from tkinter import *
import tkinter as tk
import os
import sqlite3
# import src.pageManager as pageManager

import src.pembangkitan as pembangkitan, src.EnkripDekrip as EnkripDekrip

class HomePage(Frame):
    

    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Home()

    def Home(self):
        self.canvas = Canvas(
            self.master,
            bg = "#FFFFFF",
            height = 500,
            width = 250,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.d = 26831
        self.n = 105559
        self.e = 40271

        self.canvas.place(x = 0, y = 0)
        ttk.Label(self.master, text ="E-Voting", font='Helvetika 10 bold').pack()
        ttk.Label(self.master, text ="18220001 Stephanie Hutagalung", font='Helvetika 8').pack()
        self.tabControl = ttk.Notebook(self.master)
        
        tab1 = Frame(self.tabControl, background="#FFFFFF")
        tab2 = Frame(self.tabControl, background="#FFFFFF")
        tab3 = Frame(self.tabControl, background="#FFFFFF")
        tab4 = Frame(self.tabControl, background="#FFFFFF")

        self.tabControl.add(tab1, text ='Token')
        self.tabControl.add(tab2, text ='Vote')
        self.tabControl.add(tab3, text ='Admin')
        self.tabControl.add(tab4, text ='Hitung Suara')
        self.tabControl.pack(expand = 1, fill ="both")
        
        # tab1
        ttk.Label(tab1, text ="NIM", background="#FFFFFF").grid(sticky='w', column = 0, row = 0, padx = 10, pady = 10)
        self.nim_voter = Text(tab1, width=60, height=1, font=("Times New Roman", 10))
        self.nim_voter.grid(column = 1, row=0, padx = 10, pady = 10)
        ttk.Label(tab1, text ="Password", background="#FFFFFF").grid(sticky='w', column = 0, row = 1, padx = 10, pady = 10)
        self.password = Entry(tab1, width=60, font=("Times New Roman", 10))
        self.password.grid(column = 1, row=1, padx = 10, pady = 10)
        self.password.config(show ="*")

        self.b1 = Button(tab1,text="Generate Token", bg='#FA8072',command=lambda: self.GenerateToken())
        self.b1.grid(row=2, columnspan = 3, pady = 2, padx = 5)

        
        self.StringToken = StringVar()
        self.StringToken.set("")
        self.teks_token = Label(tab1, textvariable = self.StringToken, background="#FFFFFF")
        self.teks_token.grid(sticky='w', columnspan = 3, row=3, padx = 10, pady = 10)

        
        # tab2
        ttk.Label(tab2, text ="NIM", background="#FFFFFF").grid(sticky='w', column = 0, row = 0, padx = 10, pady = 10)
        self.nim_voter2 = Text(tab2, width=60, height=1, font=("Times New Roman", 10))
        self.nim_voter2.grid(column = 1, row=0, padx = 10, pady = 10)
        ttk.Label(tab2, text ="Password", background="#FFFFFF").grid(sticky='w', column = 0, row = 1, padx = 10, pady = 10)
        self.password2 = Entry(tab2, width=60, font=("Times New Roman", 10))
        self.password2.grid(column = 1, row=1, padx = 10, pady = 10)
        self.password2.config(show ="*")
        ttk.Label(tab2, text ="token", background="#FFFFFF").grid(sticky='w', column = 0, row = 2, padx = 10, pady = 10)
        self.token = Text(tab2, width=60, height=1, font=("Times New Roman", 10))
        self.token.grid(column = 1, row=2, padx = 10, pady = 10)
        ttk.Label(tab2, text ="vote", background="#FFFFFF").grid(sticky='w', column = 0, row = 3, padx = 10, pady = 10)
        
        self.e3 = LabelFrame(tab2)
        self.radioe3 = IntVar()
        ttk.Radiobutton(self.e3, text="candidate1", variable=self.radioe3, value=1).grid(sticky="w", row = 1, column = 0)
        ttk.Radiobutton(self.e3, text="candidate2", variable=self.radioe3, value=2).grid(sticky="w", row = 1, column = 1)
        self.e3.grid(sticky="w", row = 3, column = 1, pady = 2)
       

        self.b2 = Button(tab2,text="Vote", bg='#FA8072',command=lambda: self.Vote())
        self.b2.grid(row=4, columnspan = 3, pady = 2, padx = 5)

        # tab3
        ttk.Label(tab3, text ="username", background="#FFFFFF").grid(sticky='w', column = 0, row = 0, padx = 10, pady = 10)
        self.username = Text(tab3, width=60, height=1, font=("Times New Roman", 10))
        self.username.grid(column = 1, row=0, padx = 10, pady = 10)
        ttk.Label(tab3, text ="password", background="#FFFFFF").grid(sticky='w', column = 0, row = 1, padx = 10, pady = 10)
        self.pass_admin = Entry(tab3, width=60, font=("Times New Roman", 10))
        self.pass_admin.grid(column = 1, row=1, padx = 10, pady = 10)
        self.pass_admin.config(show ="*")
        self.b2 = Button(tab3,text="Ubah Key", bg='#FA8072',command=lambda: self.Key())
        self.b2.grid(row=2, columnspan = 3, pady = 2, padx = 5)

        # tab4
        ttk.Label(tab4, text ="username", background="#FFFFFF").grid(sticky='w', column = 0, row = 0, padx = 10, pady = 10)
        self.username2 = Text(tab4, width=60, height=1, font=("Times New Roman", 10))
        self.username2.grid(column = 1, row=0, padx = 10, pady = 10)
        ttk.Label(tab4, text ="password", background="#FFFFFF").grid(sticky='w', column = 0, row = 1, padx = 10, pady = 10)
        self.pass_admin2 = Entry(tab4, width=60, font=("Times New Roman", 10))
        self.pass_admin2.grid(column = 1, row=1, padx = 10, pady = 10)
        self.pass_admin2.config(show="*")

        self.b2 = Button(tab4,text="Hitung Suara", bg='#FA8072',command=lambda: self.HitungSuara())
        self.b2.grid(row=2, columnspan = 3, pady = 2, padx = 5)

    def startPage(self):
        self.mainloop()

    def getnimvoter(self):
        conn = sqlite3.connect('database.db') 
        c = conn.cursor()
        query = """select voter_nim from voter"""
        c.execute(query)
        records = c.fetchall()
        c.close()
        return records

    def getnamavoter(self, nim):
        conn = sqlite3.connect('database.db') 
        c = conn.cursor()
        query = f"""select voter_name from voter where voter_nim == {nim}"""
        c.execute(query)
        records = c.fetchall()
        c.close()
        return records

    def checkpassword(self, nim, password):
        conn = sqlite3.connect('database.db') 
        c = conn.cursor()
        query = f"""select voter_pass from voter where voter_nim == {nim}"""
        c.execute(query)
        records = c.fetchall()
        c.close()
        if str(f"('{password}',)") == str(records[0]):
            return True
        else:
            return False

    def checkstatus(self, nim):
        conn = sqlite3.connect('database.db') 
        c = conn.cursor()
        query = f"""select status from voter where voter_nim == {nim}"""
        c.execute(query)
        records = c.fetchall()
        c.close()
        if  str(records[0]) == '(1,)':
            return True
        else: 
            False
    
    #  Generate Token
    def GenerateToken(self):
        NIM=''
        password = ''
        try:
            NIM = int(self.nim_voter.get("1.0", "end-1c"))
            password = self.password.get()
            if (NIM,) in self.getnimvoter():
                if self.checkpassword(NIM, password):
                    nama = self.getnamavoter(NIM)
                    nama_nim_pass = str(f"({nama}+{NIM}+{password})")
                    Token = EnkripDekrip.enkrip(nama_nim_pass, self.d, self.n)
                    self.StringToken.set(f"Token adalah {Token}")
                    messagebox.showinfo("Token",f"Token adalah {Token}")
                else:
                    self.StringToken.set("")
                    messagebox.showerror("Error","NIM dan password salah")
            else:
                self.StringToken.set("")
                messagebox.showerror("Error","NIM dan password salah")
        except:
            self.StringToken.set("")
            messagebox.showerror("Error","NIM dan password salah")

    def Vote(self) :
        try:
            NIM = int(self.nim_voter2.get("1.0", "end-1c"))
            password = self.password2.get()
            token = int(self.token.get("1.0", "end-1c"))
            nama = self.getnamavoter(NIM)
            nama_nim_pass = str(f"({nama}+{NIM}+{password})")
            if self.checkstatus(NIM):
                messagebox.showinfo("info", "Akun sudah melakukan vote, tidak ada percobaan voting kedua.")
            else:    
                verifying = EnkripDekrip.dekrip(nama_nim_pass, self.e, self.n, token)    
                if verifying:        
                    hasilvote = int(self.radioe3.get())
                    if hasilvote != 0:        
                        self.insertvote(hasilvote, NIM)        
                        messagebox.showinfo("info", "Voting berhasil!")
                    else:
                        messagebox.showinfo("info", "Voting tidak berhasil! Voter belum memilih.")
                else:        
                    messagebox.showerror("Error","NIM, password, dan token salah")
        except:
            messagebox.showerror("Error","NIM, password, dan token salah")

    def insertvote(self, hasilvote, nim):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        query = f"""insert into vote (vote) VALUES ({hasilvote})"""
        c.execute(query)
        query2 = f"""update voter set status == True where voter_nim == {nim}"""
        c.execute(query2)
        conn.commit()
        c.close()
        
    def Key(self):
        username = self.username.get("1.0", "end-1c")
        password = self.pass_admin.get()
        if username == 'admin' and password == 'admin':
            key = pembangkitan.genPubPrivKey()
            self.d = key[0]
            self.n = key[1]
            self.e = key[2]
            messagebox.showinfo("info", f"Key telah diubah")
        else:
            messagebox.showerror("Error","Username dan password salah")

    def HitungSuara(self):
        username = self.username2.get("1.0", "end-1c")
        password = self.pass_admin2.get()
        if username == 'admin' and password == 'admin':
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            query = f"""select vote, COUNT(*) from vote group by vote"""
            c.execute(query)
            conn.commit()
            records = c.fetchall()
            c.close()
            suara1, suara2 = 0, 0
            for i in range (len(records)):
                if records[i][0] == 1:
                    suara1 = records[i][1]
                else:
                    suara2 = records[i][1]
            suaratotal = suara1+suara2
            if suaratotal != 0:
                persensuara1 = round(suara1 / suaratotal * 100,2)
                persensuara2 = round(suara2 / suaratotal * 100,2)
            if suara2 > suara1:
                messagebox.showinfo("info", f"Suara terbanyak adalah kandidat 2, dengan perolehan suara {persensuara2} %")
            elif suara2 < suara1:
                messagebox.showinfo("info", f"Suara terbanyak adalah kandidat 1, dengan perolehan suara {persensuara1} %")
            elif suara1 == suara2 and suara1 != 0:
                messagebox.showinfo("info", "Hasil perolehan suara seri")
            else:
                messagebox.showinfo("info", "Belum ada yang melakukan vote.")
        else:
            messagebox.showerror("Error","Username dan password salah")  