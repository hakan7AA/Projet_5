# !/env/bin/usr python3
# coding: utf-8

from classes.display import Display
from classes.database import Database
from classes.api import Api
from config import CATEGORIES


class Insert:
    """This class is used one times before the launch of programme.
    It's to recover the data."""

    def __init__(self):
        """Create a condition for all requirement."""
        database = Database()
        registered = database.get_categories()
        if not registered:
            database.insert_categories()
            self.all_functions()

        if registered:
            pass

    def all_functions(self):
        """Call all functions."""
        self.biscuits()
        self.pizzas()
        self.fromage()
        self.purees()
        self.poissons()
        self.pains()
        self.confitures()
        self.yaourts()
        self.jusdOrange()
        self.salades()
        self.altern_biscuits()
        self.altern_pizzas()
        self.altern_fromages()
        self.altern_purees()
        self.altern_poissons()
        self.altern_pains()
        self.altern_confitures()
        self.altern_yaourts()
        self.altern_jusdOrange()
        self.altern_salades()

    def biscuits(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each product belonging
        to biscuits category into Product table."""
        api = Api()
        database = Database()
        products = api.get_biscuits_products()
        for product in products:
            data = (product['product_name'], product['_id'], product['url'],
                    product['nutriments']['nutrition-score-fr'], 1)
            database.insert_products(data)

    def pizzas(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each product belonging
        to pizzas category into Product table."""
        api = Api()
        database = Database()
        products = api.get_pizzas_products()
        for product in products:
            data = (product['product_name'], product['_id'], product['url'],
                    product['nutriments']['nutrition-score-fr'], 2)
            database.insert_products(data)

    def fromage(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each product belonging
        to cheese category into Product table."""
        api = Api()
        database = Database()
        products = api.get_fromages_products()
        for product in products:
            data = (product['product_name'], product['_id'], product['url'],
                    product['nutriments']['nutrition-score-fr'], 3)
            database.insert_products(data)

    def purees(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each product belonging
        to mash potatoes category into Product table."""
        api = Api()
        database = Database()
        products = api.get_purees_products()
        for product in products:
            data = (product['product_name'], product['_id'], product['url'],
                    product['nutriments']['nutrition-score-fr'], 4)
            database.insert_products(data)

    def poissons(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each product belonging
        to fish category into Product table."""
        api = Api()
        database = Database()
        products = api.get_poissons_products()
        for product in products:
            data = (product['product_name'], product['_id'], product['url'],
                    product['nutriments']['nutrition-score-fr'], 5)
            database.insert_products(data)

    def pains(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each product belonging
        to breads category into Product table."""
        api = Api()
        database = Database()
        products = api.get_pains_products()
        for product in products:
            data = (product['product_name'], product['_id'], product['url'],
                    product['nutriments']['nutrition-score-fr'], 6)
            database.insert_products(data)

    def confitures(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each product belonging
        to jams category into Product table."""
        api = Api()
        database = Database()
        products = api.get_confitures_products()
        for product in products:
            data = (product['product_name'], product['_id'], product['url'],
                    product['nutriments']['nutrition-score-fr'], 7)
            database.insert_products(data)

    def yaourts(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each product belonging
        to yaourts category into Product table."""
        api = Api()
        database = Database()
        products = api.get_yaourts_products()
        for product in products:
            data = (product['product_name'], product['_id'], product['url'],
                    product['nutriments']['nutrition-score-fr'], 8)
            database.insert_products(data)

    def jusdOrange(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each product belonging
        to jusdOrange category into Product table."""
        api = Api()
        database = Database()
        products = api.get_jus_dOrange_products()
        for product in products:
            data = (product['product_name'], product['_id'], product['url'],
                    product['nutriments']['nutrition-score-fr'], 9)
            database.insert_products(data)

    def salades(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each product belonging
        to salades category into Product table."""
        api = Api()
        database = Database()
        products = api.get_salades_products()
        for product in products:
            data = (product['product_name'], product['_id'], product['url'],
                    product['nutriments']['nutrition-score-fr'], 10)
            database.insert_products(data)

    def altern_biscuits(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each alternatives belonging
        to biscuits category into Product table."""
        api = Api()
        database = Database()
        alternatives = api.get_biscuits_alternatives()
        for alternative in alternatives:
            data = (alternative['product_name'], alternative['_id'],
                    alternative['url'], alternative['nutriments']
                    ['nutrition-score-fr'], 1)
            database.insert_alternative(data)

    def altern_pizzas(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each alternatives belonging
        to pizzas category into Product table."""
        api = Api()
        database = Database()
        alternatives = api.get_pizzas_alternatives()
        for alternative in alternatives:
            data = (alternative['product_name'], alternative['_id'],
                    alternative['url'], alternative['nutriments']
                    ['nutrition-score-fr'], 2)
            database.insert_alternative(data)

    def altern_fromages(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each alternatives belonging
        to cheese category into Product table."""
        api = Api()
        database = Database()
        alternatives = api.get_fromages_alternatives()
        for alternative in alternatives:
            data = (alternative['product_name'], alternative['_id'],
                    alternative['url'], alternative['nutriments']
                    ['nutrition-score-fr'], 3)
            database.insert_alternative(data)

    def altern_purees(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each alternatives belonging
        to mash potatoes category into Product table."""
        api = Api()
        database = Database()
        alternatives = api.get_purees_alternatives()
        for alternative in alternatives:
            data = (alternative['product_name'], alternative['_id'],
                    alternative['url'], alternative['nutriments']
                    ['nutrition-score-fr'], 4)
            database.insert_alternative(data)

    def altern_poissons(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each alternatives belonging
        to fish category into Product table."""
        api = Api()
        database = Database()
        alternatives = api.get_poissons_alternatives()
        for alternative in alternatives:
            data = (alternative['product_name'], alternative['_id'],
                    alternative['url'], alternative['nutriments']
                    ['nutrition-score-fr'], 5)
            database.insert_alternative(data)

    def altern_pains(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each alternatives belonging
        to breads category into Product table."""
        api = Api()
        database = Database()
        alternatives = api.get_pains_alternatives()
        for alternative in alternatives:
            data = (alternative['product_name'], alternative['_id'],
                    alternative['url'], alternative['nutriments']
                    ['nutrition-score-fr'], 6)
            database.insert_alternative(data)

    def altern_confitures(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each alternatives belonging
        to jams category into Product table."""
        api = Api()
        database = Database()
        alternatives = api.get_confitures_alternatives()
        for alternative in alternatives:
            data = (alternative['product_name'], alternative['_id'],
                    alternative['url'], alternative['nutriments']
                    ['nutrition-score-fr'], 7)
            database.insert_alternative(data)

    def altern_yaourts(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each alternatives belonging
        to yaourts category into Product table."""
        api = Api()
        database = Database()
        alternatives = api.get_yaourts_alternative()
        for alternative in alternatives:
            data = (alternative['product_name'], alternative['_id'],
                    alternative['url'], alternative['nutriments']
                    ['nutrition-score-fr'], 8)
            database.insert_alternative(data)

    def altern_jusdOrange(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each alternatives belonging
        to jusdOrange category into Product table."""
        api = Api()
        database = Database()
        alternatives = api.get_jus_dOrange_alternatives()
        for alternative in alternatives:
            data = (alternative['product_name'], alternative['_id'],
                    alternative['url'], alternative['nutriments']
                    ['nutrition-score-fr'], 9)
            database.insert_alternative(data)

    def altern_salades(self):
        """This function insert product_name, code_barre,
        url, nutrition_score and category_id of each alternatives belonging
        to salades category into Product table."""
        api = Api()
        database = Database()
        alternatives = api.get_salades_alternatives()
        for alternative in alternatives:
            data = (alternative['product_name'], alternative['_id'],
                    alternative['url'], alternative['nutriments']
                    ['nutrition-score-fr'], 10)
            database.insert_alternative(data)


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
                        database.get_products_registered(alternative[2])
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
            print('Here is no product.')
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
