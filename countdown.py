number = 10
HasPaintedPoints = False

while number >= 0:
    userInput = input("Qué cable quieres cortar?")
    if userInput == "red":
        print("Te has salvado")
        break
    if (number > 2 and number < 8):
        if not HasPaintedPoints:
            print("...")
            HasPaintedPoints = True
            number = 3
            number -= 1 
        continue
    print(number)
    number -= 1

print("La bomba ha explotado")
        
           