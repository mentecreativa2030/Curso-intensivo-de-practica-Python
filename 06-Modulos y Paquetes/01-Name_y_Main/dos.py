import uno

print("nivel superior en dos.py")

uno.func()

if __name__ == "__main__":
    print("dos.py esta corriendo directamente")
else:
    print("dos.py es siendo importado dentro de otro modulo")
