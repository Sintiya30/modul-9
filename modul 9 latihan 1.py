#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:53:22 2024

@author: adesintia
"""

nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")
email = input("Email: ")
dosen_wali = input("Dosen Wali: ")

file = open("Biodata.txt", "w")
file.write(f"Nama: {nama}\n")
file.write(f"Umur: {umur}\n")
file.write(f"Alamat: {alamat}\n")
file.write(f"Email: {email}\n")
file.write(f"Dosen Wali: {dosen_wali}\n")
file.close()
print("Data berhasil disimpan.")

file = open("Biodata.txt", "r")
data = file.read()
print(data)
file.close()