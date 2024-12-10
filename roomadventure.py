from time import sleep

# Room CLass
class Room:

    # constructor
    def __init__(self, name: str):
        self.name = name

        self.exits: list['Room'] = []         # Room objects
        self.exit_locations: list[str] = []     # words like north south

        self.items: list[str] = []
        self.item_descriptions: list[str] = []

        self.grababbles: list[str] = []

    # getters and setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value


    @property
    def exit_locations(self):
        return self._exit_locations

    @exit_locations.setter
    def exit_locations(self, value):
        self._exit_locations = value


    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value


    @property
    def item_descriptions(self):
        return self._item_descriptions

    @item_descriptions.setter
    def item_descriptions(self, value):
        self._item_descriptions = value


    @property
    def grababbles(self):
        return self._grababbles

    @grababbles.setter
    def grababbles(self, value):
        self._grababbles = value

    # additional methods
    def add_exit(self, exit_location, exit_):
        self.exit_locations.append(exit_location)
        self.exits.append(exit_)

    def add_item(self, item_name:str, item_description):
        self.items.append(item_name)
        self.item_descriptions.append(item_description)

    def add_grababble(self, new_grababble):
        self.grababbles.append(new_grababble)

    def delete_grababble(self, existing_grababble):
        if existing_grababble in self.grababbles:
            self.grababbles.remove(existing_grababble)


    # __str__ functipn
    def __str__(self) -> str:
        result = ''

        # where we are
        result += f'Location {self.name}'

        # what we see
        if len(self.items) != 0:
            result += "You see:"
            for item in self.items:
                result += f" {item}"
            result += "\n"

        # exits available
        if len(self.exit_locations) != 0:
            result += "Exits:"
            for location in self.exit_locations:
                result += f" {location}"

        # return the result
        return result


# Create rooms function
def create_rooms(starting_room = 1):

    # create each room
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    rooms = [r1, r2, r3, r4]

    # add exits to each room
    r1.add_exit("east", r2)
    r1.add_exit("south", r3)

    r2.add_exit("west", r1)
    r2.add_exit("south", r4)

    r3.add_exit("east", r4)
    r3.add_exit("north", r1)

    r4.add_exit("west", r3)
    r4.add_exit("north", r2)
    r4.add_exit("south", None)

    # add items to each room
    r1.add_item("chair", "this chair has two legs. seems like it skipped leg day.")
    r1.add_item("table", "seems like it skipped chair day.")

    r2.add_item("rug", "it needs to be vacuumed.")
    r2.add_item("fireplace", "looks like it was recently used.")

    r3.add_item("bookshelves", "looks like someone was reading their fortnite strategy guide.")
    r3.add_item("statue", "looks like it skipped leg day.")

    r4.add_item("oven", "wonder what's for dinner. the oven obviously didn't skip leg day")
    

    # add grababbles to the rooms
    r1.add_grababble("key")
    
    r3.add_grababble("fortnite strategy guide")

    r4.add_grababble("bread")

    return rooms[starting_room - 1]

# Death
def death():
    print("You died.")


# Main Program
inventory = []
current_room = create_rooms()

while True:

    # kill the game if player dies
    if current_room == None:
        death()
        break

    status = "\n" + str(current_room)

    # include info about the inventory in the status
    if len(inventory) != 0:
        status += f"\nYou are carrying: "
        status += ', '.join(inventory)
    else:
        status += "\nYou have no items in your inventory"

    # inform the user of the current status
    print(status)

    # set the response to a default value
    response = "Invalid input. Try the format [verb] [noun]. \
        I only understand the verbs 'go', 'look', and \
        'take'.\nType 'quit' to quit."

    # ask for input from the user
    action = input("What would you like to do? ").lower()

    # quit if they wanted that
    if action in ["quit", "q", "exit", "byr", "adios", "ciao", "meesa out"]:
        break

    # process the input
    

    # split the input
    words = action.split()
    if len(words) == 2:
        verb = words[0]
        noun = words [1]

        # did they say go?
        if verb == "go":
            response = "Invalid exit"
            if noun in current_room.exit_locations:
                index = current_room.exit_locations.index(noun)
                current_room = current_room.exits[index]

        # did they say look?
        elif verb == "look":
            response = "That item doesn't exist here."
            if noun in current_room.items:
                index = current_room.items.index(noun)
                response = current_room.item_descriptions[index]

        # did they say take?
        elif verb == "take":
            response = "That's not something I can take."
            if noun in current_room.grababbles:
                inventory.append(noun)
                current_room.delete_grababble(noun)
                response - f"Grabbed {noun}"

    # print the response
    print("\n" + response)
    sleep(1)