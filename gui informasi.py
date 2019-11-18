#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:53:29 2019

@author: bhaskaraby
"""

from tkinter import Tk, Frame, StringVar, Label, Entry, Button, OptionMenu, messagebox
import numpy as np
import pandas as pd
import mysql.connector
import hashlib
import aes

db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Madem45aw^_^",
        database = "bros"
        )
csr = db.cursor()
root = Tk()

class Main():
    def __init__(self, master, title):
        self.master = master
        self.master.title(title)
        self.master.config(background="#333333")
        self.loginPage()
                           
    def loginPage(self):
        self.frameInput = Frame(self.master)
        self.frameInput.grid(row=0, column=0)
        lblUsername = Label(self.frameInput, text="Username")
        lblUsername.grid(row=0, column=0, padx=5, pady=10)
        self.username = StringVar(value="")
        entryUsername = Entry(self.frameInput, width="20", textvariable=self.username, font="Calibri 15")
        entryUsername.grid(row=0, column=1, padx=10, pady=10)
        lblPassword = Label(self.frameInput, text="Password")
        lblPassword.grid(row=1, column=0, padx=5, pady=10)
        self.password = StringVar(value="")
        entryPassword = Entry(self.frameInput, width="20", show="*", textvariable=self.password, font="Calibri 15")
        entryPassword.grid(row=1, column=1, padx=10, pady=10)
        btnLogin = Button(self.frameInput, text="Login", command=self.login)
        btnLogin.grid(row=2, column=0, pady=15, columnspan=2)
        
    def login(self):
        username = self.username.get()
        password = hashlib.md5(self.password.get().encode('utf-8')).hexdigest()
        sql = "SELECT username,password,role FROM user WHERE username = %s"
        csr.execute(sql, (username,))
        user_verified = csr.fetchone()
        if username == user_verified[0] and password == user_verified[1]:
            messagebox.showinfo("Message", "Login berhasil!")
            self.user = username
            self.role = str(user_verified[2])
            self.frameInput.destroy()
            self.mainPage()
        else:
            messagebox.showinfo("Message", "Username atau Password salah.")
            
    def mainPage(self):
        self.absensi = []
        frameTop = Frame(self.master)
        frameTop.grid(row=0, column=0, padx=10, sticky="W")
        self.frameMid = Frame(self.master)
        self.frameMid.grid(row=1, column=0, padx=10)
        if self.role == 'mahasiswa':
            sql = 'SELECT k.nama FROM absensi a INNER JOIN mata_kuliah k ON k.id = a.matkul_id INNER JOIN mahasiswa m ON m.id = a.mhs_id WHERE m.nim = %s'
        else:
            sql = 'SELECT k.nama FROM absensi a INNER JOIN mata_kuliah k ON k.id = a.matkul_id INNER JOIN dosen_pengajar d ON d.id = a.dos_id INNER JOIN user u ON u.mhs_dos_id = d.id WHERE u.username = %s'
        csr.execute(sql, (self.user,))
        matkuls = np.unique(np.array(csr.fetchall(), dtype=str).flatten())
        self.matkulSelected = StringVar(value="Pilih Matkul")
        OpmMatkul = OptionMenu(frameTop, self.matkulSelected, *matkuls)
        OpmMatkul.grid(row=0, column=0)
        btnLihat = Button(frameTop, text="Check", command=self.checkAbsensi)
        btnLihat.grid(row=0, column=1)
        btnCetak = Button(frameTop, text="Cetak", command=self.cetakAbsensi)
        btnCetak.grid(row=0, column=2, sticky="E")
        headerTabel = ['No', 'NIM', 'Nama', 'Absensi']
        MidHeader1 = Label(self.frameMid, text=headerTabel[0], width="4")
        MidHeader1.grid(row=0, column=0)
        MidHeader2 = Label(self.frameMid, text=headerTabel[1], width="10")
        MidHeader2.grid(row=0, column=1)
        MidHeader3 = Label(self.frameMid, text=headerTabel[2], width="45")
        MidHeader3.grid(row=0, column=2)
        MidHeader4 = Label(self.frameMid, text=headerTabel[3])
        MidHeader4.grid(row=0, column=3, columnspan=12)
        self.MidContain1 = []
        self.MidContain2 = []
        self.MidContain3 = []
        self.MidContain4 = []
        
        
    def checkAbsensi(self):
        if self.role == 'mahasiswa':
            sql = "SELECT m.nim, m.nama, a.p1, a.p2, a.p3, a.p4, a.p5, a.p6, a.p7, a.p8, a.p9, a.p10, a.p11, a.p12, u.password FROM mahasiswa m INNER JOIN absensi a ON a.mhs_id = m.id INNER JOIN user u ON u.username = m.nim INNER JOIN mata_kuliah k ON k.id = a.matkul_id WHERE m.nim = %s AND k.nama = %s"
            csr.execute(sql, (self.user, self.matkulSelected.get()))
        else:
            sql = "SELECT m.nim, m.nama, a.p1, a.p2, a.p3, a.p4, a.p5, a.p6, a.p7, a.p8, a.p9, a.p10, a.p11, a.p12, u.password FROM mahasiswa m INNER JOIN absensi a ON a.mhs_id = m.id INNER JOIN dosen_pengajar d ON d.id = a.dos_id INNER JOIN user u ON u.username = m.nim INNER JOIN mata_kuliah k ON k.id = a.matkul_id WHERE k.nama = %s;"
            csr.execute(sql, (self.matkulSelected.get(),))
        self.absensi = np.array(csr.fetchall(), dtype=str)
        self.showAbsensi(self.absensi)
        
    def cetakAbsensi(self):
        if len(self.absensi) > 0:
            absensi = self.absensi
            tmp = np.copy(self.absensi)
            for i in range(len(absensi)):
                for j in range(2, len(absensi[i]) - 1):
                    if absensi[i,j] == "":
                        tmp[i,j] = "belum absen"
                    elif int(aes.AESCipher(absensi[i, -1]).decrypt(absensi[i,j])) < 0:
                        tmp[i,j] = "tidak hadir"
                    elif int(aes.AESCipher(absensi[i, -1]).decrypt(absensi[i,j])) > 0:
                        tmp[i,j] = "hadir"
            tmp = tmp[:, :-1]
            colhead = ['NIM', 'Nama', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12']
            df = pd.DataFrame(tmp)
            df.to_excel('Absensi %s.xlsx' % self.matkulSelected.get(), index=False, header=colhead)
            messagebox.showinfo("Message", "Absensi tersimpan sebagai Absensi %s.xlsx" % self.matkulSelected.get())
    
    def showAbsensi(self, absensi):
        self.clearTable()
        for i in range(len(absensi)):
            self.MidContain1.append(Label(self.frameMid, font="12", width="4", text=str(i+1)))
            self.MidContain2.append(Label(self.frameMid, font="12", width="10", text=absensi[i,0]))
            self.MidContain3.append(Label(self.frameMid, font="12", width="45", text=absensi[i,1]))
            self.MidContain1[-1].grid(row=i+1, column=0)
            self.MidContain2[-1].grid(row=i+1, column=1)
            self.MidContain3[-1].grid(row=i+1, column=2)
            for j in range(3,15):
                if absensi[i,j-1] == "":
                    self.MidContain4.append(Label(self.frameMid, width="2", bg="#ffffff", borderwidth="1", relief="groove"))
                elif int(aes.AESCipher(absensi[i, -1]).decrypt(absensi[i,j-1])) < 0:
                    self.MidContain4.append(Label(self.frameMid, width="2", bg="#ff0000", borderwidth="1", relief="groove"))
                elif int(aes.AESCipher(absensi[i, -1]).decrypt(absensi[i,j-1])) > 0:
                    self.MidContain4.append(Label(self.frameMid, width="2", bg="#00ff00", borderwidth="1", relief="groove"))
                self.MidContain4[-1].grid(row=i+1, column=j)
                
    def clearTable(self):
        for i in range(len(self.MidContain1)):
            self.MidContain1[i].destroy()
            self.MidContain2[i].destroy()
            self.MidContain3[i].destroy()
        for i in range(len(self.MidContain4)):
            self.MidContain4[i].destroy()
                           
Main(root, "== Informasi ==")
root.mainloop()
