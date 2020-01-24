# !/env/bin/usr python3
# coding: utf-8

from classes.display import Display
from classes.database import Database
from classes.api import Api
from config import CATEGORIES


class Insert:
    """This class is used one times before the launch of programme.
    It is to insert the data."""

    def __init__(self):
        """Create a condition for insertion."""
        database = Database()
        api = Api()
        registered = database.get_categories()
        if not registered:
            database.insert_categories()
            api.insert_attribute()
        else:
            pass


class Main:
    """This class is used to launch the programme."""
    def __init__(self):
        """Contains question, then two choice for start."""
        display = Display()
        next_step = False
        while not next_step:
            next_step = True
            choice = input("Choose a number for an action : ")
            try:
                if choice == '1':
                    self.select_categories(display)
                elif choice == '2':
                    self.select_saved_categories(display)
                else:
                    print("Incorrect choice, please try again.")
                    next_step = False
            except ValueError:
                print("Incorrect choice, please try again.")
                next_step = False

    def select_categories(self, display):
        """Show the different categories of product and request to choose."""
        display.display_categories()
        next_step = False
        while not next_step:
            next_step = True
            choice = display.display_input()
            if choice == 'Home':
                print("Back to the main menu.")
                self.__init__()
            try:
                if int(choice) - 1 in range(len(CATEGORIES)):
                    self.select_products(display, CATEGORIES[int(choice) - 1])

                else:
                    print("Incorrect choice, please try again.")
                    next_step = False
            except ValueError:
                print("Incorrect choice, please try again.")
                next_step = False

    def select_products(self, display, category):
        """Show the different product belonging to
        his categories and request to choose."""
        database = Database()
        products = database.get_products_one(category[0])
        display.display_products(products)
        next_step = False
        while not next_step:
            next_step = True
            choice = display.display_input()
            if choice == "Home":
                print("Back to the main menu.")
                self.__init__()
            try:
                if int(choice) - 1 in range(len(products)):
                    self.select_alternative(
                        display, products[int(choice) - 1],
                        database)
                else:
                    print("Incorrect choice, please try again.")
                    next_step = False

            except ValueError:
                print("Incorrect choice, please try again.")
                next_step = False

    def select_alternative(self, display, product, database):
        """Show an alternative product belonging
        to chosen product and ask for choice."""
        alternative = database.get_one_alternative(product)
        if alternative:
            display.display_alternative(product, alternative)
            next_step = False
            while not next_step:
                next_step = True
                choice = input("Choose '1' to save it or "
                               "'Home' to return to the main menu :")
                if choice == "Home":
                    print('Back to the main menu.')
                    self.__init__()

                elif choice == '1':
                    alternative_already_insert =\
                        database.get_products_registered(product[2])
                    if not alternative_already_insert:
                        data_1 = (product[1], product[2],
                                  product[3], product[4], product[5])
                        database.insert_products_registered(data_1)
                        products = database.get_products_registered(product[2])
                        data_2 = (alternative[1], alternative[2],
                                  alternative[3], alternative[4], products[0])
                        database.insert_registered(data_2)
                        print("Your product has been registered.")
                        print("Back to the main menu")
                        self.__init__()

                    if alternative_already_insert:
                        print("This product is already registered")
                        print("Back to the main menu")
                        self.__init__()
                else:
                    print("Incorrect choice, please try again.")
                    next_step = False

        else:
            print("Sorry no substitute product found.")
            print('Back to the main menu.')
            self.__init__()

    def select_saved_categories(self, display):
        """Show the different registered categories
        of product and request to choose."""
        database = Database()
        categories = database.get_saved_categories()
        if categories:
            display.display_saved_categories(categories)
            next_step = False
            while not next_step:
                next_step = True
                choice = display.display_input()
                if choice == "Home":
                    print("Back to the main menu.")
                    self.__init__()
                try:
                    if int(choice) - 1 in range(len(categories)):
                        self.select_saved_products(
                            display, categories[int(choice) - 1])
                    else:
                        print("Incorrect choice, please try again.")
                        next_step = False
                except ValueError:
                    print("Incorrect choice, please try again.")
                    next_step = False
        if not categories:
            print('There is no registered product.')
            print('Back to the main menu.')
            self.__init__()

    def select_saved_products(self, display, category):
        """Show the different registered product
        belonging to his categories and request to choose."""
        database = Database()
        products = database.get_saved_products_registered(category[0])
        if products:
            display.display_saved_products(products)
            next_step = False
            while not next_step:
                next_step = True
                choice = display.display_input()
                if choice == "Home":
                    print("Back to the main menu.")
                    self.__init__()
                try:
                    if int(choice) - 1 in range(len(products)):
                        self.select_saved_registered(
                            display, products[int(choice) - 1])
                    else:
                        print("Incorrect choice, please try again.")
                        next_step = False
                except ValueError:
                    print("Incorrect choice, please try again.")
                    next_step = False

        if not products:
            print("Sorry, you have not saved a product for this category.")
            print("Back to the main menu.")
            self.__init__()

    def select_saved_registered(self, display, product):
        """Show registered alternative product belonging to chosen product."""
        database = Database()
        alternative = database.get_saved_registered(product)
        display.display_saved_alternatives(product, alternative)
        next_step = False
        while not next_step:
            next_step = True
            choice = input("Choose 'Home' to return to the main menu : ")
            if choice == "Home":
                print("Back to the main menu.")
                self.__init__()
            else:
                print("Incorrect choice, please try again.")
                next_step = False
        if not alternative:
            print("Sorry, you have not saved "
                  "alternative product for this product.")
            print("Back to the main menu.")
            self.__init__()


if __name__ == "__main__":
    INSERT = Insert()
    MAIN = Main()
