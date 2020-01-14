import requests
from config import CATEGORIES
from classes.database import Database


class Api:
    """This class is used for every interaction with api,
    config file and database."""
    @staticmethod
    def get_products(name):
        """Return a list of products taken from Api."""
        url = "https://fr.openfoodfacts.org/cgi/search.pl?action=" + \
              "process&search_terms=" + name + "&sort_by=" + \
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
    def insert_attribute():
        """Restart the get_products function as many times as
        the number of product categories and insert the products
        and alternatives in the product table"""
        database = Database()
        api = Api()
        category = CATEGORIES
        for number, name in category:
            products = api.get_products(name)
            all_products = products[:67]
            for product in all_products:
                data = (product['product_name'],
                        product['_id'], product['url'],
                        product['nutriments']['nutrition-score-fr'],
                        number)
                database.insert_products(data)
            all_alternatives = products[-91:]
            for alternative in all_alternatives:
                data = (alternative['product_name'],
                        alternative['_id'], alternative['url'],
                        alternative['nutriments']['nutrition-score-fr'],
                        number)
                database.insert_alternative(data)


API = Api()
