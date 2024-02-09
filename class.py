class Robot:
  def _init_(self,name):
    self.name= name
    self.hit_points = 10

    def _str_(self):
       return f"Robot { self.name}"
    

    class Robot:
        def _init_(self, name):      #my constructor code 
           self.name= name           #my constructor code
    self.hit_points = 10             #my constructor code

    def fire(self, target_robot):    #my fire method code
       target_robot.hit_points -=2   #my fire method code 


    class Robot:
        def _init_(self, name):
           self.name= name
    self.hit_points = 10
    def fire(self, target_robot):
       target_robot.hit_points -=2
       def isDead(self):                   #is Dead method
          return self.hit_points <= 0
       

    class Arena: 
       def fight(self,robot1,robot2):
          while not robot1.isDead() and not robot2.isDead():
             robot1.fire(robot2)
             robot2.fire(robot1)


          if robot1.isDead():
               print(f"{robot2} wins the fight!")
          else:
               print(f"{robot1} wins the fight!")     


               bob=    Robot("bob") 
               alice=  Robot("alice")
               arena=  Arena()
               arena.fight(bob, alice)
             