print("ingrese 1 si conoce celcios")
print("ingrese 2 si conoce farenheit")
opcion = int(input(""))

temperatura = float(input("ingrese el valor"))


def celcius_a_farenheit(temperatura):
    farenheit = (temperatura * 9/5) + 32
    print(str(farenheit) + "grados farenheit")

def farenheit_a_celcius( temperatura):
    celcius = (temperatura - 32) * 5/9
    print(str(celcius) + "grados celcius")

match opcion:
    case 1:
        resultado = celcius_a_farenheit(temperatura)
    case 2:
        resultado = farenheit_a_celcius(temperatura)
    case 3:
        resultado = "opción invalida"
print(resultado)