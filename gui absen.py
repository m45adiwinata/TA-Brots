# -*- coding: utf-8 -*-
"""
Created on Wed Jul 03 21:30:29 2019

@author: bhaskaraby
"""

from tkinter import Button, Frame, Label, OptionMenu, StringVar, Tk, Entry, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
import os
import bluetooth
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
        self.master.config(background="#0000F8")
        pImgs = 'Data Mahasiswa/Foto Profil/'
        self.loginPage()
        #self.komponenMain()
        self.profileImgs = np.array([os.path.join(pImgs,fname) for fname in os.listdir(pImgs)])
        self.toogleState = 0
        self.path = 'konden mepoto.jpg'
        self.ambilImg()
        #self.imgShow(self.img)
        self.fDataIdx = []
        
    def clearMaster(self):
        self.frameInput.destroy()
    
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
    
    def komponenMain(self):
        sql = "SELECT d.id, d.nama FROM dosen_pengajar d INNER JOIN user u ON d.id = u.mhs_dos_id WHERE u.username = %s"
        csr.execute(sql, (self.username.get(),))
        dos = np.array(csr.fetchone(), dtype=str)
        self.dosId = dos[0]
        self.dosNama = dos[1]
        frameDaftarAbsen = Frame(self.master, bg="#0000F8")
        frameDaftarAbsen.grid(row=0, column=0, padx=8, pady=5)
        framePreview = Frame(self.master, bg="#970423")
        framePreview.grid(row=1, column=0, padx=8, pady=5)
        frameOpAbsen = Frame(self.master, bg="#239704")
        frameOpAbsen.grid(row=2, column=0, padx=8, pady=5)
        frameTblAbsensi = Frame(self.master)
        frameTblAbsensi.grid(row=0, column=1, padx=8, pady=5, rowspan=3)
        
        self.image_empty = Image.open("konden mepoto.jpg")
        self.image_empty = ImageTk.PhotoImage(self.image_empty)
        
        sql = "SELECT m.nama, m.kode FROM mata_kuliah m INNER JOIN absensi a ON m.id = a.matkul_id WHERE a.dos_id = %s"
        csr.execute(sql, (str(self.dosId),))
        result = np.array(csr.fetchall(), dtype=str)
        matkuls = np.unique(result[:,0])
        self.matkul = StringVar(value="Pilih Mata Kuliah")
        opmSelectMatkul = OptionMenu(frameDaftarAbsen, self.matkul, *matkuls)
        opmSelectMatkul.grid(row=0, column=0)
        pertemuan = []
        for i in range(1,13):
            pertemuan.append('Pertemuan %s' % i)
        self.pertemuan = StringVar(value="Pilih Pertemuan")
        opmSelectPert = OptionMenu(frameDaftarAbsen, self.pertemuan, *pertemuan)
        opmSelectPert.grid(row=0, column=1)
        btnBrowseData = Button(frameDaftarAbsen, width="10", height="2", text="Masukkan\nDaftar\nAbsen", font="Arial 10", command=self.browse)
        btnBrowseData.grid(row=0, column=2, padx=4, pady=4)
        self.lblNamaDaftar = Label(frameDaftarAbsen, width="20", bg="#0000F8")
        self.lblNamaDaftar.grid(row=1, column=0, padx=4, pady=2)
        
        self.lblPrevFoto = Label(framePreview, width="100", height="130", image=self.image_empty)
        self.lblPrevFoto.grid(row=0, column=0, rowspan=4)
        lblNama = Label(framePreview, width="5", font="12", text="Nama", bg="#970423")
        lblNama.grid(row=0, column=1, padx=4, pady=3, sticky="W")
        lblNIM = Label(framePreview, width="5", font="12", text="NIM", bg="#970423")
        lblNIM.grid(row=1, column=1, padx=4, pady=3, sticky="W")
        lblNoHP = Label(framePreview, width="5", font="12", text="No HP", bg="#970423")
        lblNoHP.grid(row=2, column=1, padx=4, pady=3, sticky="W")
        self.lblNamaMhs = Label(framePreview, width="10", font="12", text="", bg="#970423")
        self.lblNamaMhs.grid(row=0, column=2, pady=3, sticky="W")
        self.lblNIMMhs = Label(framePreview, width="10", font="12", text="", bg="#970423")
        self.lblNIMMhs.grid(row=1, column=2, pady=3, sticky="W")
        self.lblNoHPMhs = Label(framePreview, width="10", font="12", text="", bg="#970423")
        self.lblNoHPMhs.grid(row=2, column=2, pady=3, sticky="W")
        self.selected = StringVar(value="Keterangan")
        self.keteranganMhs = OptionMenu(framePreview, self.selected, "Hadir", "Tidak Hadir")
        self.keteranganMhs.grid(row=3, column=1, pady=3, padx=4, columnspan=2, sticky="W")
        self.btnSimpan = Button(framePreview, text="Simpan")
        self.btnSimpan.grid(row=4, column=2, pady=3, padx=4)
        
        mainTblKop = Label(frameTblAbsensi, text="Daftar Nama Mahasiswa", font="Arial 20 bold")
        mainTblKop.grid(row=0, column=0, columnspan=7, sticky="N", pady=5)
        self.namaMatKul = Label(frameTblAbsensi, text="Mata Kuliah : ", font="12")
        self.namaMatKul.grid(row=1, column=0, columnspan=7, sticky="E")
        self.lblNamaDosen = Label(frameTblAbsensi, text="Dosen Pengajar : ", font="12")
        self.lblNamaDosen.grid(row=2, column=0, columnspan=7, sticky="E", pady=3)
        headerTabel = ['No', 'NIM', 'Nama', 'Keterangan', 'Opsi']
        mainTblHeader1 = Label(frameTblAbsensi, text=headerTabel[0], font="12", width="4")
        mainTblHeader1.grid(row=3, column=0)
        mainTblHeader2 = Label(frameTblAbsensi, text=headerTabel[1], font="12", width="10")
        mainTblHeader2.grid(row=3, column=1)
        mainTblHeader3 = Label(frameTblAbsensi, text=headerTabel[2], font="12", width="45")
        mainTblHeader3.grid(row=3, column=2)
        mainTblHeader4 = Label(frameTblAbsensi, text=headerTabel[3], font="12", width="10")
        mainTblHeader4.grid(row=3, column=3)
        mainTblHeader5 = Label(frameTblAbsensi, text=headerTabel[4], font="12", width="6")
        mainTblHeader5.grid(row=3, column=4, columnspan=2)
        
        self.mainTblContain1 = []
        self.mainTblContain2 = []
        self.mainTblContain3 = []
        self.mainTblContain4 = []
        for i in range(4,14):
            self.mainTblContain1.append(Label(frameTblAbsensi, font="12", width="4"))
            self.mainTblContain2.append(Label(frameTblAbsensi, font="12", width="10"))
            self.mainTblContain3.append(Label(frameTblAbsensi, font="12", width="45"))
            self.mainTblContain4.append(Label(frameTblAbsensi, font="12", width="10"))
            self.mainTblContain1[-1].grid(row=i, column=0)
            self.mainTblContain2[-1].grid(row=i, column=1)
            self.mainTblContain3[-1].grid(row=i, column=2)
            self.mainTblContain4[-1].grid(row=i, column=3)
        self.mainTbl1Contain5 = Button(frameTblAbsensi, font="12", bg="#FFFFFF")
        self.mainTbl2Contain5 = Button(frameTblAbsensi, font="12", bg="#FFFFFF")
        self.mainTbl3Contain5 = Button(frameTblAbsensi, font="12", bg="#FFFFFF")
        self.mainTbl4Contain5 = Button(frameTblAbsensi, font="12", bg="#FFFFFF")
        self.mainTbl5Contain5 = Button(frameTblAbsensi, font="12", bg="#FFFFFF")
        self.mainTbl6Contain5 = Button(frameTblAbsensi, font="12", bg="#FFFFFF")
        self.mainTbl7Contain5 = Button(frameTblAbsensi, font="12", bg="#FFFFFF")
        self.mainTbl8Contain5 = Button(frameTblAbsensi, font="12", bg="#FFFFFF")
        self.mainTbl9Contain5 = Button(frameTblAbsensi, font="12", bg="#FFFFFF")
        self.mainTbl10Contain5 = Button(frameTblAbsensi, font="12", bg="#FFFFFF")
        self.mainTbl1Contain5.grid(row=4, column=4, columnspan=2)
        self.mainTbl2Contain5.grid(row=5, column=4, columnspan=2)
        self.mainTbl3Contain5.grid(row=6, column=4, columnspan=2)
        self.mainTbl4Contain5.grid(row=7, column=4, columnspan=2)
        self.mainTbl5Contain5.grid(row=8, column=4, columnspan=2)
        self.mainTbl6Contain5.grid(row=9, column=4, columnspan=2)
        self.mainTbl7Contain5.grid(row=10, column=4, columnspan=2)
        self.mainTbl8Contain5.grid(row=11, column=4, columnspan=2)
        self.mainTbl9Contain5.grid(row=12, column=4, columnspan=2)
        self.mainTbl10Contain5.grid(row=13, column=4, columnspan=2)
        
        mainTblPaging1 = Button(frameTblAbsensi, text="<", command=lambda:self.mainChangePage('prev'))
        mainTblPaging1.grid(row=14, column=3, sticky="E")
        self.mainPageNumber = 1
        self.mainTblPage = Label(frameTblAbsensi, text="1")
        self.mainTblPage.grid(row=14, column=4)
        mainTblPaging2 = Button(frameTblAbsensi, text=">", command=lambda:self.mainChangePage('next'))
        mainTblPaging2.grid(row=14, column=5, sticky="W")
        
        self.btnMulaiAbsen = Button(frameOpAbsen, width="10", height="4", text="Mulai\nAbsen", bg="#00FF00", font="Cooper 15", command=self.startAbsen)
        self.btnMulaiAbsen.grid(row=0, column=0, padx=5, pady=5)
    
    def mainChangePage(self, to):
        if to == 'prev':
            if self.mainPageNumber > 1:
                self.mainPageNumber -= 1
                self.writeToTable(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10], self.kehadiran[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
                self.mainTblPage.config(text=str(self.mainPageNumber))
        else:
            if len(self.tempData) > self.mainPageNumber*10:
                self.mainPageNumber += 1
                self.writeToTable(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10], self.kehadiran[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
                self.mainTblPage.config(text=str(self.mainPageNumber))
    
    def imgShow(self, image):
        image_show = Image.fromarray(image[:,:,::-1])
        image_show = ImageTk.PhotoImage(image_show)
        self.lblPrevFoto.config(image=image_show)
        self.lblPrevFoto.image = image_show
        
    def ambilImg(self):
        if (len(self.path) > 0):
            self.img = self.read_img(self.path)
            w = 100
            h = 130
            self.img = cv2.resize(self.img, (w, h))
            
    def read_img(self, filepath):
        return cv2.imread(filepath)
    
    def browse(self):
        sql = "SELECT m.*, u.password FROM absensi a INNER JOIN mahasiswa m ON a.mhs_id = m.id INNER JOIN mata_kuliah k ON k.id = a.matkul_id INNER JOIN user u ON u.username = m.nim WHERE k.nama = %s"
        csr.execute(sql, (self.matkul.get(),))
        self.daftarAbsen = np.array(csr.fetchall(), dtype=str)
        self.lblNamaDaftar.config(text=self.matkul.get())
        self.namaMatKul.config(text="Mata Kuliah : "+self.matkul.get())
        self.lblNamaDosen.config(text="Dosen Pengajar : "+self.dosNama)
        self.btAddrAbsen = self.daftarAbsen[:,4]
        sql = "SELECT a.mhs_id, a.p1, a.p2, a.p3, a.p4, a.p5, a.p6, a.p7, a.p8, a.p9, a.p10, a.p11, a.p12 FROM absensi a INNER JOIN mahasiswa m ON a.mhs_id = m.id INNER JOIN mata_kuliah k ON a.matkul_id = k.id INNER JOIN user u ON u.mhs_dos_id = m.id WHERE k.nama = %s AND role='mahasiswa'"
        csr.execute(sql, (self.matkul.get(),))
        temp = np.array(csr.fetchall(), dtype=str)
        tempidx = int(self.pertemuan.get().split(' ')[-1])
        self.kehadiran = temp[:, tempidx]
        self.tempData = self.daftarAbsen[:,1:]
        self.mainPageNumber = 1
        self.writeToTable(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10], self.kehadiran[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
        
    def startAbsen(self):
        tempidx = self.pertemuan.get().split(' ')[-1]
        self.scanBluetooth()
        data = self.tempData
        for i in range(len(self.btAddrAbsen)):
            for addr, name in self.nearby_devices:
                if addr == self.btAddrAbsen[i].upper():
                    bil_random = str(np.random.randint(1, high=100))
                    enkripsi = aes.AESCipher(data[i][-1]).encrypt(bil_random).decode('utf-8')
                    sql = "UPDATE absensi a INNER JOIN mahasiswa m ON m.id = a.mhs_id INNER JOIN mata_kuliah k ON k.id = a.matkul_id SET p"+tempidx+" = %s WHERE m.nim = %s AND k.nama = %s"
                    csr.execute(sql, (enkripsi, str(data[i][0]), self.matkul.get()))
                    db.commit()
        sql = "SELECT a.mhs_id, a.p1, a.p2, a.p3, a.p4, a.p5, a.p6, a.p7, a.p8, a.p9, a.p10, a.p11, a.p12 FROM absensi a INNER JOIN mahasiswa m ON a.mhs_id = m.id INNER JOIN mata_kuliah k ON a.matkul_id = k.id INNER JOIN user u ON u.mhs_dos_id = m.id WHERE k.nama = %s AND role='mahasiswa'"
        csr.execute(sql, (self.matkul.get(),))
        temp = np.array(csr.fetchall(), dtype=str)
        self.kehadiran = temp[:, int(tempidx)]
        self.writeToTable(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10], self.kehadiran[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
                                     
    def scanBluetooth(self):
        self.nearby_devices = np.array(bluetooth.discover_devices(lookup_names=True))
                
    def writeToTable(self, data, hadir):
        self.clearMainTable()
        kehadiran = []
        if len(data) % 10 != 0:
            for i in range(len(data) % 10):
                self.mainTblContain1[i].config(text=str((self.mainPageNumber-1)*10+i+1))
                self.mainTblContain2[i].config(text=data[i][0])
                self.mainTblContain3[i].config(text=data[i][1])
                if hadir[i] == '':
                    self.mainTblContain4[i].config(text="Belum Absen")
                    kehadiran.append(False)
                elif int(aes.AESCipher(data[i, -1]).decrypt(hadir[i])) < 0:
                    self.mainTblContain4[i].config(text="Tidak Hadir")
                    kehadiran.append(False)
                elif int(aes.AESCipher(data[i, -1]).decrypt(hadir[i])) > 0:
                    self.mainTblContain4[i].config(text="Hadir")
                    kehadiran.append(True)
            j=0
            if j<=i:
                self.mainTbl1Contain5.config(text="Preview", command=lambda:self.previewData(data[0], kehadiran[0]), bg="#049723")
            j+=1
            if j<=i:
                self.mainTbl2Contain5.config(text="Preview", command=lambda:self.previewData(data[1], kehadiran[1]), bg="#049723")
            j+=1
            if j<=i:
                self.mainTbl3Contain5.config(text="Preview", command=lambda:self.previewData(data[2], kehadiran[2]), bg="#049723")
            j+=1
            if j<=i:
                self.mainTbl4Contain5.config(text="Preview", command=lambda:self.previewData(data[3], kehadiran[3]), bg="#049723")
            j+=1
            if j<=i:
                self.mainTbl5Contain5.config(text="Preview", command=lambda:self.previewData(data[4], kehadiran[4]), bg="#049723")
            j+=1
            if j<=i:
                self.mainTbl6Contain5.config(text="Preview", command=lambda:self.previewData(data[5], kehadiran[5]), bg="#049723")
            j+=1
            if j<=i:
                self.mainTbl7Contain5.config(text="Preview", command=lambda:self.previewData(data[6], kehadiran[6]), bg="#049723")
            j+=1
            if j<=i:
                self.mainTbl8Contain5.config(text="Preview", command=lambda:self.previewData(data[7], kehadiran[7]), bg="#049723")
            j+=1
            if j<=i:
                self.mainTbl9Contain5.config(text="Preview", command=lambda:self.previewData(data[8], kehadiran[8]), bg="#049723")
        else:
            for i in range(10):
                self.mainTblContain1[i].config(text=str((self.mainPageNumber-1)*10+i+1))
                self.mainTblContain2[i].config(text=data[i][0])
                self.mainTblContain3[i].config(text=data[i][1])
                if hadir[i] == '':
                    self.mainTblContain4[i].config(text="Belum Absen")
                    kehadiran.append(False)
                elif int(aes.AESCipher(data[i, -1]).decrypt(hadir[i])) < 0:
                    self.mainTblContain4[i].config(text="Tidak Hadir")
                    kehadiran.append(False)
                elif int(aes.AESCipher(data[i, -1]).decrypt(hadir[i])) > 0:
                    self.mainTblContain4[i].config(text="Hadir")
                    kehadiran.append(True)
            j=0
            self.mainTbl1Contain5.config(text="Preview", command=lambda:self.previewData(data[0], kehadiran[0]), bg="#049723")
            j+=1
            self.mainTbl2Contain5.config(text="Preview", command=lambda:self.previewData(data[1], kehadiran[1]), bg="#049723")
            j+=1
            self.mainTbl3Contain5.config(text="Preview", command=lambda:self.previewData(data[2], kehadiran[2]), bg="#049723")
            j+=1
            self.mainTbl4Contain5.config(text="Preview", command=lambda:self.previewData(data[3], kehadiran[3]), bg="#049723")
            j+=1
            self.mainTbl5Contain5.config(text="Preview", command=lambda:self.previewData(data[4], kehadiran[4]), bg="#049723")
            j+=1
            self.mainTbl6Contain5.config(text="Preview", command=lambda:self.previewData(data[5], kehadiran[5]), bg="#049723")
            j+=1
            self.mainTbl7Contain5.config(text="Preview", command=lambda:self.previewData(data[6], kehadiran[6]), bg="#049723")
            j+=1
            self.mainTbl8Contain5.config(text="Preview", command=lambda:self.previewData(data[7], kehadiran[7]), bg="#049723")
            j+=1
            self.mainTbl9Contain5.config(text="Preview", command=lambda:self.previewData(data[8], kehadiran[8]), bg="#049723")
            j+=1
            self.mainTbl10Contain5.config(text="Preview", command=lambda:self.previewData(data[9], kehadiran[9]), bg="#049723")
            
    def clearMainTable(self):
        for i in range(10):
            self.mainTblContain1[i].config(text="")
            self.mainTblContain2[i].config(text="")
            self.mainTblContain3[i].config(text="")
            self.mainTblContain4[i].config(text="")
        self.mainTbl1Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl2Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl3Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl4Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl5Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl6Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl7Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl8Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl9Contain5.config(text="", command="", bg="#FFFFFF")
        self.mainTbl10Contain5.config(text="", command="", bg="#FFFFFF")
                                      
    def previewData(self, data, hadir):
        self.path = 'Data Mahasiswa/Foto Profil/'+data[0]+'.jpg'
        self.ambilImg()
        self.imgShow(self.img)
        self.lblNamaMhs.config(text=data[1])
        self.lblNIMMhs.config(text=data[0])
        self.lblNoHPMhs.config(text=data[2])
        if hadir == True:
            self.selected.set("Hadir")
        else:
            self.selected.set("Tidak Hadir")
        self.btnSimpan.config(command=lambda:self.saveChangePreview(data))
        
    def saveChangePreview(self, data):
        tempidx = self.pertemuan.get().split(' ')[-1]
        if self.selected.get() == 'Hadir':
            bil_random = str(np.random.randint(1, high=100))
            enkripsi = aes.AESCipher(data[-1]).encrypt(bil_random).decode('utf-8')
            sql = "UPDATE absensi a INNER JOIN mahasiswa m ON m.id = a.mhs_id INNER JOIN mata_kuliah k ON k.id = a.matkul_id SET p"+tempidx+" = %s WHERE m.nim = %s AND k.nama = %s"
            csr.execute(sql, (enkripsi, str(data[0]), self.matkul.get()))
            db.commit()
        else:
            bil_random = str(np.random.randint(-100, high=-1))
            enkripsi = aes.AESCipher(data[-1]).encrypt(bil_random).decode('utf-8')
            sql = "UPDATE absensi a INNER JOIN mahasiswa m ON m.id = a.mhs_id INNER JOIN mata_kuliah k ON k.id = a.matkul_id SET p"+tempidx+" = %s WHERE m.nim = %s AND k.nama = %s"
            csr.execute(sql, (enkripsi, str(data[0]), self.matkul.get()))
            db.commit()
        self.clearPreview()
        sql = "SELECT a.mhs_id, a.p1, a.p2, a.p3, a.p4, a.p5, a.p6, a.p7, a.p8, a.p9, a.p10, a.p11, a.p12 FROM absensi a INNER JOIN mahasiswa m ON a.mhs_id = m.id INNER JOIN mata_kuliah k ON a.matkul_id = k.id INNER JOIN user u ON u.mhs_dos_id = m.id WHERE k.nama = %s AND role='mahasiswa'"
        csr.execute(sql, (self.matkul.get(),))
        temp = np.array(csr.fetchall(), dtype=str)
        self.kehadiran = temp[:, int(tempidx)]
        self.writeToTable(self.tempData[(self.mainPageNumber-1)*10:self.mainPageNumber*10], self.kehadiran[(self.mainPageNumber-1)*10:self.mainPageNumber*10])
    
    def clearPreview(self):
        self.path = 'konden mepoto.jpg'
        self.ambilImg()
        self.imgShow(self.img)
        self.lblNamaMhs.config(text="")
        self.lblNIMMhs.config(text="")
        self.lblNoHPMhs.config(text="")
        self.btnSimpan.config(command="")
                
    def login(self):
        username = self.username.get()
        password = hashlib.md5(self.password.get().encode('utf-8')).hexdigest()
        sql = "SELECT username,password FROM user WHERE username = %s"
        csr.execute(sql, (username,))
        user_verified = csr.fetchone()
        if username == user_verified[0] and password == user_verified[1]:
            messagebox.showinfo("Message", "Login berhasil!")
            self.clearMaster()
            self.komponenMain()
        else:
            messagebox.showinfo("Message", "Username atau Password salah.")

Main(root, "== Absensi ==")
root.mainloop()
