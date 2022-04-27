#Creates grid with input of (1) length, (2) height, and (3) desired character for grid have

#Welcome
print("Welcome!" + "\n\nThis program creates a grid out of a character of your choice!" + "\nYou will also input the size of your desired grid!" + "\n")

gridLength = 0
gridHeight = 0
character = ""

while True: 
  #main loop that continuously asks for user inputs until they are given
  while True:
    #asks user for single they want in their grid
    while True:
      character = input("What character do you want in your grid? Ex) 'X', '$'" + "\nEnter one character only: ")
      if len(character) > 1:
        print("Try again")
        continue
      else:
        break
      
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
  
  
  #starts with the main empty list
  maze = []
  #outer loop starts with a new empty list and then the inner loop adds the character the specificed number of times (the length of the grid) to that empty loop. Then that empty loops gets appended to the main list. This successfully creates a row with the desired length. This repeats till the desired height of the grid is reached. 
  for i in range(gridHeight):
    row = []
    for i2 in range(gridLength):
      row.append(character)
    maze.append(row)

  def outputMaze(inputMaze):
    print("\n" + "-" * (2 * len(inputMaze[0]) + 3)) #Top border line 
    for row in inputMaze:
      print("|", end = " ") #left side border
      for item in row:
        print(item, end = " ") #each item separated by spaces
      print('|') # right side border
    print("-"*(2 * len(inputMaze[0]) + 3) + "\n") #Bottom border line

  outputMaze(maze)

  #loop to get correct input to play again
  while True:
    playagain = input("Do you want to play again?" + "\nEnter 'Y' or 'N': ")
    if playagain == "Y" or playagain == "N":
      break
    elif playagain != "N" or playagain != "Y":
      print("Please enter a valid input")
      continue

  #determine whether to play again (go to top of loop) or break and end
  if playagain == "Y":
    print("\nWelcome back!")
    continue
  elif playagain == "N":
    print("Bye!")
    break
  else:
    print(".")
  