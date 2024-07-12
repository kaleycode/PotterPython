print("Which Harry Potter character are you?")
study = input("Do you prepare for exams and study frequently? yes or no: ")
if study == "yes":
  print("You are Hermione Granger!")
else:
  print("You're not Hermione, but you could be Harry, Ron, or Luna.")
  myCharacter = input("Do you have a scar on your forehead? yes or no: ")
  if myCharacter == "yes":
    print("You are Harry Potter!")
  if myCharacter == "no":
    aORb = input("Do you (a) play sports or (b) are you seen as a bit of an oddball? (type a or b) ")
    if aORb == "a":
      print("You are Ron Weasely!")
    if aORb == "b":
      print("You are Luna Lovegood!")