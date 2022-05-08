def menu():
    awal=int(input("Masukkan Jumlah Mahasiswa"))
    for i in range (awal):
        NIM=input ("NIM : ")
        Nama=input ("Nama : ")
        NTugas=int (input ("Nilai Tugas : "))
        NUTS=int (input ("Nilai UTS : "))
        NEAS=int (input ("Nilai EAS : "))

        Nilai_Tugas=int(20/100*NTugas)
        Nilai_UTS=int(30/100*NUTS)
        Nilai_EAS=int(40/100*NEAS)
        Nilai_Akhir = Nilai_Tugas+Nilai_UTS+Nilai_EAS

        print("##########-DATA MAHASISWA-##########")
        print("Jumlah Mahasiswa : ",awal)
        print("Nama : ",Nama)
        print("NIM : ",NIM)
        print("Nilai Tugas Mahasiswa",NTugas)
        print("Nilai UTS : ",NUTS)
        print("Nilai EAS : ",NEAS)
        print("Nilai Akhir : ",Nilai_Akhir)

        if Nilai_Akhir>=85:
            print("Grades A")
        elif Nilai_Akhir<80 and Nilai_Akhir>=60:
            print("Grades B")
        elif Nilai_Akhir<60 and Nilai_Akhir>=50:
            print("Grades C")
        elif Nilai_Akhir<50:
            print("Grades D")
        if Nilai_Akhir>=80 and Nilai_Akhir>50:
            print("Keterangan : Selamat Anda Lulus")
        else:
            print("Keterangan : Anda Tidak Lulus")
        print("======================================================")
    
    menu()