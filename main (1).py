# Define the base class player
class Player:
  def Play(self):
      print("The player is playing cricket.")     
# Define the derived class Batsman
class  Batsman(Player):
  def Play(self):
      print ("The batsman is batting. ")
# Define the derived class Bowler
class Bowler(Player):
  def Play(self):
      print(" The bowler is bowling. ") 
# create objects of Batsman and Bowler classes
batsman=Batsman ()
bowler=Bowler()
# call the play()method for each object
batsman. Play() 
bowler. Play()

