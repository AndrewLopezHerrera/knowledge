from logic import And, Not, Implication, Or, Symbol, model_check

# Symbols
# "Rain"
# "Hagrid"
# "Dumbledore"

# knowledge
knowledge = And()


# Si no llovió, Harry visitó a Hagrid hoy
# Harry visitó a Hagrid o a Dumbledore hoy, pero no a ambos
# Harry visitó a Dumbledore hoy

# print(f"Rain: {model_check(knowledge, rain)}")
# print(f"Hagrid: {model_check(knowledge, hagrid)}")
# print(f"Dumbledore: {model_check(knowledge, dumbledore)}")
