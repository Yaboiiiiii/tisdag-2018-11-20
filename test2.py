check = False

while check != True:
    answer = input("Skriv ett kolon: ")
    if answer == ":":
        check = True
        print("Grattis du gissade rätt!")
    elif answer == "Nä du är fan sämst":
        print("no u")
    else:
        print("Du är fan sämst!")
    