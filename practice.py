from logic import And, Not, Implication, Or, Symbol, model_check

cardEmployee = Symbol("CardEmployee")
pinCode = Symbol("PinCode")
isVisitor = Symbol("IsVisitor")
enterServerRoom = Symbol("EnterServerRoom")
enterMeetingRoom = Symbol("EnterMeetingRoom")
isModeEmergency = Symbol("isModeEmergency")
isModeIntruder = Symbol("isModeIntruder")
isOpenDoor = Symbol("isOpenDoor")

knowledge = And()

knowledge.add(Implication(And(pinCode, cardEmployee), enterServerRoom))
knowledge.add(Implication(Or(cardEmployee, isVisitor), enterMeetingRoom))
knowledge.add(Implication(isVisitor, Not(enterServerRoom)))
knowledge.add(Implication(isModeEmergency, isOpenDoor))
knowledge.add(Implication(isModeIntruder, Not(isModeEmergency)))

knowledge.add(cardEmployee)
knowledge.add(Not(pinCode))
knowledge.add(Not(isModeEmergency))

print("Problem 1: Smart Building")
print(f"Can Ana enter the server room? -> {model_check(knowledge, enterServerRoom)}")
print(f"Can Ana enter the meeting room? -> {model_check(knowledge, enterMeetingRoom)}")

knowledge.add(isModeIntruder)

print(f"If an intruder alert is now activated, does Ana's access to the server room change? -> {model_check(knowledge, enterServerRoom)}")


ColMustard = Symbol("ColMustard")
ProfPlum = Symbol("ProfPlum")
MsScarlet = Symbol("MsScarlet")

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")

knowledge = And()

knowledge.add(Not(ColMustard))
knowledge.add(Not(kitchen))
knowledge.add(Not(revolver))
knowledge.add(Or(Not(MsScarlet), Not(library), Not(wrench)))
knowledge.add(Not(ProfPlum))
knowledge.add(Not(ballroom))

character = ""
weapon = ""
room = ""

if model_check(knowledge, ColMustard) :
    character = "ColMustard"
elif model_check(knowledge, ProfPlum) :
    character = "ProfPlum"
elif model_check(knowledge, MsScarlet) :
    character = "MsScarlet"

if model_check(knowledge, knife) :
    weapon = "knife"
elif model_check(knowledge, revolver) :
    weapon = "revolver"
elif model_check(knowledge, wrench) :
    weapon = "wrench"

if model_check(knowledge, ballroom) :
    room = "ballroom"
elif model_check(knowledge, kitchen) :
    room = "kitchen"
elif model_check(knowledge, wrench) :
    room = "wrench"

print("Problem 2: Clue Mystery")

# Verificación de Personajes
print(f"Is ColMustard the culprit? {model_check(knowledge, ColMustard)}")
print(f"Is ProfPlum the culprit? {model_check(knowledge, ProfPlum)}")
print(f"Is MsScarlet the culprit? {model_check(knowledge, MsScarlet)}")

# Verificación de Armas
print(f"Was the weapon the knife? {model_check(knowledge, knife)}")
print(f"Was the weapon the revolver? {model_check(knowledge, revolver)}")
print(f"Was the weapon the wrench? {model_check(knowledge, wrench)}")

# Verificación de Habitaciones
print(f"Did it happen in the ballroom? {model_check(knowledge, ballroom)}")
print(f"Did it happen in the kitchen? {model_check(knowledge, kitchen)}")
print(f"Did it happen in the library? {model_check(knowledge, library)}")

print(f"The guilty party is {character} in the {room} with the {weapon}.")