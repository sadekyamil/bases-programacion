def ordenar_numeros():
  """
  Solicita tres números enteros positivos al usuario y los muestra de menor a mayor.
  """
  numeros = []
  for i in range(3):
    while True:
      try:
        num_str = input(f"Ingrese el número entero positivo #{i+1}: ")
        num = int(num_str)
        if num > 0:
          numeros.append(num)
          break
        else:
          print("Por favor, ingrese un número entero positivo.")
      except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

  numeros.sort()
  print("\nLos números ingresados, ordenados de menor a mayor, son:")
  print(numeros[0], "<=", numeros[1], "<=", numeros[2])

if __name__ == "__main__":
  ordenar_numeros()