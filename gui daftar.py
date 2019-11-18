#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:12:29 2019

@author: bhaskaraby
"""

from tkinter import Tk, Frame, StringVar, Label, Entry, Button, OptionMenu, messagebox, filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2
import bluetooth
import pandas as pd
import mysql.connector
import hashlib

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
        self.mainFrame = Frame(self.master)
        self.loginPage()
        #self.mainPage()
        #self.tampilFrame(1)
        
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
        sql = "SELECT username,password FROM user WHERE username = %s"
        csr.execute(sql, (username,))
        user_verified = csr.fetchone()
        if username == user_verified[0] and password == user_verified[1]:
            messagebox.showinfo("Message", "Login Berhasil!")
            self.frameInput.destroy()
            self.mainPage()
            self.tampilFrame(1)
        else:
            messagebox.showinfo("Message", "Username atau Password salah.")
            
    def mainPage(self):
        frameTab = Frame(self.master)
        frameTab.grid(row=0, column=0, padx=10, sticky="W")
        self.btnTabMhs = Button(frameTab, text="Daftarkan Mahasiswa", bg="#ffffff", command=lambda:self.tampilFrame(1))
        self.btnTabMhs.grid(row=0, column=0, sticky="W")
        self.btnTabDos = Button(frameTab, text="Daftarkan Dosen", bg="#ffffff", command=lambda:self.tampilFrame(2))
        self.btnTabDos.grid(row=0, column=1, sticky="W")
        self.btnTabMtk = Button(frameTab, text="Daftarkan Mata Kuliah", bg="#ffffff", command=lambda:self.tampilFrame(3))
        self.btnTabMtk.grid(row=0, column=2, sticky="W")
        self.btnTabAbs = Button(frameTab, text="Lihat Absensi", bg="#ffffff", command=lambda:self.tampilFrame(4))
        self.btnTabAbs.grid(row=0, column=3, sticky="W")
        
    def tampilFrame(self, idx):
        if idx == 1:
            sql = "SELECT * FROM mahasiswa"
            csr.execute(sql)
            temp = np.array(csr.fetchall())
            if len(temp) > 0:
                self.tempData = temp[:, 1:]
            else:
                self.tempData = temp
            self.path = "konden mepoto.jpg"
            self.ambilImg()
            self.btnTabMhs.config(bg="#5adced")
            self.btnTabDos.config(bg="#ffffff")
            self.btnTabMtk.config(bg="#ffffff")
            self.btnTabAbs.config(bg="#ffffff")
            self.image_empty = Image.open("konden mepoto.jpg")
            self.image_empty = ImageTk.PhotoImage(self.image_empty)
            self.mainFrame.destroy()
            self.mainFrame = Frame(self.master)
            self.mainFrame.grid(row=1, column=0, padx=10, sticky="N")
            #MAIN TABLE FRAME SECTION
            frameMainTbl = Frame(self.mainFrame)
            frameMainTbl.grid(row=0, column=0, rowspan=2)
            frameFormDftr = Frame(self.mainFrame)
            frameFormDftr.grid(row=0, column=1, padx=10, pady=10, rowspan=2)
            frameBtDet = Frame(self.mainFrame)
            frameBtDet.grid(row=2, column=1, padx=10, pady=10)
            frameOperator = Frame(self.mainFrame)
            frameOperator.grid(row=2, column=0, padx=10, pady=10)
            headerTabel = ['No', 'NIM', 'Nama', 'Opsi']
            mainTblHeader1 = Label(frameMainTbl, text=headerTabel[0], font="12", width="4")
            mainTblHeader1.grid(row=0, column=0)
            mainTblHeader2 = Label(frameMainTbl, text=headerTabel[1], font="12", width="10")
            mainTblHeader2.grid(row=0, column=1)
            mainTblHeader3 = Label(frameMainTbl, text=headerTabel[2], font="12", width="45")
            mainTblHeader3.grid(row=0, column=2)
            mainTblHeader4 = Label(frameMainTbl, text=headerTabel[3], font="12", width="6")
            mainTblHeader4.grid(row=0, column=3, columnspan=3)
            self.mainTblContain1 = []
            self.mainTblContain2 = []
            self.mainTblContain3 = []
            for i in range(1,11):
                self.mainTblContain1.append(Label(frameMainTbl, font="12", width="4"))
                self.mainTblContain2.append(Label(frameMainTbl, font="12", width="10"))
                self.mainTblContain3.append(Label(frameMainTbl, font="12", width="45"))
                self.mainTblContain1[-1].grid(row=i, column=0)
                self.mainTblContain2[-1].grid(row=i, column=1)
                self.mainTblContain3[-1].grid(row=i, column=2)
            self.mainTbl1Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl2Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl3Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl4Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl5Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl6Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl7Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl8Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl9Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl10Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl1Contain4.grid(row=1, column=3)
            self.mainTbl2Contain4.grid(row=2, column=3)
            self.mainTbl3Contain4.grid(row=3, column=3)
            self.mainTbl4Contain4.grid(row=4, column=3)
            self.mainTbl5Contain4.grid(row=5, column=3)
            self.mainTbl6Contain4.grid(row=6, column=3)
            self.mainTbl7Contain4.grid(row=7, column=3)
            self.mainTbl8Contain4.grid(row=8, column=3)
            self.mainTbl9Contain4.grid(row=9, column=3)
            self.mainTbl10Contain4.grid(row=10, column=3)
            self.mainTbl1Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl2Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl3Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl4Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl5Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl6Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl7Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl8Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl9Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl10Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl1Contain5.grid(row=1, column=4)
            self.mainTbl2Contain5.grid(row=2, column=4)
            self.mainTbl3Contain5.grid(row=3, column=4)
            self.mainTbl4Contain5.grid(row=4, column=4)
            self.mainTbl5Contain5.grid(row=5, column=4)
            self.mainTbl6Contain5.grid(row=6, column=4)
            self.mainTbl7Contain5.grid(row=7, column=4)
            self.mainTbl8Contain5.grid(row=8, column=4)
            self.mainTbl9Contain5.grid(row=9, column=4)
            self.mainTbl10Contain5.grid(row=10, column=4)
            self.searchBar = Entry(frameMainTbl)
            self.searchBar.grid(row=11, column=0, sticky="W", padx=8)
            btnSearch = Button(frameMainTbl, text="Cari", command=self.searchData)
            btnSearch.grid(row=11, column=1, sticky="W")
            self.mainPageNumber = 1
            mainTblPaging1 = Button(frameMainTbl, text="<", command=lambda:self.mainChangePage('prev', 1))
            mainTblPaging1.grid(row=11, column=2, sticky="E")
            self.mainTblPage = Label(frameMainTbl, text=str(self.mainPageNumber))
            self.mainTblPage.grid(row=11, column=3)
            mainTblPaging2 = Button(frameMainTbl, text=">", command=lambda:self.mainChangePage('next', 1))
            mainTblPaging2.grid(row=11, column=4, sticky="W")
            #FORM FRAME SECTION
            self.btnPhoto = Button(frameFormDftr, bg="#ffffff", width="100", height="130", command=self.browse, image=self.image_empty)
            self.btnPhoto.grid(row=0, columnspan=3, padx=5, pady=5)
            self.btnPhoto.image = self.image_empty
            labelNama = Label(frameFormDftr, font="12", width="10", text="Nama")
            labelNama.grid(row=1, column=0, padx=5, pady=3)
            self.nama = StringVar(value="")
            entryNama = Entry(frameFormDftr, font="12", textvariable=self.nama, width="20")
            entryNama.grid(row=1, column=1, columnspan=2, padx=4, pady=3)
            labelNIM = Label(frameFormDftr, font="12", width="10", text="NIM")
            labelNIM.grid(row=2, column=0, padx=3, pady=3)
            self.NIM = StringVar(value="")
            entryNIM = Entry(frameFormDftr, font="12", textvariable=self.NIM, width="20")
            entryNIM.grid(row=2, column=1, columnspan=2, padx=4, pady=3)
            labelPass = Label(frameFormDftr, font="12", width="10", text="Password")
            labelPass.grid(row=3, column=0, padx=3, pady=3)
            self.passw = StringVar(value="")
            entryPassw = Entry(frameFormDftr, font="12", textvariable=self.passw, width="20")
            entryPassw.grid(row=3, column=1, columnspan=2, padx=4, pady=3)
            labelNoHP = Label(frameFormDftr, font="12", width="10", text="No HP")
            labelNoHP.grid(row=4, column=0, padx=3, pady=3)
            self.NoHP = StringVar(value="")
            entryNoHp = Entry(frameFormDftr, font="12", textvariable=self.NoHP, width="20")
            entryNoHp.grid(row=4, column=1, columnspan=2, padx=4, pady=3)
            labelBtAddr = Label(frameFormDftr, font="12", width="10", text="MAC")
            labelBtAddr.grid(row=5, column=0, padx=3, pady=3)
            self.BtAddr = StringVar(value="")
            entryBtAddr = Entry(frameFormDftr, font="12", textvariable=self.BtAddr, width="20")
            entryBtAddr.grid(row=5, column=1, columnspan=2, padx=4, pady=3)
            labelFakultas = Label(frameFormDftr, font="12", width="10", text="Fakultas")
            labelFakultas.grid(row=6, column=0, padx=3, pady=3)
            self.fakultas = StringVar(value="")
            entryFakultas = Entry(frameFormDftr, font="12", textvariable=self.fakultas, width="20")
            entryFakultas.grid(row=6, column=1, columnspan=2, padx=4, pady=3)
            labelJurusan = Label(frameFormDftr, font="12", width="10", text="Jurusan")
            labelJurusan.grid(row=7, column=0, padx=3, pady=3)
            self.jurusan = StringVar(value="")
            entryJurusan = Entry(frameFormDftr, font="12", textvariable=self.jurusan, width="20")
            entryJurusan.grid(row=7, column=1, columnspan=2, padx=4, pady=3)
            labelAngkatan = Label(frameFormDftr, font="12", width="10", text="Angkatan")
            labelAngkatan.grid(row=8, column=0, padx=3, pady=3)
            self.angkatan = StringVar(value="")
            entryAngkatan = Entry(frameFormDftr, font="12", textvariable=self.angkatan, width="20")
            entryAngkatan.grid(row=8, column=1, columnspan=2, padx=4, pady=3)
            btnScan = Button(frameFormDftr, text="Scan Bluetooth", command=self.scanBluetooth)
            btnScan.grid(row=9, column=0)
            self.btnSave = Button(frameFormDftr, text="Simpan", command=self.saveData)
            self.btnSave.grid(row=9, column=1, columnspan=2)
            #BLUETOOTH FRAME SECTION
            self.bt1Cols1 = Label(frameBtDet, width="25", height="1", font="Helvetica 10")
            self.bt2Cols1 = Label(frameBtDet, width="25", height="1", font="Helvetica 10")
            self.bt3Cols1 = Label(frameBtDet, width="25", height="1", font="Helvetica 10")
            self.bt4Cols1 = Label(frameBtDet, width="25", height="1", font="Helvetica 10")
            self.bt5Cols1 = Label(frameBtDet, width="25", height="1", font="Helvetica 10")
            self.bt1Cols2 = Label(frameBtDet, width="20", height="1", font="Helvetica 10")
            self.bt2Cols2 = Label(frameBtDet, width="20", height="1", font="Helvetica 10")
            self.bt3Cols2 = Label(frameBtDet, width="20", height="1", font="Helvetica 10")
            self.bt4Cols2 = Label(frameBtDet, width="20", height="1", font="Helvetica 10")
            self.bt5Cols2 = Label(frameBtDet, width="20", height="1", font="Helvetica 10")
            self.bt1Cols3 = Button(frameBtDet, command=lambda:self.printToMAC(""))
            self.bt2Cols3 = Button(frameBtDet, command=lambda:self.printToMAC(""))
            self.bt3Cols3 = Button(frameBtDet, command=lambda:self.printToMAC(""))
            self.bt4Cols3 = Button(frameBtDet, command=lambda:self.printToMAC(""))
            self.bt5Cols3 = Button(frameBtDet, command=lambda:self.printToMAC(""))
            self.bt1Cols1.grid(row=0, column=0, padx=2, pady=2)
            self.bt2Cols1.grid(row=1, column=0, padx=2, pady=2)
            self.bt3Cols1.grid(row=2, column=0, padx=2, pady=2)
            self.bt4Cols1.grid(row=3, column=0, padx=2, pady=2)
            self.bt5Cols1.grid(row=4, column=0, padx=2, pady=2)
            self.bt1Cols2.grid(row=0, column=1, padx=3, pady=2)
            self.bt2Cols2.grid(row=1, column=1, padx=3, pady=2)
            self.bt3Cols2.grid(row=2, column=1, padx=3, pady=2)
            self.bt4Cols2.grid(row=3, column=1, padx=3, pady=2)
            self.bt5Cols2.grid(row=4, column=1, padx=3, pady=2)
            self.bt1Cols3.grid(row=0, column=2, padx=1, pady=2)
            self.bt2Cols3.grid(row=1, column=2, padx=1, pady=2)
            self.bt3Cols3.grid(row=2, column=2, padx=1, pady=2)
            self.bt4Cols3.grid(row=3, column=2, padx=1, pady=2)
            self.bt5Cols3.grid(row=4, column=2, padx=1, pady=2)
            scrollUpBtn = Button(frameBtDet, text="previous", command=lambda:self.btChangePage('prev'))
            scrollUpBtn.grid(row=5, column=1, sticky="E", padx=5)
            scrollUpBtn = Button(frameBtDet, text="next", command=lambda:self.btChangePage('next'))
            scrollUpBtn.grid(row=5, column=2)
            self.btPages = 1
            self.writeToTable(self.tempData[:10])
            
        elif idx == 2:
            self.btnTabMhs.config(bg="#ffffff")
            self.btnTabDos.config(bg="#5adced")
            self.btnTabMtk.config(bg="#ffffff")
            self.btnTabAbs.config(bg="#ffffff")
            sql = "SELECT * FROM dosen_pengajar"
            csr.execute(sql)
            temp = np.array(csr.fetchall())
            if len(temp) > 0:
                self.tempData = temp[:,1:]
            else:
                self.tempData = []
            self.path = "konden mepoto.jpg"
            self.ambilImg()
            self.image_empty = Image.open("konden mepoto.jpg")
            self.image_empty = ImageTk.PhotoImage(self.image_empty)
            self.mainFrame.destroy()
            self.mainFrame = Frame(self.master)
            self.mainFrame.grid(row=1, column=0, padx=10, sticky="N")
            #MAIN TABLE FRAME SECTION
            frameMainTbl = Frame(self.mainFrame)
            frameMainTbl.grid(row=0, column=0, rowspan=2)
            frameFormDftr = Frame(self.mainFrame)
            frameFormDftr.grid(row=0, column=1, padx=10, pady=10, rowspan=2)
            frameBtDet = Frame(self.mainFrame)
            frameBtDet.grid(row=2, column=1, padx=10, pady=10)
            frameOperator = Frame(self.mainFrame)
            frameOperator.grid(row=2, column=0, padx=10, pady=10)
            headerTabel = ['No', 'NIP', 'Nama', 'Opsi']
            mainTblHeader1 = Label(frameMainTbl, text=headerTabel[0], font="12", width="4")
            mainTblHeader1.grid(row=0, column=0)
            mainTblHeader2 = Label(frameMainTbl, text=headerTabel[1], font="12", width="15")
            mainTblHeader2.grid(row=0, column=1)
            mainTblHeader3 = Label(frameMainTbl, text=headerTabel[2], font="12", width="45")
            mainTblHeader3.grid(row=0, column=2)
            mainTblHeader4 = Label(frameMainTbl, text=headerTabel[3], font="12", width="6")
            mainTblHeader4.grid(row=0, column=3, columnspan=3)
            self.mainTblContain1 = []
            self.mainTblContain2 = []
            self.mainTblContain3 = []
            for i in range(1,11):
                self.mainTblContain1.append(Label(frameMainTbl, font="12", width="4"))
                self.mainTblContain2.append(Label(frameMainTbl, font="12", width="15"))
                self.mainTblContain3.append(Label(frameMainTbl, font="12", width="45"))
                self.mainTblContain1[-1].grid(row=i, column=0)
                self.mainTblContain2[-1].grid(row=i, column=1)
                self.mainTblContain3[-1].grid(row=i, column=2)
            self.mainTbl1Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl2Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl3Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl4Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl5Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl6Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl7Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl8Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl9Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl10Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl1Contain4.grid(row=1, column=3)
            self.mainTbl2Contain4.grid(row=2, column=3)
            self.mainTbl3Contain4.grid(row=3, column=3)
            self.mainTbl4Contain4.grid(row=4, column=3)
            self.mainTbl5Contain4.grid(row=5, column=3)
            self.mainTbl6Contain4.grid(row=6, column=3)
            self.mainTbl7Contain4.grid(row=7, column=3)
            self.mainTbl8Contain4.grid(row=8, column=3)
            self.mainTbl9Contain4.grid(row=9, column=3)
            self.mainTbl10Contain4.grid(row=10, column=3)
            self.mainTbl1Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl2Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl3Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl4Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl5Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl6Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl7Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl8Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl9Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl10Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl1Contain5.grid(row=1, column=4)
            self.mainTbl2Contain5.grid(row=2, column=4)
            self.mainTbl3Contain5.grid(row=3, column=4)
            self.mainTbl4Contain5.grid(row=4, column=4)
            self.mainTbl5Contain5.grid(row=5, column=4)
            self.mainTbl6Contain5.grid(row=6, column=4)
            self.mainTbl7Contain5.grid(row=7, column=4)
            self.mainTbl8Contain5.grid(row=8, column=4)
            self.mainTbl9Contain5.grid(row=9, column=4)
            self.mainTbl10Contain5.grid(row=10, column=4)
            self.searchBar = Entry(frameMainTbl)
            self.searchBar.grid(row=11, column=0, sticky="W", padx=8)
            btnSearch = Button(frameMainTbl, text="Cari", command=self.searchDataDosen)
            btnSearch.grid(row=11, column=1, sticky="W")
            self.mainPageNumber = 1
            mainTblPaging1 = Button(frameMainTbl, text="<", command=lambda:self.mainChangePage('prev', 2))
            mainTblPaging1.grid(row=11, column=2, sticky="E")
            self.mainTblPage = Label(frameMainTbl, text=str(self.mainPageNumber))
            self.mainTblPage.grid(row=11, column=3)
            mainTblPaging2 = Button(frameMainTbl, text=">", command=lambda:self.mainChangePage('next', 2))
            mainTblPaging2.grid(row=11, column=4, sticky="W")
            #FORM FRAME SECTION
            self.btnPhoto = Button(frameFormDftr, bg="#ffffff", width="100", height="130", command=self.browse, image=self.image_empty)
            self.btnPhoto.grid(row=0, columnspan=3, padx=5, pady=5)
            self.btnPhoto.image = self.image_empty
            labelNama = Label(frameFormDftr, font="12", width="10", text="Nama")
            labelNama.grid(row=1, column=0, padx=5, pady=3)
            self.nama = StringVar(value="")
            entryNama = Entry(frameFormDftr, font="12", textvariable=self.nama, width="20")
            entryNama.grid(row=1, column=1, columnspan=2, padx=4, pady=3)
            labelNIP = Label(frameFormDftr, font="12", width="10", text="NIP")
            labelNIP.grid(row=2, column=0, padx=3, pady=3)
            self.NIP = StringVar(value="")
            entryNIP = Entry(frameFormDftr, font="12", textvariable=self.NIP, width="20")
            entryNIP.grid(row=2, column=1, columnspan=2, padx=4, pady=3)
            labelUsername = Label(frameFormDftr, font="12", width="10", text="Username")
            labelUsername.grid(row=3, column=0, padx=3, pady=3)
            self.username = StringVar(value="")
            entryUsername = Entry(frameFormDftr, font="12", textvariable=self.username, width="20")
            entryUsername.grid(row=3, column=1, columnspan=2, padx=4, pady=3)
            labelPassword = Label(frameFormDftr, font="12", width="10", text="Password")
            labelPassword.grid(row=4, column=0, padx=3, pady=3)
            self.passw = StringVar(value="")
            entryPassword = Entry(frameFormDftr, font="12", textvariable=self.passw, width="20")
            entryPassword.grid(row=4, column=1, columnspan=2, padx=4, pady=3)
            labelNoHP = Label(frameFormDftr, font="12", width="10", text="No HP")
            labelNoHP.grid(row=5, column=0, padx=3, pady=3)
            self.NoHP = StringVar(value="")
            entryNoHp = Entry(frameFormDftr, font="12", textvariable=self.NoHP, width="20")
            entryNoHp.grid(row=5, column=1, columnspan=2, padx=4, pady=3)
            labelFakultas = Label(frameFormDftr, font="12", width="10", text="Fakultas")
            labelFakultas.grid(row=6, column=0, padx=3, pady=3)
            self.fakultas = StringVar(value="")
            entryFakultas = Entry(frameFormDftr, font="12", textvariable=self.fakultas, width="20")
            entryFakultas.grid(row=6, column=1, columnspan=2, padx=4, pady=3)
            labelJurusan = Label(frameFormDftr, font="12", width="10", text="Jurusan")
            labelJurusan.grid(row=7, column=0, padx=3, pady=3)
            self.jurusan = StringVar(value="")
            entryJurusan = Entry(frameFormDftr, font="12", textvariable=self.jurusan, width="20")
            entryJurusan.grid(row=7, column=1, columnspan=2, padx=4, pady=3)
            self.btnSave = Button(frameFormDftr, text="Simpan", command=self.saveDataDosen)
            self.btnSave.grid(row=8, column=1, columnspan=2)
            self.writeToTableDosen(self.tempData[:10])
            
        elif idx == 3:
            self.btnTabMhs.config(bg="#ffffff")
            self.btnTabDos.config(bg="#ffffff")
            self.btnTabMtk.config(bg="#5adced")
            self.btnTabAbs.config(bg="#ffffff")
            self.mainFrame.destroy()
            sql = "SELECT * FROM mata_kuliah"
            csr.execute(sql)
            temp = np.array(csr.fetchall())
            if len(temp) > 0:
                self.tempData = temp[:,1:]
            else:
                self.tempData = []
            self.mainFrame = Frame(self.master)
            self.mainFrame.grid(row=1, column=0, padx=10, sticky="N")
            #MAIN TABLE FRAME SECTION
            frameMainTbl = Frame(self.mainFrame)
            frameMainTbl.grid(row=0, column=0, rowspan=2)
            frameFormDftr = Frame(self.mainFrame)
            frameFormDftr.grid(row=0, column=1, padx=10, pady=10, rowspan=2)
            frameBtDet = Frame(self.mainFrame)
            frameBtDet.grid(row=2, column=1, padx=10, pady=10)
            frameOperator = Frame(self.mainFrame)
            frameOperator.grid(row=2, column=0, padx=10, pady=10)
            headerTabel = ['No', 'Kode', 'Nama', 'Opsi']
            mainTblHeader1 = Label(frameMainTbl, text=headerTabel[0], font="12", width="4")
            mainTblHeader1.grid(row=0, column=0)
            mainTblHeader2 = Label(frameMainTbl, text=headerTabel[1], font="12", width="10")
            mainTblHeader2.grid(row=0, column=1)
            mainTblHeader3 = Label(frameMainTbl, text=headerTabel[2], font="12", width="45")
            mainTblHeader3.grid(row=0, column=2)
            mainTblHeader4 = Label(frameMainTbl, text=headerTabel[3], font="12", width="6")
            mainTblHeader4.grid(row=0, column=3, columnspan=3)
            self.mainTblContain1 = []
            self.mainTblContain2 = []
            self.mainTblContain3 = []
            for i in range(1,11):
                self.mainTblContain1.append(Label(frameMainTbl, font="12", width="4"))
                self.mainTblContain2.append(Label(frameMainTbl, font="12", width="10"))
                self.mainTblContain3.append(Label(frameMainTbl, font="12", width="45"))
                self.mainTblContain1[-1].grid(row=i, column=0)
                self.mainTblContain2[-1].grid(row=i, column=1)
                self.mainTblContain3[-1].grid(row=i, column=2)
            self.mainTbl1Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl2Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl3Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl4Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl5Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl6Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl7Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl8Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl9Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl10Contain4 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl1Contain4.grid(row=1, column=3)
            self.mainTbl2Contain4.grid(row=2, column=3)
            self.mainTbl3Contain4.grid(row=3, column=3)
            self.mainTbl4Contain4.grid(row=4, column=3)
            self.mainTbl5Contain4.grid(row=5, column=3)
            self.mainTbl6Contain4.grid(row=6, column=3)
            self.mainTbl7Contain4.grid(row=7, column=3)
            self.mainTbl8Contain4.grid(row=8, column=3)
            self.mainTbl9Contain4.grid(row=9, column=3)
            self.mainTbl10Contain4.grid(row=10, column=3)
            self.mainTbl1Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl2Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl3Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl4Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl5Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl6Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl7Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl8Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl9Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl10Contain5 = Button(frameMainTbl, font="12", width="2", bg="#FFFFFF")
            self.mainTbl1Contain5.grid(row=1, column=4)
            self.mainTbl2Contain5.grid(row=2, column=4)
            self.mainTbl3Contain5.grid(row=3, column=4)
            self.mainTbl4Contain5.grid(row=4, column=4)
            self.mainTbl5Contain5.grid(row=5, column=4)
            self.mainTbl6Contain5.grid(row=6, column=4)
            self.mainTbl7Contain5.grid(row=7, column=4)
            self.mainTbl8Contain5.grid(row=8, column=4)
            self.mainTbl9Contain5.grid(row=9, column=4)
            self.mainTbl10Contain5.grid(row=10, column=4)
            self.searchBar = Entry(frameMainTbl)
            self.searchBar.grid(row=11, column=0, sticky="W", padx=8)
            btnSearch = Button(frameMainTbl, text="Cari", command=self.searchDataMatkul)
            btnSearch.grid(row=11, column=1, sticky="W")
            self.mainPageNumber = 1
            self.mainTblPaging1 = Button(frameMainTbl, text="<", command=lambda:self.mainChangePage('prev', 3))
            self.mainTblPaging1.grid(row=11, column=2, sticky="E")
            self.mainTblPage = Label(frameMainTbl, text=str(self.mainPageNumber))
            self.mainTblPage.grid(row=11, column=3)
            self.mainTblPaging2 = Button(frameMainTbl, text=">", command=lambda:self.mainChangePage('next', 3))
            self.mainTblPaging2.grid(row=11, column=4, sticky="W")
            #FORM FRAME SECTION
            sql = "SELECT id, nama FROM dosen_pengajar"
            csr.execute(sql)
            self.dosens = np.array(csr.fetchall())
            labelNama = Label(frameFormDftr, font="12", width="10", text="Nama")
            labelNama.grid(row=1, column=0, padx=5, pady=3)
            self.nama = StringVar(value="")
            entryNama = Entry(frameFormDftr, font="12", textvariable=self.nama, width="20")
            entryNama.grid(row=1, column=1, columnspan=2, padx=4, pady=3)
            labelKode = Label(frameFormDftr, font="12", width="10", text="Kode")
            labelKode.grid(row=2, column=0, padx=3, pady=3)
            self.kode = StringVar(value="")
            entryKode = Entry(frameFormDftr, font="12", textvariable=self.kode, width="20")
            entryKode.grid(row=2, column=1, columnspan=2, padx=4, pady=3)
            labelDosen = Label(frameFormDftr, font="12", width="10", text="Dosen")
            labelDosen.grid(row=3, column=0, padx=3, pady=3)
            self.dosen = StringVar(value="Pilih Dosen")
            OpmDosen = OptionMenu(frameFormDftr, self.dosen, *self.dosens[:,1])
            OpmDosen.grid(row=3, column=1, columnspan=2, padx=4, pady=3)
            self.btnBuatAbsensi = Button(frameFormDftr, text="")
            self.btnBuatAbsensi.grid(row=4, column=0)
            self.btnSave = Button(frameFormDftr, text="Simpan", command=self.saveDataMatkul)
            self.btnSave.grid(row=4, column=1, columnspan=2)
            self.writeToTableMatkul(self.tempData[:10])
            
    def buatAbsensi(self, matkulId, dosId):
        sql = "SELECT id FROM mata_kuliah WHERE kode = %s"
        csr.execute(sql, (str(matkulId),))
        self.matkul_id = csr.fetchone()[0]
        self.dosId = dosId
        sql = "SELECT * FROM mahasiswa"
        csr.execute(sql)
        temp = np.array(csr.fetchall())
        if len(temp) > 0:
            self.tempData = temp[:, 1:]
            mhsId = np.array(temp[:,0].flatten(), dtype=int)
        else:
            self.tempData = []
            mhsId = []
        sql = "SELECT mhs_id FROM absensi WHERE matkul_id = %s"
        csr.execute(sql, (int(self.matkul_id),))
        mhs = np.array(csr.fetchall()).flatten()
        idxs = []
        for i in range(len(mhs)):
            idxs.append(np.argwhere(mhsId == mhs[i])[0,0])
        self.tempData = np.delete(self.tempData, idxs, 0)
        self.writeToTableAbsensi(self.tempData[:10])
        self.mainPageNumber = 1
        self.mainTblPaging1.config(command=lambda:self.mainChangePage('prev', 4))
        self.mainTblPaging2.config(command=lambda:self.mainChangePage('next', 4))
        self.btnBuatAbsensi.config(text="Lihat Absen", command=self.lihatAbsen)
        self.btnSave.config(text="Commit", command=lambda:self.tampilFrame(3))
    
    def mainChangePage(self, to, frameId):
        if to == 'prev':
            if self.mainPageNumber > 1:
                self.mainPageNumber -= 1
                if frameId == 1:
                    self.writeToTable(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
                elif frameId == 2:
                    self.writeToTableDosen(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
                elif frameId == 3:
                    self.writeToTableMatkul(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
                elif frameId == 4:
                    self.writeToTableAbsensi(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
                elif frameId == 5:
                    self.writeToTableAbsen(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
                self.mainTblPage.config(text=str(self.mainPageNumber))
        else:
            if len(self.tempData) > self.mainPageNumber*10:
                self.mainPageNumber += 1
                if frameId == 1:
                    self.writeToTable(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
                elif frameId == 2:
                    self.writeToTableDosen(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
                elif frameId == 3:
                    self.writeToTableMatkul(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
                elif frameId == 4:
                    self.writeToTableAbsensi(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
                elif frameId == 5:
                    self.writeToTableAbsen(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
                self.mainTblPage.config(text=str(self.mainPageNumber))
    
    def btChangePage(self, to):
        if to == 'prev':
            if self.btPages > 1:
                self.btPages -= 1
                dataBt = self.nearby_devices[(self.btPages - 1) * 5 : self.btPages * 5]
                self.renderScannedBluetooth(dataBt)
        else:
            if len(self.nearby_devices) > 5 * self.btPages:
                dataBt = self.nearby_devices[self.btPages * 5 : (self.btPages + 1) * 5]
                self.renderScannedBluetooth(dataBt)
                self.btPages += 1
        
    def browse(self):
        self.path = filedialog.askopenfilename()
        if len(self.path) > 0:
            self.ambilImg()
            self.imgShow(self.img)
            
    def ambilImg(self):
        w = 100
        h = 130
        self.img = cv2.resize(cv2.imread(self.path), (w, h))
        
    def saveImg(self, nim):
        path = 'Data Mahasiswa/Foto Profil/' + nim + '.jpg'
        cv2.imwrite(path, self.img)
        
    def saveImgDosen(self, nip):
        path = 'Data Dosen/Foto Profil/' + nip + '.jpg'
        cv2.imwrite(path, self.img)
            
    def imgShow(self, image):
        image_show = Image.fromarray(image[:,:,::-1])
        image_show = ImageTk.PhotoImage(image_show)
        self.btnPhoto.config(image=image_show)
        self.btnPhoto.image = image_show
    
    def scanBluetooth(self):
        self.nearby_devices = bluetooth.discover_devices(lookup_names=True)
        if len(self.nearby_devices) > 0:
            if len(self.nearby_devices) <=5:
                self.renderScannedBluetooth(self.nearby_devices)
            else:
                self.renderScannedBluetooth(self.nearby_devices[:5])
        else:
            messagebox.showinfo("Message", "Tidak ada bluetooth device terdeteksi di area anda.")
            
    def renderScannedBluetooth(self, data):
        self.clearScannedBluetooth()
        i = len(data)
        if i>0:
            self.bt1Cols1.config(text=data[0][0])
            self.bt1Cols2.config(text=data[0][1])
            self.bt1Cols3.config(text="+", command=lambda:self.printToMAC(data[0][0]))
        i-=1
        if i>0:
            self.bt2Cols1.config(text=data[1][0])
            self.bt2Cols2.config(text=data[1][1])
            self.bt2Cols3.config(text="+", command=lambda:self.printToMAC(data[1][0]))
        i-=1
        if i>0:
            self.bt3Cols1.config(text=data[2][0])
            self.bt3Cols2.config(text=data[2][1])
            self.bt3Cols3.config(text="+", command=lambda:self.printToMAC(data[2][0]))
        i-=1
        if i>0:
            self.bt4Cols1.config(text=data[3][0])
            self.bt4Cols2.config(text=data[3][1])
            self.bt4Cols3.config(text="+", command=lambda:self.printToMAC(data[3][0]))
        i-=1
        if i>0:
            self.bt5Cols1.config(text=data[4][0])
            self.bt5Cols2.config(text=data[4][1])
            self.bt5Cols3.config(text="+", command=lambda:self.printToMAC(data[4][0]))
            
    def printToMAC(self, addr):
        self.BtAddr.set(addr)
    
    def saveData(self):
        nama = self.nama.get()
        nim = self.NIM.get()
        password = self.passw.get()
        nohp = self.NoHP.get()
        btaddr = self.BtAddr.get()
        fakultas = self.fakultas.get()
        jurusan = self.jurusan.get()
        angkatan = self.angkatan.get()
        img_path = 'Data Mahasiswa/Foto Profil/'+nim+'.jpg'
        if nama != "" and nim != "" and nohp != "" and btaddr != "" and fakultas != "" and jurusan != "" and angkatan != "" and password != "":
            #CREATE
            password = hashlib.md5(password.encode('utf-8')).hexdigest()
            data = (nim, nama, nohp, btaddr, fakultas, jurusan, int(angkatan), img_path)
            sql = "INSERT INTO mahasiswa (nim, nama, no_telp, mac_addr, fakultas, jurusan, angkatan, img_path) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            csr.execute(sql, data)
            db.commit()
            sql = "SELECT id FROM mahasiswa WHERE nim = %s"
            csr.execute(sql, (nim,))
            idmhs = csr.fetchone()[0]
            sql = "INSERT INTO user (mhs_dos_id, username, password, role) VALUES (%s, %s, %s, %s)"
            csr.execute(sql, (idmhs, nim, password, 'mahasiswa'))
            db.commit()
            self.saveImg(nim)
            #READ
            sql = "SELECT * FROM mahasiswa"
            csr.execute(sql)
            self.tempData = np.array(csr.fetchall())[:,1:]
            self.writeToTable(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
            self.clearForm()
            
    def saveDataDosen(self):
        nama = self.nama.get()
        nip = self.NIP.get()
        nohp = self.NoHP.get()
        fakultas = self.fakultas.get()
        jurusan = self.jurusan.get()
        img_path = 'Data Dosen/Foto Profil/'+nip+'.jpg'
        username = self.username.get()
        password = self.passw.get()
        if nama != "" and nip != "" and nohp != "" and fakultas != "" and jurusan != "" and username != "" and password != "" :
            #CREATE
            password = hashlib.md5(password.encode('utf-8')).hexdigest()
            data = (nip, nama, nohp, fakultas, jurusan, img_path)
            sql = "INSERT INTO dosen_pengajar (nip, nama, no_telp, fakultas, jurusan, img_path) VALUES (%s, %s, %s, %s, %s, %s)"
            csr.execute(sql, data)
            db.commit()
            self.saveImgDosen(nip)
            sql = "SELECT id FROM dosen_pengajar WHERE nip = %s"
            csr.execute(sql, (nip,))
            iddos = csr.fetchone()[0]
            sql = "INSERT INTO user (mhs_dos_id, username, password, role) VALUES (%s, %s, %s, %s)"
            csr.execute(sql, (iddos, username, password, 'dosen'))
            db.commit()
            #READ
            sql = "SELECT * FROM dosen_pengajar"
            csr.execute(sql)
            self.tempData = np.array(csr.fetchall())[:,1:]
            self.writeToTableDosen(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
            self.clearFormDosen()
            
    def saveDataMatkul(self):
        nama = self.nama.get()
        kode = self.kode.get()
        dosen = self.dosen.get()
        if nama != "" and kode != "" and dosen != "Pilih Dosen":
            #CREATE
            dosId = self.dosens[np.where(self.dosens[:, 1] == dosen)[0][0],0]
            data = (kode, nama, int(dosId))
            sql = "INSERT INTO mata_kuliah (kode, nama, id_dosen) VALUES (%s, %s, %s)"
            csr.execute(sql, data)
            db.commit()
            #READ
            sql = "SELECT * FROM mata_kuliah"
            csr.execute(sql)
            self.tempData = np.array(csr.fetchall())[:,1:]
            self.writeToTableMatkul(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
            self.clearFormMatkul()
        
    def searchData(self):
        sql = "SELECT * FROM mahasiswa WHERE nim LIKE '"+self.searchBar.get()+"%'"
        csr.execute(sql)
        self.tempData = np.array(csr.fetchall())
        if len(self.tempData) > 0:
            self.tempData = self.tempData[:, 1:]
        self.writeToTable(self.tempData[0:10])
        
    def searchDataDosen(self):
        sql = "SELECT * FROM dosen_pengajar WHERE nama LIKE '"+self.searchBar.get()+"%'"
        csr.execute(sql)
        self.tempData = np.array(csr.fetchall())
        if len(self.tempData) > 0:
            self.tempData = self.tempData[:, 1:]
        self.writeToTable(self.tempData[0:10])
        
    def searchDataMatkul(self):
        sql = "SELECT * FROM mata_kuliah WHERE nama LIKE '"+self.searchBar.get()+"%'"
        csr.execute(sql)
        self.tempData = np.array(csr.fetchall())
        if len(self.tempData) > 0:
            self.tempData = self.tempData[:, 1:]
        self.writeToTable(self.tempData[0:10])
    
    def showDataOnForm(self, data):
        self.NIM.set(data[0])
        self.nama.set(data[1])
        self.NoHP.set(data[2])
        self.BtAddr.set(data[3])
        self.fakultas.set(data[4])
        self.jurusan.set(data[5])
        self.angkatan.set(str(data[6]))
        self.path = data[7]
        self.ambilImg()
        self.imgShow(self.img)
        self.passw.set("")
        sql = "SELECT id FROM mahasiswa WHERE nim = %s"
        csr.execute(sql, (self.NIM.get(),))
        idmhs = csr.fetchone()[0]
        self.btnSave.config(text="Ubah", command=lambda:self.updateData(idmhs))
    
    def showDataOnFormDosen(self, data):
        self.NIP.set(data[0])
        self.nama.set(data[1])
        self.NoHP.set(data[2])
        self.fakultas.set(data[4])
        self.jurusan.set(data[3])
        self.path = data[5]
        self.ambilImg()
        self.imgShow(self.img)
        self.passw.set("")
        sql = "SELECT id FROM dosen_pengajar WHERE nip = %s"
        csr.execute(sql, (self.NIP.get(),))
        iddos = csr.fetchone()[0]
        self.btnSave.config(text="Ubah", command=lambda:self.updateDataDosen(iddos))
        
    def showDataOnFormMatkul(self, data):
        self.kode.set(data[0])
        self.nama.set(data[1])
        dosName = self.dosens[np.where(self.dosens[:, 0] == data[2])[0][0],1]
        self.dosen.set(dosName)
        self.btnSave.config(text="Ubah", command=self.updateDataMatkul)
        self.btnBuatAbsensi.config(command=lambda:self.buatAbsensi(data[0], data[2]), text="Buat Absensi")
        
    def updateData(self, idmhs):
        nim = self.NIM.get()
        nama = self.nama.get()
        nohp = self.NoHP.get()
        btaddr = self.BtAddr.get()
        fakultas = self.fakultas.get()
        jurusan = self.jurusan.get()
        angkatan = self.angkatan.get()
        password = self.passw.get()
        img_path = 'Data Mahasiswa/Foto Profil/'+nim+'.jpg'
        if nama != "" and nim != "" and nohp != "" and btaddr != "" and fakultas != "" and jurusan != "" and angkatan != "" and password != "":
            password = hashlib.md5(self.passw.get().encode('utf-8')).hexdigest()
            sql = "UPDATE mahasiswa SET nim = %s, nama = %s, no_telp = %s, mac_addr = %s, fakultas = %s, jurusan = %s, angkatan = %s, img_path = %s WHERE nim = %s"
            csr.execute(sql, (nim, nama, nohp, btaddr, fakultas, jurusan, int(angkatan), img_path, nim))
            db.commit()
            sql = "UPDATE user u INNER JOIN mahasiswa m ON m.id = u.mhs_dos_id SET u.username = %s, u.password = %s, u.role = %s WHERE m.id = %s"
            csr.execute(sql, (nim, password, 'mahasiswa', idmhs))
            db.commit()
            self.saveImg(nim)
        self.clearForm()
        sql = "SELECT * FROM mahasiswa"
        csr.execute(sql)
        temp = np.array(csr.fetchall())
        if len(temp) > 0:
            self.tempData = temp[:,1:]
        else:
            self.tempData = []
        self.writeToTable(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
    
    def updateDataDosen(self, iddos):
        nip = self.NIP.get()
        nama = self.nama.get()
        nohp = self.NoHP.get()
        fakultas = self.fakultas.get()
        jurusan = self.jurusan.get()
        img_path = 'Data Dosen/Foto Profil/'+nip+'.jpg'
        username = self.username.get()
        password = self.passw.get()
        if nama != "" and nip != "" and nohp != "" and fakultas != "" and username != "" and jurusan != "":
            password = hashlib.md5(password.encode('utf-8')).hexdigest()
            sql = "UPDATE dosen_pengajar SET nip = %s, nama = %s, no_telp = %s, fakultas = %s, jurusan = %s, img_path = %s WHERE id = %s"
            csr.execute(sql, (nip, nama, nohp, fakultas, jurusan, img_path, iddos))
            db.commit()
            sql = "UPDATE user u INNER JOIN dosen_pengajar d ON d.id = u.mhs_dos_id SET u.username = %s, u.password = %s, u.role = %s  WHERE d.id = %s"
            csr.execute(sql, (username, password, 'dosen', iddos))
            db.commit()
            self.saveImgDosen(nip)
        self.clearFormDosen()
        sql = "SELECT * FROM dosen_pengajar"
        csr.execute(sql)
        temp = np.array(csr.fetchall())
        if len(temp) > 0:
            self.tempData = temp[:,1:]
        else:
            self.tempData = []
        self.writeToTableDosen(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
        
    def updateDataMatkul(self):
        kode = self.kode.get()
        nama = self.nama.get()
        dosen = self.dosen.get()
        if nama != "" and kode != "" and dosen != "Pilih Dosen":
            dosId = self.dosens[np.where(self.dosens[:, 1] == dosen)[0][0],0]
            sql = "UPDATE mata_kuliah SET kode = %s, nama = %s, id_dosen = %s WHERE kode = %s"
            csr.execute(sql, (kode, nama, int(dosId), kode))
            db.commit()
        self.clearFormMatkul()
        sql = "SELECT * FROM mata_kuliah"
        csr.execute(sql)
        temp = np.array(csr.fetchall())
        if len(temp) > 0:
            self.tempData = temp[:,1:]
        else:
            self.tempData = []
        self.writeToTableMatkul(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
    
    def clearForm(self):
        self.path = 'konden mepoto.jpg'
        self.ambilImg()
        self.imgShow(self.img)
        self.nama.set("")
        self.NIM.set("")
        self.NoHP.set("")
        self.BtAddr.set("")
        self.passw.set("")
        self.btnSave.config(text="Simpan", command=self.saveData)
        
    def clearFormDosen(self):
        self.path = 'konden mepoto.jpg'
        self.ambilImg()
        self.imgShow(self.img)
        self.nama.set("")
        self.NIP.set("")
        self.NoHP.set("")
        self.username.set("")
        self.passw.set("")
        self.btnSave.config(text="Simpan", command=self.saveDataDosen)
        
    def clearFormMatkul(self):
        self.nama.set("")
        self.kode.set("")
        self.dosen.set("Pilih Dosen")
        self.btnSave.config(text="Simpan", command=self.saveDataMatkul)
    
    def clearMainTable(self):
        for i in range(10):
            self.mainTblContain1[i].config(text="")
            self.mainTblContain2[i].config(text="")
            self.mainTblContain3[i].config(text="")
        self.mainTbl1Contain4.config(text="", command="", bg="#FFFFFF")
        self.mainTbl1Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl2Contain4.config(text="", command="", bg="#FFFFFF")
        self.mainTbl2Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl3Contain4.config(text="", command="", bg="#FFFFFF")
        self.mainTbl3Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl4Contain4.config(text="", command="", bg="#FFFFFF")
        self.mainTbl4Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl5Contain4.config(text="", command="", bg="#FFFFFF")
        self.mainTbl5Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl6Contain4.config(text="", command="", bg="#FFFFFF")
        self.mainTbl6Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl7Contain4.config(text="", command="", bg="#FFFFFF")
        self.mainTbl7Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl8Contain4.config(text="", command="", bg="#FFFFFF")
        self.mainTbl8Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl9Contain4.config(text="", command="", bg="#FFFFFF")
        self.mainTbl9Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl10Contain4.config(text="", command="", bg="#FFFFFF")
        self.mainTbl10Contain5.config(text="", command="", bg="#FFFFFF")
    
    def clearScannedBluetooth(self):
        self.bt1Cols1.config(text="")
        self.bt2Cols1.config(text="")
        self.bt3Cols1.config(text="")
        self.bt4Cols1.config(text="")
        self.bt5Cols1.config(text="")
        self.bt1Cols2.config(text="")
        self.bt2Cols2.config(text="")
        self.bt3Cols2.config(text="")
        self.bt4Cols2.config(text="")
        self.bt5Cols2.config(text="")
        self.bt1Cols3.config(text="", command=lambda:self.printToMAC(""))
        self.bt2Cols3.config(text="", command=lambda:self.printToMAC(""))
        self.bt3Cols3.config(text="", command=lambda:self.printToMAC(""))
        self.bt4Cols3.config(text="", command=lambda:self.printToMAC(""))
        self.bt5Cols3.config(text="", command=lambda:self.printToMAC(""))
    
    def deleteTempData(self, data):
        sql = "DELETE a, m FROM absensi a INNER JOIN mahasiswa m ON m.id = a.mhs_id WHERE m.nim = %s"
        csr.execute(sql, (str(data[0]),))
        db.commit()
        sql = "DELETE FROM mahasiswa WHERE nim = %s"
        csr.execute(sql, (str(data[0]),))
        db.commit()
        sql = "SELECT * FROM mahasiswa"
        csr.execute(sql)
        temp = np.array(csr.fetchall())
        if len(temp) > 0:
            self.tempData = temp[:,1:]
        else:
            self.tempData = []
        self.writeToTable(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
        
    def deleteTempDataDosen(self, data):
        sql = "DELETE a, d FROM absensi a INNER JOIN dosen_pengajar d ON d.id = a.dos_id WHERE nip = %s"
        csr.execute(sql, (str(data[0]),))
        db.commit()
        sql = "DELETE FROM dosen_pengajar WHERE nip = %s"
        csr.execute(sql, (str(data[0]),))
        db.commit()
        sql = "SELECT * FROM dosen_pengajar"
        csr.execute(sql)
        temp = np.array(csr.fetchall())
        if len(temp) > 0:
            self.tempData = temp[:,1:]
        else:
            self.tempData = []
        self.writeToTableDosen(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
        
    def deleteTempDataMatkul(self, data):
        sql = "DELETE a, m FROM absensi a INNER JOIN mata_kuliah k ON k.id = a.matkul_id WHERE k.kode = %s"
        csr.execute(sql, (str(data[0]),))
        db.commit()
        sql = "DELETE FROM mata_kuliah WHERE kode = %s"
        csr.execute(sql, (str(data[0]),))
        db.commit()
        sql = "SELECT * FROM mata_kuliah"
        csr.execute(sql)
        temp = np.array(csr.fetchall())
        if len(temp) > 0:
            self.tempData = temp[:,1:]
        else:
            self.tempData = []
        self.writeToTableMatkul(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
    
    def writeToTable(self, data):
        self.clearMainTable()
        if len(data) % 10 != 0:
            for i in range(len(data)):
                self.mainTblContain1[i].config(text=str((self.mainPageNumber-1)*10+i+1))
                self.mainTblContain2[i].config(text=data[i][0])
                self.mainTblContain3[i].config(text=data[i][1])
            j=0
            if j<=i:
                self.mainTbl1Contain4.config(text="e", command=lambda:self.showDataOnForm(data[0]), bg="#049723")
                self.mainTbl1Contain5.config(text="d", command=lambda:self.deleteTempData(data[0]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl2Contain4.config(text="e", command=lambda:self.showDataOnForm(data[1]), bg="#049723")
                self.mainTbl2Contain5.config(text="d", command=lambda:self.deleteTempData(data[1]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl3Contain4.config(text="e", command=lambda:self.showDataOnForm(data[2]), bg="#049723")
                self.mainTbl3Contain5.config(text="d", command=lambda:self.deleteTempData(data[2]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl4Contain4.config(text="e", command=lambda:self.showDataOnForm(data[3]), bg="#049723")
                self.mainTbl4Contain5.config(text="d", command=lambda:self.deleteTempData(data[3]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl5Contain4.config(text="e", command=lambda:self.showDataOnForm(data[4]), bg="#049723")
                self.mainTbl5Contain5.config(text="d", command=lambda:self.deleteTempData(data[4]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl6Contain4.config(text="e", command=lambda:self.showDataOnForm(data[5]), bg="#049723")
                self.mainTbl6Contain5.config(text="d", command=lambda:self.deleteTempData(data[5]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl7Contain4.config(text="e", command=lambda:self.showDataOnForm(data[6]), bg="#049723")
                self.mainTbl7Contain5.config(text="d", command=lambda:self.deleteTempData(data[6]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl8Contain4.config(text="e", command=lambda:self.showDataOnForm(data[7]), bg="#049723")
                self.mainTbl8Contain5.config(text="d", command=lambda:self.deleteTempData(data[7]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl9Contain4.config(text="e", command=lambda:self.showDataOnForm(data[8]), bg="#049723")
                self.mainTbl9Contain5.config(text="d", command=lambda:self.deleteTempData(data[8]), bg="#970423")
        else:
            for i in range(len(data)):
                self.mainTblContain1[i].config(text=str((self.mainPageNumber-1)*10+i+1))
                self.mainTblContain2[i].config(text=data[i][0])
                self.mainTblContain3[i].config(text=data[i][1])
            if len(data) > 0:
                j=0
                self.mainTbl1Contain4.config(text="e", command=lambda:self.showDataOnForm(data[0]), bg="#049723")
                self.mainTbl1Contain5.config(text="d", command=lambda:self.deleteTempData(data[0]), bg="#970423")
                j+=1
                self.mainTbl2Contain4.config(text="e", command=lambda:self.showDataOnForm(data[1]), bg="#049723")
                self.mainTbl2Contain5.config(text="d", command=lambda:self.deleteTempData(data[1]), bg="#970423")
                j+=1
                self.mainTbl3Contain4.config(text="e", command=lambda:self.showDataOnForm(data[2]), bg="#049723")
                self.mainTbl3Contain5.config(text="d", command=lambda:self.deleteTempData(data[2]), bg="#970423")
                j+=1
                self.mainTbl4Contain4.config(text="e", command=lambda:self.showDataOnForm(data[3]), bg="#049723")
                self.mainTbl4Contain5.config(text="d", command=lambda:self.deleteTempData(data[3]), bg="#970423")
                j+=1
                self.mainTbl5Contain4.config(text="e", command=lambda:self.showDataOnForm(data[4]), bg="#049723")
                self.mainTbl5Contain5.config(text="d", command=lambda:self.deleteTempData(data[4]), bg="#970423")
                j+=1
                self.mainTbl6Contain4.config(text="e", command=lambda:self.showDataOnForm(data[5]), bg="#049723")
                self.mainTbl6Contain5.config(text="d", command=lambda:self.deleteTempData(data[5]), bg="#970423")
                j+=1
                self.mainTbl7Contain4.config(text="e", command=lambda:self.showDataOnForm(data[6]), bg="#049723")
                self.mainTbl7Contain5.config(text="d", command=lambda:self.deleteTempData(data[6]), bg="#970423")
                j+=1
                self.mainTbl8Contain4.config(text="e", command=lambda:self.showDataOnForm(data[7]), bg="#049723")
                self.mainTbl8Contain5.config(text="d", command=lambda:self.deleteTempData(data[7]), bg="#970423")
                j+=1
                self.mainTbl9Contain4.config(text="e", command=lambda:self.showDataOnForm(data[8]), bg="#049723")
                self.mainTbl9Contain5.config(text="d", command=lambda:self.deleteTempData(data[8]), bg="#970423")
                j+=1
                self.mainTbl10Contain4.config(text="e", command=lambda:self.showDataOnForm(data[9]), bg="#049723")
                self.mainTbl10Contain5.config(text="d", command=lambda:self.deleteTempData(data[9]), bg="#970423")
                                              
    def writeToTableDosen(self, data):
        self.clearMainTable()
        if len(data) % 10 != 0:
            for i in range(len(data)):
                self.mainTblContain1[i].config(text=str((self.mainPageNumber-1)*10+i+1))
                self.mainTblContain2[i].config(text=data[i][0])
                self.mainTblContain3[i].config(text=data[i][1])
            j=0
            if j<=i:
                self.mainTbl1Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[0]), bg="#049723")
                self.mainTbl1Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[0]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl2Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[1]), bg="#049723")
                self.mainTbl2Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[1]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl3Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[2]), bg="#049723")
                self.mainTbl3Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[2]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl4Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[3]), bg="#049723")
                self.mainTbl4Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[3]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl5Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[4]), bg="#049723")
                self.mainTbl5Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[4]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl6Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[5]), bg="#049723")
                self.mainTbl6Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[5]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl7Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[6]), bg="#049723")
                self.mainTbl7Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[6]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl8Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[7]), bg="#049723")
                self.mainTbl8Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[7]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl9Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[8]), bg="#049723")
                self.mainTbl9Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[8]), bg="#970423")
        else:
            for i in range(len(data)):
                self.mainTblContain1[i].config(text=str((self.mainPageNumber-1)*10+i+1))
                self.mainTblContain2[i].config(text=data[i][0])
                self.mainTblContain3[i].config(text=data[i][1])
            if len(data) > 0:
                j=0
                self.mainTbl1Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[0]), bg="#049723")
                self.mainTbl1Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[0]), bg="#970423")
                j+=1
                self.mainTbl2Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[1]), bg="#049723")
                self.mainTbl2Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[1]), bg="#970423")
                j+=1
                self.mainTbl3Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[2]), bg="#049723")
                self.mainTbl3Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[2]), bg="#970423")
                j+=1
                self.mainTbl4Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[3]), bg="#049723")
                self.mainTbl4Contain5.config(text="d", command=lambda:self.deleteTempData(data[3]), bg="#970423")
                j+=1
                self.mainTbl5Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[4]), bg="#049723")
                self.mainTbl5Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[4]), bg="#970423")
                j+=1
                self.mainTbl6Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[5]), bg="#049723")
                self.mainTbl6Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[5]), bg="#970423")
                j+=1
                self.mainTbl7Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[6]), bg="#049723")
                self.mainTbl7Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[6]), bg="#970423")
                j+=1
                self.mainTbl8Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[7]), bg="#049723")
                self.mainTbl8Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[7]), bg="#970423")
                j+=1
                self.mainTbl9Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[8]), bg="#049723")
                self.mainTbl9Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[8]), bg="#970423")
                j+=1
                self.mainTbl10Contain4.config(text="e", command=lambda:self.showDataOnFormDosen(data[9]), bg="#049723")
                self.mainTbl10Contain5.config(text="d", command=lambda:self.deleteTempDataDosen(data[9]), bg="#970423")
                                              
    def writeToTableMatkul(self, data):
        self.clearMainTable()
        if len(data) % 10 != 0:
            for i in range(len(data)):
                self.mainTblContain1[i].config(text=str((self.mainPageNumber-1)*10+i+1))
                self.mainTblContain2[i].config(text=data[i][0])
                self.mainTblContain3[i].config(text=data[i][1])
            j=0
            if j<=i:
                self.mainTbl1Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[0]), bg="#049723")
                self.mainTbl1Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[0]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl2Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[1]), bg="#049723")
                self.mainTbl2Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[1]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl3Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[2]), bg="#049723")
                self.mainTbl3Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[2]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl4Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[3]), bg="#049723")
                self.mainTbl4Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[3]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl5Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[4]), bg="#049723")
                self.mainTbl5Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[4]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl6Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[5]), bg="#049723")
                self.mainTbl6Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[5]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl7Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[6]), bg="#049723")
                self.mainTbl7Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[6]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl8Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[7]), bg="#049723")
                self.mainTbl8Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[7]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl9Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[8]), bg="#049723")
                self.mainTbl9Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[8]), bg="#970423")
        else:
            for i in range(len(data)):
                self.mainTblContain1[i].config(text=str((self.mainPageNumber-1)*10+i+1))
                self.mainTblContain2[i].config(text=data[i][0])
                self.mainTblContain3[i].config(text=data[i][1])
            if len(data) > 0:
                j=0
                self.mainTbl1Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[0]), bg="#049723")
                self.mainTbl1Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[0]), bg="#970423")
                j+=1
                self.mainTbl2Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[1]), bg="#049723")
                self.mainTbl2Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[1]), bg="#970423")
                j+=1
                self.mainTbl3Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[2]), bg="#049723")
                self.mainTbl3Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[2]), bg="#970423")
                j+=1
                self.mainTbl4Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[3]), bg="#049723")
                self.mainTbl4Contain5.config(text="d", command=lambda:self.deleteTempData(data[3]), bg="#970423")
                j+=1
                self.mainTbl5Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[4]), bg="#049723")
                self.mainTbl5Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[4]), bg="#970423")
                j+=1
                self.mainTbl6Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[5]), bg="#049723")
                self.mainTbl6Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[5]), bg="#970423")
                j+=1
                self.mainTbl7Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[6]), bg="#049723")
                self.mainTbl7Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[6]), bg="#970423")
                j+=1
                self.mainTbl8Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[7]), bg="#049723")
                self.mainTbl8Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[7]), bg="#970423")
                j+=1
                self.mainTbl9Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[8]), bg="#049723")
                self.mainTbl9Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[8]), bg="#970423")
                j+=1
                self.mainTbl10Contain4.config(text="e", command=lambda:self.showDataOnFormMatkul(data[9]), bg="#049723")
                self.mainTbl10Contain5.config(text="d", command=lambda:self.deleteTempDataMatkul(data[9]), bg="#970423")
                                              
    def writeToTableAbsensi(self, data):
        self.clearMainTable()
        if len(data) % 10 != 0:
            for i in range(len(data)):
                self.mainTblContain1[i].config(text=str((self.mainPageNumber-1)*10+i+1))
                self.mainTblContain2[i].config(text=data[i][0])
                self.mainTblContain3[i].config(text=data[i][1])
            j=0
            if j<=i:
                self.mainTbl1Contain4.config(text="+", command=lambda:self.addToAbsen(data[0]), bg="#049723")
                self.mainTbl1Contain5.config(text="", command="", bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl2Contain4.config(text="+", command=lambda:self.addToAbsen(data[1]), bg="#049723")
                self.mainTbl2Contain5.config(text="", command="", bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl3Contain4.config(text="+", command=lambda:self.addToAbsen(data[2]), bg="#049723")
                self.mainTbl3Contain5.config(text="", command="", bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl4Contain4.config(text="+", command=lambda:self.addToAbsen(data[3]), bg="#049723")
                self.mainTbl4Contain5.config(text="", command="", bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl5Contain4.config(text="+", command=lambda:self.addToAbsen(data[4]), bg="#049723")
                self.mainTbl5Contain5.config(text="", command="", bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl6Contain4.config(text="+", command=lambda:self.addToAbsen(data[5]), bg="#049723")
                self.mainTbl6Contain5.config(text="", command="", bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl7Contain4.config(text="+", command=lambda:self.addToAbsen(data[6]), bg="#049723")
                self.mainTbl7Contain5.config(text="", command=lambda:self.deleteTempDataMatkul(data[6]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl8Contain4.config(text="+", command=lambda:self.addToAbsen(data[7]), bg="#049723")
                self.mainTbl8Contain5.config(text="", command="", bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl9Contain4.config(text="+", command=lambda:self.addToAbsen(data[8]), bg="#049723")
                self.mainTbl9Contain5.config(text="", command="", bg="#970423")
        else:
            for i in range(len(data)):
                self.mainTblContain1[i].config(text=str((self.mainPageNumber-1)*10+i+1))
                self.mainTblContain2[i].config(text=data[i][0])
                self.mainTblContain3[i].config(text=data[i][1])
            if len(data) > 0:
                j=0
                self.mainTbl1Contain4.config(text="+", command=lambda:self.addToAbsen(data[0]), bg="#049723")
                self.mainTbl1Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl2Contain4.config(text="+", command=lambda:self.addToAbsen(data[1]), bg="#049723")
                self.mainTbl2Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl3Contain4.config(text="+", command=lambda:self.addToAbsen(data[2]), bg="#049723")
                self.mainTbl3Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl4Contain4.config(text="+", command=lambda:self.addToAbsen(data[3]), bg="#049723")
                self.mainTbl4Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl5Contain4.config(text="+", command=lambda:self.addToAbsen(data[4]), bg="#049723")
                self.mainTbl5Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl6Contain4.config(text="+", command=lambda:self.addToAbsen(data[5]), bg="#049723")
                self.mainTbl6Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl7Contain4.config(text="+", command=lambda:self.addToAbsen(data[6]), bg="#049723")
                self.mainTbl7Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl8Contain4.config(text="+", command=lambda:self.addToAbsen(data[7]), bg="#049723")
                self.mainTbl8Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl9Contain4.config(text="+", command=lambda:self.addToAbsen(data[8]), bg="#049723")
                self.mainTbl9Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl10Contain4.config(text="+", command=lambda:self.addToAbsen(data[9]), bg="#049723")
                self.mainTbl10Contain5.config(text="", command="", bg="#970423")
                                              
    def writeToTableAbsen(self, data):
        self.clearMainTable()
        if len(data) % 10 != 0:
            for i in range(len(data)):
                self.mainTblContain1[i].config(text=str((self.mainPageNumber-1)*10+i+1))
                self.mainTblContain2[i].config(text=data[i][0])
                self.mainTblContain3[i].config(text=data[i][1])
            j=0
            if j<=i:
                self.mainTbl1Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[0]), bg="#049723")
                self.mainTbl1Contain5.config(text="", command="", bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl2Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[1]), bg="#049723")
                self.mainTbl2Contain5.config(text="", command="", bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl3Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[2]), bg="#049723")
                self.mainTbl3Contain5.config(text="", command="", bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl4Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[3]), bg="#049723")
                self.mainTbl4Contain5.config(text="", command="", bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl5Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[4]), bg="#049723")
                self.mainTbl5Contain5.config(text="", command="", bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl6Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[5]), bg="#049723")
                self.mainTbl6Contain5.config(text="", command="", bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl7Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[6]), bg="#049723")
                self.mainTbl7Contain5.config(text="", command=lambda:self.deleteTempDataMatkul(data[6]), bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl8Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[7]), bg="#049723")
                self.mainTbl8Contain5.config(text="", command="", bg="#970423")
            j+=1
            if j<=i:
                self.mainTbl9Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[8]), bg="#049723")
                self.mainTbl9Contain5.config(text="", command="", bg="#970423")
        else:
            for i in range(len(data)):
                self.mainTblContain1[i].config(text=str((self.mainPageNumber-1)*10+i+1))
                self.mainTblContain2[i].config(text=data[i][0])
                self.mainTblContain3[i].config(text=data[i][1])
            if len(data) > 0:
                j=0
                self.mainTbl1Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[0]), bg="#049723")
                self.mainTbl1Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl2Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[1]), bg="#049723")
                self.mainTbl2Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl3Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[2]), bg="#049723")
                self.mainTbl3Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl4Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[3]), bg="#049723")
                self.mainTbl4Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl5Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[4]), bg="#049723")
                self.mainTbl5Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl6Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[5]), bg="#049723")
                self.mainTbl6Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl7Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[6]), bg="#049723")
                self.mainTbl7Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl8Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[7]), bg="#049723")
                self.mainTbl8Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl9Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[8]), bg="#049723")
                self.mainTbl9Contain5.config(text="", command="", bg="#970423")
                j+=1
                self.mainTbl10Contain4.config(text="-", command=lambda:self.deleteFromAbsen(data[9]), bg="#049723")
                self.mainTbl10Contain5.config(text="", command="", bg="#970423")
                                              
    def addToAbsen(self, data):
        sql = "SELECT id FROM mahasiswa WHERE nim = %s"
        csr.execute(sql, (str(data[0]),))
        temp = csr.fetchone()[0]
        sql = "INSERT INTO absensi (matkul_id, dos_id, mhs_id, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (int(self.matkul_id), int(self.dosId), int(temp), "", "", "", "", "", "", "", "", "", "", "", "")
        csr.execute(sql, values)
        db.commit()
        tempIdx = np.argwhere(self.tempData[:, 0] == data[0])[0,0]
        self.tempData = np.delete(self.tempData, tempIdx, axis=0)
        self.writeToTableAbsensi(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
        
    def deleteFromAbsen(self, data):
        sql = "SELECT id FROM mahasiswa WHERE nim = %s"
        csr.execute(sql, (str(data[0]),))
        temp = csr.fetchone()[0]
        sql = "DELETE FROM absensi WHERE mhs_id = %s AND matkul_id = %s"
        values = (int(temp), int(self.matkul_id))
        csr.execute(sql, values)
        db.commit()
        tempIdx = np.argwhere(self.tempData[:, 0] == data[0])[0,0]
        self.tempData = np.delete(self.tempData, tempIdx, axis=0)
        self.writeToTableAbsen(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
        
    def lihatAbsen(self):
        self.btnTabMhs.config(bg="#ffffff")
        self.btnTabDos.config(bg="#ffffff")
        self.btnTabMtk.config(bg="#ffffff")
        self.btnTabAbs.config(bg="#5adced")
        sql = "SELECT mhs_id FROM absensi WHERE matkul_id = %s"
        csr.execute(sql, (int(self.matkul_id),))
        temp = np.array(csr.fetchall())
        self.tempData = []
        for t in temp:
            sql = "SELECT * FROM mahasiswa WHERE id = %s"
            csr.execute(sql, (int(t),))
            self.tempData.append(csr.fetchone()[1:])
        self.tempData = np.array(self.tempData)
        self.writeToTableAbsen(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
        sql = "SELECT kode FROM mata_kuliah WHERE id = %s"
        csr.execute(sql, (int(self.matkul_id),))
        matkulId = csr.fetchone()[0]
        self.btnBuatAbsensi.config(text="Kembali", command=lambda:self.buatAbsensi(matkulId, self.dosId))
        self.mainTblPaging1.config(command=lambda:self.mainChangePage('prev', 5))
        self.mainTblPaging2.config(command=lambda:self.mainChangePage('next', 5))
        
Main(root, "== Pendaftaran ==")
root.mainloop()