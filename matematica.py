

def decimal_a_binario(decimal):
    """Convierte un número decimal entero a su representación binaria (string)."""
    if decimal == 0:
        return "0"
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    return binario

# Solicitar al usuario que ingrese un número decimal
try:
    num_decimal = int(input("Ingresa un número decimal entero: "))
    resultado_binario = decimal_a_binario(num_decimal)
    print(f"El binario de {num_decimal} es: {resultado_binario}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")

