# ----- Ejercicios de CodeWars: KYU 7 -----

def jumping_number(number):
    number_str = str(number)
    for i, letra in enumerate(number_str):
        print(int(letra), i, letra[0])
jumping_number(123)
