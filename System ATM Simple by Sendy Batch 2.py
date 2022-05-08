pin = '229012'
saldo = 0

print('Selamat Datang Di ATM BANK SENDY™🗿')

for i in range(3):
    print()
    inPin = input("Silahkan Masukkan Pin Anda : ")
    if inPin == pin :
        print()
        print("PIN Anda BENAR💯")
        print()
        break

    else :
        print("PIN Anda SALAH🤦‍♂️🤦‍♀️")
        if i == 2 :
            print("============================================")
            print("Akun Anda Kami Tangguhkan Selama 24 Jam☹")
            print("============================================")
            quit()

pilihan = 'y'
while (pilihan == 'y'):
    print('01. Informasi Saldo')
    print('02. Penarkan Uang Tunai')
    print('03. Setor Tabungan')
    print('04. Keluar')
    print()

    menu = input('Silahkan Pilih Menu yang Anda Inginkan : ')
    print("===================================================")

    if menu == '1':
        print(f"Sisa Saldo Anda : {saldo}")
    elif menu == '2':

        if saldo < 50000:
            print("Maaf, Saldo Anda saat ini Tidak Mencukupi untuk Bertransaksi.😥")
            print("Silahkan Isi Saldo Terlebih Dahulu.")
            print("Silahkan Cek Terlebih Dahulu untuk Kenyamanan Anda")

        else:
            print("Jumlah Nominal Penarikan Sebesar 50000, 100000, 250000, 500000, 1000000")
            tunai = int(input("Jumlah penarikan anda : "))
            if (tunai == 50000) or (tunai == 100000) or (tunai == 250000) or (tunai == 500000) or (tunai == 1000000):
                saldo == saldo - tunai
                print()
                print(f"Saldo Ditarik : {tunai}")
                print(f"Sisa Saldo Anda : {saldo}")
            else:
                print("Nominal Uang Tidak Diketahui😮")
        setor = int(input("Silahkan Masukkan Nominal yang Ingin Anda Setor : "))
        saldo = saldo + setor
        print()
        print(f"Sisa Saldo Anda : {saldo}")

    elif menu == '4':
        print("Silahkan Ambil Kartu Anda dari mesin ATM👍🏻")
        print()
        print("🙏🏻Terima Kasih Sudah Menggunakan Layanan BANK SENDY™🗿")
        print()

    print("=========================================================")
    pilihan = input("Apakah Ingin Melanjutkan Transaksi (y/n)? ")
    print("=========================================================")