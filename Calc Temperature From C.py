# Program Convertion Temperature From C to All
 
# convert celcius to reamur
def conv_reamur(celcius):
    convert_reamur = 4 * celcius / 5
    return convert_reamur
 
# convert celcius to farenheit
def conv_farenheit(celcius):
    convert_farenheit = 9 * celcius / 5 + 32
    return convert_farenheit
 
# convert celcius to kelvin
def conv_kelvin(celcius):
    convert_kelvin = celcius + 273
    return convert_kelvin
 
# create main menu
def main():
    print('Program Convertion Temperature')
    print('By Sendy Prismana Nurferian')
 
    # create input
    temperature = int(input('Enter Celcius Temperature Scala: '))
 
    # cetak hasil
    print('++++++++++++++++++++++++++++++++++++++++++++')
    print(f'Result Covert Temperature {temperature} C is {conv_reamur(temperature)} Reamur')
    print(f'Result Covert Temperature {temperature} C is {conv_farenheit(temperature)} Farenheit')
    print(f'Result Covert Temperature {temperature} C is {conv_kelvin(temperature)} Kelvin')
    print('++++++++++++++++++++++++++++++++++++++++++++++')
 
if __name__=='__main__':
    main()