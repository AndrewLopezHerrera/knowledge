from logic import And, Not, Implication, Or, Symbol, model_check

# Symbols
# "Rain"
# "Hagrid"
# "Dumbledore"
rain = Symbol("Rain")
hagrid = Symbol("Hagrid")
dumbledore = Symbol("Dumbledore")

# knowledge
knowledge = And()


# Si no llovió, Harry visitó a Hagrid hoy
knowledge.add(Implication(Not(rain), hagrid))

# Harry visitó a Hagrid o a Dumbledore hoy, pero no a ambos
knowledge.add(Or(hagrid, dumbledore))
knowledge.add(Not(And(hagrid, dumbledore)))

# Harry visitó a Dumbledore hoy
knowledge.add(dumbledore)

print(f"Rain: {model_check(knowledge, rain)}")
print(f"Hagrid: {model_check(knowledge, hagrid)}")
print(f"Dumbledore: {model_check(knowledge, dumbledore)}")


# Examples

## 1. Si estudio o hago tareas, entonces paso el curso, pero si no estudio, no paso.
# Dado que: estudio
# ¿paso el curso? → True
# ¿no paso el curso? → False

estudiar = Symbol("Estudiar")
tareas = Symbol("Tareas")
aprobar = Symbol("Aprobar")

knowledge = And()

knowledge.add(Implication(Or(estudiar, tareas), aprobar))
knowledge.add(Implication(Not(estudiar), Not(aprobar)))
knowledge.add(estudiar)

print("\nEjemplo 1")
print(f"Estudiar: {model_check(knowledge, estudiar)}")
print(f"Hacer tareas: {model_check(knowledge, tareas)}")
print(f"Aprobar: {model_check(knowledge, aprobar)}")

## 2. Si estudio, entonces si hago tareas paso el curso.
# Dado que: estudio, hago tareas
# ¿paso el curso? → True

estudiar = Symbol("Estudiar")
tareas = Symbol("Tareas")
aprobar = Symbol("Aprobar")

knowledge = And()

knowledge.add(Implication(estudiar, Implication(tareas, aprobar)))
knowledge.add(estudiar)
knowledge.add(tareas)

print("\nEjemplo 2")
print(f"Estudiar: {model_check(knowledge, estudiar)}")
print(f"Hacer tareas: {model_check(knowledge, tareas)}")
print(f"Aprobar: {model_check(knowledge, aprobar)}")

## 3. Voy al cine si y solo si termino la tarea y no estoy cansado.
# Dado que: termino la tarea, no estoy cansado
# ¿voy al cine? → True
# ¿no voy al cine? → False

cine = Symbol("Cine")
tarea = Symbol("Tarea")
cansado = Symbol("Cansado")

knowledge = And()

knowledge.add(Implication(cine, And(tarea, Not(cansado))))
knowledge.add(Implication(And(tarea, Not(cansado)), cine))
knowledge.add(tarea)
knowledge.add(Not(cansado))

print("\nEjemplo 3")
print(f"Voy al cine: {model_check(knowledge, cine)}")
print(f"Hacer tareas: {model_check(knowledge, tarea)}")
print(f"Estoy cansado: {model_check(knowledge, cansado)}")

## 4. Si el sistema responde y no hay timeout, entonces la transacción se procesa; de lo contrario, falla.
# Dado que: el sistema responde, no hay timeout
# ¿la transacción se procesa? → True
# ¿la transacción falla? → False

sistema = Symbol("Sistema")
timeout = Symbol("Timeout")
transaccion = Symbol("Transaccion")

knowledge = And()

knowledge.add(Implication(And(sistema, Not(timeout)), transaccion))
knowledge.add(sistema)
knowledge.add(Not(timeout))

print("\nEjemplo 4")
print(f"El sistema funciona: {model_check(knowledge, sistema)}")
print(f"Hay timeout: {model_check(knowledge, timeout)}")
print(f"Se hace la transacción: {model_check(knowledge, transaccion)}")

## 5. No es cierto que si estudio entonces paso.
# ¿estudio? → True
# ¿no paso? → True

estudio = Symbol("Estudiar")
aprobar = Symbol("Aprobar")

knowledge = And()

knowledge.add(Not(Implication(estudio, aprobar)))

print("\nEjemplo 5")
print(f"¿Estudio?: {model_check(knowledge, sistema)}")
print(f"¿Paso?: {model_check(knowledge, timeout)}")