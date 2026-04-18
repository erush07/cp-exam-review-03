from helper_functions import clear_screen
clear_screen()

# ===========
# PEEWEE CRUD
# ===========


# 1. CREATE A PEEWEE MODEL AND SQLITE DATABASE
# Create a SQLite Database called cats.db through peewee
'''
It should have the following columns:
    - cat_id (the primary key)
    - cat_name
    - cat_age
    - owner_name
'''
from peewee import *

db = SqliteDatabase("cats.db")

class Cat(Model):
    cat_id = AutoField(primary_key = True)
    cat_name = TextField()
    cat_age = IntegerField()
    owner_name = TextField()

    class Meta:
        database = db

    @classmethod
    def create(cls, **query):
        cat_name = query.get("cat_name", "")
        cat_name = cat_name.title().strip()
        cat_age = query.get("cat_age", "")
        owner_name = query.get("owner_name", "")
        owner_name = owner_name.title().strip()

        return super().create(**query)

    def get_info(self):
        return f"Cat: {self.cat_name} Age: {self.cat_age} Owner: {self.owner_name}"

# 2. CREATE A ROW USING INPUTS
# Ask the user for inputs for the cat_name, owner_name, and age to create new rows
# in the database
menu = "Opition 1: add a new cat" \
        "\nOption 2: show all cats" \
        "\nOption 3: Search by Owner" \
        "\nOption 4: get info for all cats" \
        "\nOption 5: Rename Cat" \
        "\nOption 6: Delete Cat" \
        "\nOption 7: Exit"
option = input("Choose an option (1-6, or exit): ")

while True:
    print(menu)
    if option == "1":
        cat_name_input = input("What is the name of your cat? ")
        cat_age_input = int(input("How old is your cat? "))
        owner_name_input = input("Enter the owner's (your) name: ")
        cat_obj = Cat.create(cat_name = cat_name_input, cat_age = cat_age_input, owner_name = owner_name_input)
    elif option == "2": # Show all cats ordered by name desc
        all_cats = Cat.select().order_by(Cat.cat_name.desc())
        for cat_obj in all_cats:
            print(cat_obj.cat_name)
    elif option == "3": # search by owner
        owner_name_input = int(input("Input the name of the cat's owner: "))
        cat_obj = Cat.get().where(owner_name = owner_name_input) #what to do if owner has more than one cat...
        if cat_obj == None:
            print("Owner not in database.")
        elif cat_obj != None:
            print()
    elif option == "4": # get info for all cats
        all_cats = Cat.select()
        for cat_obj in all_cats:
            print(cat_obj.get_info())
    elif option == "5": # rename cat
        cat_id_input = int(input("Input the id of the cat you'd like to rename: "))
        cat_obj = Cat.get_by_id(cat_id_input)
    elif option == "6": # Delete cat
        cat_id_input = int(input("Input the id of the cat you'd like to delete: "))
        cat_obj = Cat.get_by_id(cat_id_input)
    elif option == "7":
        print("Goodbye! Thanks for using our program :)")
        print()
        exit()

# 3. OVERRIDE THE CREATE FUNCTION
# Override the create function to make sure that every cat_name and
# owner_name gets stored as a capitalized version. (e.g. "max" or "MAX" should
# be stored as "Max") Don't stop anything from being created, just make it so
# the first letter is capitalized and that it is stored without leading or
# trailing spaces.

#DONE :)

# 4. ADD A GET_INFO METHOD TO THE CAT CLASS
# In your Cat class, add a method called "get_info" that returns the
# cat's name, owner name and age in a nicely formatted string.

#DONE :)


# 5. MAKE A MENU AND ADD A READ OPTION
# Make a menu. Option 1 is to add a new cat (for what you did in #1)
# Option 2 is to see all cats. When option 2 is selected, make it so that the
# cats print out in reverse alphabetical order by cat_name. The menu should
# repeat until the user enters "exit"




# 6. READ A SPECIFIC SUBSET (OPTION 3)
# Add option 3. Option 3 should ask for an owner's name. If the owner name
# exists, make it show all the cats with that owner_name. If the owner_name
# doesn't exist in the database, display a message that that owner couldn't be
# found, and go back to the menu.



# 6. FIND THE YOUNGEST CAT (OPTION 4)
# Add option 4. Option 4 should display the the get_info of the youngest cat 
# in the database. For simplicity, if there is a tie for the youngest, you 
# can just display one. (If you want a little extra challenge, feel free to
# try and write code that accounts for a tie for youngest age)


# 7. UPDATE A ROW  (OPTION 5)
# Add option 5. Enter a cat's id to get it, then enter a new name, and save
# that name. For time's sake you can assume the Id entered will always be valid


# 8. DELETE A ROW (OPTION 6)
# Add option 6. Enter a cat's id to get it, then delete it. Print out a
# message that it was deleted.
