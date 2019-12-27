import requests


class Api:
    """This class is used for the every interaction with Api."""
    @staticmethod
    def get_biscuits():
        """return a list of cookies taken from Api."""
        url = "https://fr.openfoodfacts.org/cgi/search.pl?action=" +\
            "process&search_terms=Biscuits&sort_by=unique" +\
            "_scans_n&page_size=500&json=1"
        request = requests.get(url)
        json = request.json()
        products = []
        min = 0
        max = 200
        while min < max:
            try:
                if (json['products'][min]['nutriments']
                    ['nutrition-score-fr'] and
                        json['products'][min]['product_name']):
                        products.append(json['products'][min])
            except KeyError:
                max += 1
            min += 1
        return products

    @staticmethod
    def get_biscuits_products():
        """Get the first seventy cookies."""
        api = Api()
        all_biscuits = api.get_biscuits()
        products_biscuits = all_biscuits[:70]
        return products_biscuits

    @staticmethod
    def get_biscuits_alternatives():
        """Get the last hundred and twenty three cookies."""
        api = Api()
        all_biscuits = api.get_biscuits()
        alternatives_biscuits = all_biscuits[-123:]
        return alternatives_biscuits

    @staticmethod
    def get_pizzas():
        """return a list of pizzas taken from Api."""
        url = "https://fr.openfoodfacts.org/cgi/search.pl?action=" +\
            "process&search_terms=Pizzas&sort_by=" +\
            "unique_scans_n&page_size=500&json=1"
        request = requests.get(url)
        json = request.json()
        products = []
        min = 0
        max = 200
        while min < max:
            try:
                if (json['products'][min]['nutriments']
                    ['nutrition-score-fr'] and
                        json['products'][min]['product_name']):
                        products.append(json['products'][min])
            except KeyError:
                max += 1
            min += 1
        return products

    @staticmethod
    def get_pizzas_products():
        """Get the first seventy pizzas."""
        api = Api()
        all_pizzas = api.get_pizzas()
        products_pizzas = all_pizzas[:70]
        return products_pizzas

    @staticmethod
    def get_pizzas_alternatives():
        """Get the last hundred and twenty three pizzas."""
        api = Api()
        all_pizzas = api.get_pizzas()
        alternatives_pizzas = all_pizzas[-122:]
        return alternatives_pizzas

    @staticmethod
    def get_fromages():
        """return a list of cheese taken from Api."""
        url = "https://fr.openfoodfacts.org/cgi/search.pl?action=" +\
            "process&search_terms=Fromages&sort_by=" +\
            "unique_scans_n&page_size=500&json=1"
        request = requests.get(url)
        json = request.json()
        products = []
        min = 0
        max = 200
        while min < max:
            try:
                if (json['products'][min]['nutriments']
                    ['nutrition-score-fr'] and
                        json['products'][min]['product_name']):
                        products.append(json['products'][min])
            except KeyError:
                max += 1
            min += 1
        return products

    @staticmethod
    def get_fromages_products():
        """Get the first seventy cheese."""
        api = Api()
        all_fromages = api.get_fromages()
        products_fromages = all_fromages[:70]
        return products_fromages

    @staticmethod
    def get_fromages_alternatives():
        """Get the last hundred and twenty three cheese."""
        api = Api()
        all_fromages = api.get_fromages()
        alternatives_fromages = all_fromages[-125:]
        return alternatives_fromages

    @staticmethod
    def get_purees():
        """return a list of mash potatoes taken from Api."""
        url = "https://fr.openfoodfacts.org/cgi/search.pl?action=" +\
            "process&search_terms=purees&sort_by=" +\
            "unique_scans_n&page_size=500&json=1"
        request = requests.get(url)
        json = request.json()
        products = []
        min = 0
        max = 200
        while min < max:
            try:
                if (json['products'][min]['nutriments']
                    ['nutrition-score-fr'] and
                        json['products'][min]['product_name']):
                        products.append(json['products'][min])
            except KeyError:
                max += 1
            min += 1
        return products

    @staticmethod
    def get_purees_products():
        """Get the first seventy mash potatoes."""
        api = Api()
        all_purees = api.get_purees()
        products_purees = all_purees[:70]
        return products_purees

    @staticmethod
    def get_purees_alternatives():
        """Get the last hundred and twenty three mash potatoes."""
        api = Api()
        all_purees = api.get_purees()
        alternatives_purees = all_purees[-114:]
        return alternatives_purees

    @staticmethod
    def get_poissons():
        """return a list of fish taken from Api."""
        url = "https://fr.openfoodfacts.org/cgi/search.pl?action=" +\
            "process&search_terms=Poissons&sort_by=" +\
            "unique_scans_n&page_size=500&json=1"
        request = requests.get(url)
        json = request.json()
        products = []
        min = 0
        max = 200
        while min < max:
            try:
                if (json['products'][min]['nutriments']
                    ['nutrition-score-fr'] and
                        json['products'][min]['product_name']):
                        products.append(json['products'][min])
            except KeyError:
                max += 1
            min += 1
        return products

    @staticmethod
    def get_poissons_products():
        """Get the first seventy fish."""
        api = Api()
        all_poissons = api.get_poissons()
        products_poissons = all_poissons[:70]
        return products_poissons

    @staticmethod
    def get_poissons_alternatives():
        """Get the last hundred and twenty three fish."""
        api = Api()
        all_poissons = api.get_poissons()
        alternatives_poissons = all_poissons[-95:]
        return alternatives_poissons

    @staticmethod
    def get_pains():
        """return a list of breads taken from Api."""
        url = "https://fr.openfoodfacts.org/cgi/search.pl?action=" +\
            "process&search_terms=Pains&sort_by=" +\
            "unique_scans_n&page_size=500&json=1"
        request = requests.get(url)
        json = request.json()
        products = []
        min = 0
        max = 200
        while min < max:
            try:
                if (json['products'][min]['nutriments']
                    ['nutrition-score-fr'] and
                        json['products'][min]['product_name']):
                        products.append(json['products'][min])
            except KeyError:
                max += 1
            min += 1
        return products

    @staticmethod
    def get_pains_products():
        """Get the first seventy breads."""
        api = Api()
        all_pains = api.get_pains()
        products_pains = all_pains[:70]
        return products_pains

    @staticmethod
    def get_pains_alternatives():
        """Get the last hundred and twenty three breads."""
        api = Api()
        all_pains = api.get_pains()
        alternatives_pains = all_pains[-91:]
        return alternatives_pains

    @staticmethod
    def get_confitures():
        """return a list of jams taken from Api."""
        url = "https://fr.openfoodfacts.org/cgi/search.pl?action=" +\
            "process&search_terms=Confitures&sort_by=" +\
            "unique_scans_n&page_size=500&json=1"
        request = requests.get(url)
        json = request.json()
        products = []
        min = 0
        max = 200
        while min < max:
            try:
                if (json['products'][min]['nutriments']
                    ['nutrition-score-fr'] and
                        json['products'][min]['product_name']):
                        products.append(json['products'][min])
            except KeyError:
                max += 1
            min += 1
        return products

    @staticmethod
    def get_confitures_products():
        """Get the first seventy jams."""
        api = Api()
        all_confitures = api.get_confitures()
        products_confitures = all_confitures[:70]
        return products_confitures

    @staticmethod
    def get_confitures_alternatives():
        """Get the last hundred and twenty three jams."""
        api = Api()
        all_confitures = api.get_confitures()
        alternatives_confitures = all_confitures[-129:]
        return alternatives_confitures

    @staticmethod
    def get_yaourts():
        """Return a list of yogurts taken from Api."""
        url = "https://fr.openfoodfacts.org/cgi/search.pl?action=" +\
            "process&search_terms=Yaourts&sort_by=" +\
            "unique_scans_n&page_size=500&json=1"
        request = requests.get(url)
        json = request.json()
        products = []
        min = 0
        max = 200
        while min < max:
            try:
                if (json['products'][min]['nutriments']
                    ['nutrition-score-fr'] and
                        json['products'][min]['product_name']):
                        products.append(json['products'][min])
            except KeyError:
                max += 1
            min += 1
        return products

    @staticmethod
    def get_yaourts_products():
        """Get the first seventy yogurts."""
        api = Api()
        all_yaourts = api.get_yaourts()
        products_yaourts = all_yaourts[:70]
        return products_yaourts

    @staticmethod
    def get_yaourts_alternative():
        """Get the last hundred and ten yogurts."""
        api = Api()
        all_yaourts = api.get_yaourts()
        alternatives_yaourts = all_yaourts[-110:]
        return alternatives_yaourts

    @staticmethod
    def get_jus_dOrange():
        """Return a list of Orange juice taken from Api."""
        url = "https://fr.openfoodfacts.org/cgi/search.pl?action=" +\
            "process&search_terms=jus%20d'Orange&sort_by=" +\
            "unique_scans_n&page_size=500&json=1"
        request = requests.get(url)
        json = request.json()
        products = []
        min = 0
        max = 200
        while min < max:
            try:
                if (json['products'][min]['nutriments']
                    ['nutrition-score-fr'] and
                        json['products'][min]['product_name']):
                        products.append(json['products'][min])
            except KeyError:
                max += 1
            min += 1
        return products

    @staticmethod
    def get_jus_dOrange_products():
        """Get the first seventy Orange juice."""
        api = Api()
        all_jus_dOrange = api.get_jus_dOrange()
        products_jus_dOrange = all_jus_dOrange[:70]
        return products_jus_dOrange

    @staticmethod
    def get_jus_dOrange_alternatives():
        """Get the last hundred and twenty nine Orange juice."""
        api = Api()
        all_jus_dOrange = api.get_jus_dOrange()
        alternatives_jus_dOrange = all_jus_dOrange[-129:]
        return alternatives_jus_dOrange

    @staticmethod
    def get_salades():
        """Return a list of salads taken from Api."""
        url = "https://fr.openfoodfacts.org/cgi/search.pl?action=" +\
            "process&search_terms=Salades&sort_by=" +\
            "unique_scans_n&page_size=500&json=1"
        request = requests.get(url)
        json = request.json()
        products = []
        min = 0
        max = 200
        while min < max:
            try:
                if (json['products'][min]['nutriments']
                    ['nutrition-score-fr'] and
                        json['products'][min]['product_name']):
                        products.append(json['products'][min])
            except KeyError:
                max += 1
            min += 1
        return products

    @staticmethod
    def get_salades_products():
        """Get the first seventy salads."""
        api = Api()
        all_salades = api.get_salades()
        products_salades = all_salades[:67]
        return products_salades

    @staticmethod
    def get_salades_alternatives():
        """Get the last hundred and fourteen salads."""
        api = Api()
        products = api.get_salades()
        alternatives_salades = products[-114:]
        return alternatives_salades
