def mi_receta(ingrediente1, ingrediente2):
  """Esta receta combina los ingredientes."""
  resultado = ingrediente1 + " con " + ingrediente2
  return resultado

primer_ingrediente = input()
segundo_ingrediente = input()

# Aquí estamos LLAMANDO a la función 'mi_receta'
# y le estamos dando los 'ingredientes' (argumentos)
combinacion = mi_receta(primer_ingrediente, segundo_ingrediente)

print(f"La combinación es: {combinacion}")