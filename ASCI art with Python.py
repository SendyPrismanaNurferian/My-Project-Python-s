import ascii_magic

try:
    my_art = ascii_magic.from_image_file('....png/jpg') # Tanda .... adalah nama file
    ascii_magic.to_terminal(my_art)
except Exception as e:
    print("Gambar Error!!", e)
    
    #Sebelumnya pastikan download Python unttuk software dan juga download ascii-magic di https://pypi.org/project/ascii-magic/ 
    #Setelah itu bisa mengikuti source code yang saya buat atau buat dari defaultnya di link download atau bisa lihat channel YT lainnya
