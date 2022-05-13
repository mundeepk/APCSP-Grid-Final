#Creates grid with input of (1) length, (2) height, and (3) desired character for grid have

#Welcome
print("Welcome!" +
      "\n\nThis program creates a grid out of characters of your choice!" +
      "\nYou will also input the size of your desired grid!" + "\n")

gridLength = 0
gridHeight = 0
userCharacters = ""

while True:
    #main loop that continuously asks for user inputs until they are given
    while True:
        #asks user for single they want in their grid
        userCharacters = input(
                "What character(s) do you want in your grid? Ex) 'X%', '$j5'" +
                "\nEnter as many as you wish: ")
      
        #asks user for square or rectangle grid
        while True:
            shape = input("\nDo you want a square or rectangle grid?" +
                          "\nEnter 'square' or 'rectangle': ")
            #gets sole side length and uses loop to continue to do so if not    given an integer
            if shape == "square":
                while True:
                    try:
                        sideLength = int(input("\tEnter your side length: "))
                        break
                    except ValueError:
                        print("\tPlease try again")
                        continue
                gridLength = sideLength
                gridHeight = sideLength
                break
            #gets height, length of rect. and uses loop to continue to do so if not given an integer
            elif shape == "rectangle":
                while True:
                    try:
                        sideLength = int(input("\tEnter length: "))
                        break
                    except ValueError:
                        print("\tPlease try again")
                        continue
                while True:
                    try:
                        sideHeight = int(input("\tEnter height: "))
                        break
                    except ValueError:
                        print("\tPlease try again")
                        continue
                gridLength = sideLength
                gridHeight = sideHeight
                break
            else:
                print("Please try again")
                continue
            break
        break

    
    textNoSpaces = list(userCharacters.replace(" ", ""))
    multipliedFactor = ((gridHeight * gridLength))
    longList = []
    longList.extend(textNoSpaces * multipliedFactor)

    grid = []
  
    for i in range(gridHeight):
      grid.append(longList[(gridLength * i):gridLength * (i + 1)])

    def outputGrid(inputGrid):
        if gridLength * gridHeight > 25:
          print("Here is your large size " + shape + " grid!")
        elif gridLength * gridHeight > 10:
          print("Here is your medium size " + shape + " grid!")
        else:
          print("Here is your small size " + shape + " grid!")

        print("-" * (2 * len(inputGrid[0]) + 3))  #Top border line
        for row in inputGrid:
            print("|", end = " ")  #left side border
            for item in row:
                print(item, end = " ")  #each item separated by spaces
            print('|')  # right side border
        print("-" * (2 * len(inputGrid[0]) + 3) + "\n")  #Bottom border line

    outputGrid(grid)


    #loop to get correct input to play again
    while True:
        playagain = input("Do you want to play again?" +
                          "\nEnter 'y' or 'n': ")
        if playagain == "y" or playagain == "n":
            break
        elif playagain != "n" or playagain != "y":
            print("Please enter a valid input")
            continue

    #determine whether to play again (go to top of loop) or break and end
    if playagain == "y":
        print("\nWelcome back!")
        continue
    elif playagain == "n":
        print("Bye!")
        break