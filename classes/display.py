from config import CATEGORIES


class Display:
    """This class is used for every display."""
    def __init__(self):
        """Contains the first display."""
        self.display_separator()
        print("Welcome to EatMoreHealthy !")
        print("1 - What food do you want to replace ?")
        print("2 - Find my saved substitute Food.")

    def display_separator(self):
        """Display for spacing."""
        print("_____________________________________"
              "_______________________________________________")
        print(" ")
        print("---------------------------------------"
              "----------------------------------------------")

    def display_input(self):
        """Return a question that request to choose an action."""
        choice = input("Choose a number for an action "
                       "or 'Home' to return to the main menu : ")
        return choice

    def display_categories(self):
        """Show list of different categories of product."""
        self.display_separator()
        print("Here are the different product categories.")
        print("Choose a category number to see its products.")
        for i, category in enumerate(CATEGORIES):
            print(i + 1, category[1])

    def display_products(self, products):
        """Show list the different product."""
        self.display_separator()
        print("Here are the products belonging to this category.")
        print("Choose a product number to find a "
              "substitute for it or 'home' to return to the main menu.")
        for i, product in enumerate(products):
            print(i + 1, product[1])

    def display_alternative(self, product, alternative):
        """Show an alternative for chosen product."""
        self.display_separator()
        print('The chosen product is :', product[1])
        print('His nutriscore is :', product[4])
        print('Here is the link to consult this product :')
        print(product[3])
        print('Replace it with :', alternative[1])
        print('His nutriscore is :', alternative[4])
        print('Here is the link to consult this product :')
        print(alternative[3])
        print('Choose 1 to save it.')

    def display_saved_categories(self, categories):
        """Show list of categories that contains saved product."""
        self.display_separator()
        print("Here is the different product categories.")
        print("Choose a category number to see its "
              "saved products or 'home' to return to the main menu.")
        for i, category in enumerate(categories):
            print(i + 1, category[1])

    def display_saved_products(self, products):
        """Show list of saved product contains saved alternative product."""
        self.display_separator()
        print("Here are the product containing saved alternative products.")
        print("Choose a product number to find a saved "
              "alternative product or 'home' to return to the main menu.")
        for i, product in enumerate(products):
            print(i + 1, product[1])

    def display_saved_alternatives(self, product, alternative):
        """Show saved alternative product belonging to chosen product."""
        self.display_separator()
        print("The chosen product is :", product[1])
        print("His nutriscore is :", product[4])
        print("Here is the link to consult this product :")
        print(product[3])
        print("His alternative product is :", alternative[1])
        print("His nutriscore is :", alternative[4])
        print("Here is the link to consult this alternative productsss :")
        print(alternative[3])
