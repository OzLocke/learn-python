import sys
#Global variables
# Key is "Strong against" value
type_clash = {"water": "fire", "fire": "grass", "grass": "water"}

class Pokemon:
  def __init__(self, p_name, p_level, p_type):
    self.p_name = p_name
    self.p_level = p_level
    self.p_type = p_type
    self.p_max_health = self.p_level * 10
    self.p_health = self.p_max_health
    self.p_status = {"knocked out": False, "poisoned": False, "stunned": False}
    
  def __repr__(self):
    return "A level {level} pokemon called {name}. Health: {health}/{max_health}. Statuses: {statuses}".format(level=str(self.p_level), name=self.p_name, health=str(self.p_health), max_health=str(self.p_max_health), statuses=str(self.p_status))
  
  def lose_health(self, damage):
    # Apply damage, setting it to zero if the damage was lethal
    if self.p_health - damage < 0:
      self.p_health = 0
    else:
      self.p_health -= damage
    
    print("{name} took {damage} damage. Their health is now {health}".format(name=self.p_name, damage=damage, health=self.p_health))
    
    # Check for and apply Knocked Out status
    if self.p_health == 0:
      self.p_status["knocked out"] = True
      print("Oh no! {name} was knocked out!".format(name=self.p_name))
  
  def gain_health(self, health):
    # Check if health can be applied (knocked out pokemon cannot be healed this way)
    if self.p_status["knocked out"] == True:
      print("{name} is knocked out, it can't be healed!".format(name=self.p_name))
    else:
      # Apply health, overhealing is not allowed
      if self.p_health + health > self.p_max_health:
        self.p_health = self.p_max_health
      else:
        self.p_health += health
      print("{name} received {health} points of healing. {name}'s health is now {new_health}".format(name=self.p_name, health=health, new_health=self.p_health))
    
  def restore(self):
    # Check if restore can be used (pokemons not knocked out cannot be restored)
    if self.p_status["knocked out"] == False:
      print("{name} isn't knocked out so cannot be restored".format(name=self.p_name))
    else:
      self.p_status["knocked out"] = False
      self.p_health = self.p_max_health
      print("{name} was restored, they are no longer knocked out, and their health is {health}/{max_health}".format(name=self.p_name, health=self.p_health, max_health=self.p_max_health))

  def deal_damage(self, target):
    # Exit script if 
    if target == self:
      print("Sorry, your pokemon can't target itself!")
      sys.exit(1)
    # Only run if target is another pokemon
    try:
      #-Calculate and apply damage-
      # Detect crits by comparing types
      crit = type_clash[self.p_type] == target.p_type
      # Calculate damage as 1 damage per level, doubled if crit (1 or 0 for True or False plus 1)
      damage = (1 * self.p_level) * crit + 1
      print("{attacker} attacks {defender}.".format(attacker=self.p_name, defender=target.p_name))
      if crit: print("Crititcal hit!")
      target.lose_health(damage)
    except (TypeError, AttributeError):
      print("Sorry, you pokemon can only target other pokemons")

class FunctionsTestManual():
    def __init__(self):
        print("----TESTING-----")
        # Take user input to set up the pokemon to test against
        self.p_pokemon = input("Name your test pokemon: ")
        self.p_level = int(input("Give it a level (int): "))
        self.p_type = input("Give it a type: ")
        
        # Create the pokemon
        self.obj = Pokemon(self.p_pokemon, self.p_level, self.p_type)
        
        # Create the test list (note this needs to be done after creating the pokemon, so the object is accessible)
        self.tests = {"1": self.obj.lose_health, "2": self.obj.gain_health, "3": self.obj.restore}
        print("\nYou can test the following functions:")
        
        # Print out the available tests
        for key, value in self.tests.items():
          print(key + ": " + value.__name__)
        # Take test choice input, use Try Except with while loop to catch bad inputs and let user try again
        while True:
          try:
            self.fn = self.tests[input("\nChoose a test (by the number): ")]
            break #input was valid so break the loop
          except KeyError:
            print("That test does not exist!")
        
        print("\nOK, lest test {function} against {pokemon}\n".format(function=self.fn.__name__, pokemon=self.obj.p_name))
        # Run the relevent sub function to test the chosen function
        if self.fn.__name__ == "lose_health":
            self.test_lose_health(self.obj, self.fn)
        if self.fn.__name__ == "gain_health":
            self.test_gain_health(self.obj, self.fn)
        if self.fn.__name__ == "restore":
            self.test_restore(self.obj, self.fn)
        
        print("------------------")
    
    def __repr__(self):
        return "A test instance for the {function} function of the {class_name} class".format(function=self.fn.__name__, class_name=self.obj.__class__.__name__)

    def test_lose_health(self, obj, fn):
        print("\n--TESTING: LOSE HEALTH") 
        
        print("-Losing health without getting knocked out")
        print(self.obj)
        self.obj.lose_health(50)
        print(self.obj)
  
        print("\n-Losing enough health to get knocked out")
        print(self.obj)
        self.obj.lose_health(50)
        print(self.obj)

        print("\n-Losing enough health to get knocked out, overkill")
        self.obj.p_health = 50
        self.obj.p_status["knocked out"] = False
        print(self.obj)
        self.obj.lose_health(100)
        print(self.obj)

    def test_gain_health(self, obj, fn):
        print("\n--TESTING: GAIN HEALTH")
        print("-Attempting gain health on a knocked out pokemon")
        self.obj.p_health = 0
        self.obj.p_status["knocked out"] = True
        print(self.obj)
        self.obj.gain_health(50)
        print(self.obj)
        
        print("\n-Attempting gain health on a non knocked out pokemon")
        self.obj.p_status["knocked out"] = False
        print(self.obj)
        self.obj.gain_health(50)
        print(self.obj)
        
        print("\n-Attempting gain health on a non knocked out pokemon, overhealing")
        print(self.obj)
        self.obj.gain_health(75)
        print(self.obj)

    def test_restore(self, obj, fn):
        print("\n--TESTING: RESTORE")
        print("-Attempting restore on a knocked out pokemon")
        self.obj.p_health = 0
        self.obj.p_status["knocked out"] = True
        print(self.obj)
        self.obj.restore()
        print(self.obj)
        
        print("\n-Atempting restore on a not knocked out Pokemon")
        print(self.obj)
        self.obj.restore()
        print(self.obj)
    