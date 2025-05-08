def saludar(nombre):
  """Esta función toma un nombre y lo saluda."""
  print(f"¡Hola, {nombre}!")

nombre_de_persona = input()
saludar(nombre_de_persona)

otro_nombre = input()
saludar(otro_nombre)

saludar(nombre_de_persona + otro_nombre)

