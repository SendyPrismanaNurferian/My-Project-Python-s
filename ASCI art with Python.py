import ascii_magic

try:
    my_art = ascii_magic.from_image_file('....png/jpg') # Tanda .... adalah nama file
    ascii_magic.to_terminal(my_art)
except Exception as e:
    print("Gambar Error!!", e)
    
    