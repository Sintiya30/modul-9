#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:29:11 2024

@author: adesintia
"""

def file_ada(nama_file):
    """Memeriksa apakah file ada dengan mencoba membukanya."""
    try:
        open(nama_file).close()
        return True
    except:
        return False

def buat_file(nama_file):
    open(nama_file, 'w').close()
    print(f"File '{nama_file}' berhasil dibuat.")

def baca_file(nama_file):
    if file_ada(nama_file):
        with open(nama_file, 'r') as file:
            isi = file.read()
            print(f"Isi file '{nama_file}':\n{isi or '(Kosong)'}")
    else:
        print(f"File '{nama_file}' tidak ditemukan.")

def tambah_teks(nama_file, teks):
    if file_ada(nama_file):
        with open(nama_file, 'a') as file:
            file.write(teks + '\n')
            print(f"Teks berhasil ditambahkan ke file '{nama_file}'.")
    else:
        print(f"File '{nama_file}' tidak ditemukan.")

while True:
    print("\nMenu: 1.Buat File 2.Baca File 3.Tambah Text 4.Keluar")
    p = input("Pilih (1/2/3/4): ")
    if p == '4':
        print("Program selesai."); break
    nama = input("Nama file: ")
    if p == '1': 
        buat_file(nama)
    eli