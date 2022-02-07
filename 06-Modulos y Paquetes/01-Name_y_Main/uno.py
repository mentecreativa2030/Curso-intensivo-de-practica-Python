def func():
    print("func() ejecuto en uno.py")

print("Impresión de nivel superior dentro de una.py")

if __name__ == "__main__":
    print("uno.py esta corriendo directamente")
else:
    print("uno.py esta siendo importado de otro modulo")
