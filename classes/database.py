from config import CATEGORIES
import mysql.connector
from secret_code import Host, User, Passwd


class Database:
    """This class is used for every interaction with the database,
        even creating it if it doesn't exist yet."""

    def __init__(self):
        """Create the connector and
           all required elements if they don't exist yet
            """
        self.connector = mysql.connector.connect(host=Host,
                                                 user=User,
                                                 passwd=Passwd
                                                 )

        self.icursor = self.connector.cursor()
        self.create_database()
        self.create_table_categories()
        self.create_table_products()
        self.create_table_alternative()
        self.create_table_products_registered()
        self.create_table_registered()

    def create_database(self):
        """Create database if it doesn't exist, then update the connector."""
        self.icursor.execute('CREATE DATABASE IF NOT EXISTS Proj_5')

        self.connector = mysql.connector.connect(host=Host,
                                                 user=User,
                                                 passwd=Passwd,
                                                 database='Proj_5',
                                                 buffered=True
                                                 )

        self.icursor = self.connector.cursor()

    def create_table_categories(self):
        """Create the table Categories if it doesn't exist."""

        table = "CREATE TABLE IF NOT EXISTS Categories" + \
                "(id INTEGER(2) PRIMARY KEY NOT NULL," + \
                "name VARCHAR(155) NOT NULL)"

        self.icursor.execute(table)

    def get_categories(self):
        """Return all the categories."""
        select = "SELECT * FROM Categories"
        self.icursor.execute(select)
        fetch = self.icursor.fetchall()
        return fetch

    def insert_categories(self):
        """Insert the different categories in the
        table 'Categories' if its doesn't insert yet."""
        already_insert = self.get_categories()
        if not already_insert:
            insert = "INSERT INTO Categories (id, name) VALUES (%s, %s)"
            self.icursor.executemany(insert, CATEGORIES)
            self.connector.commit()

    def get_saved_categories(self):
        """Return categories that have a registered product."""
        select_join = "SELECT DISTINCT Categories.id, Categories.name " +\
                      "FROM Categories " +\
                      "INNER JOIN P_Registered ON " +\
                      "Categories.id = P_Registered.registered_category_id "

        self.icursor.execute(select_join)
        fetch = self.icursor.fetchall()
        return fetch

    def create_table_products(self):
        """Create table Products if it doesn't exist yet."""
        table = "CREATE TABLE IF NOT EXISTS Products" + \
                "(id INTEGER(2) PRIMARY KEY NOT NULL AUTO_INCREMENT," + \
                "name VARCHAR(155)  NOT NULL," + \
                "codebar VARCHAR(13) NOT NULL," + \
                "url VARCHAR(255) NOT NULL," + \
                "nutriscore INTEGER(2) NOT NULL," + \
                "category_id INTEGER(2) NOT NULL," + \
                "CONSTRAINT fk_category FOREIGN KEY (category_id) " + \
                "REFERENCES Categories(id))"

        self.icursor.execute(table)

    def insert_products(self, data):
        """Insert values into Products table"""
        insert = "INSERT INTO Products (name, codebar, url, nutriscore, " +\
            "category_id) VALUES (%s, %s, %s, %s, %s)"
        self.icursor.execute(insert, data)
        self.connector.commit()

    def get_products_one(self, category):
        """Return the products that have a category_id = %s."""
        select = "SELECT * FROM Products WHERE category_id = %s"
        data = (category, )
        self.icursor.execute(select, data)
        fetch = self.icursor.fetchall()
        return fetch

    def create_table_alternative(self):
        """Create table Alternatives if it doesn't exist yet."""
        table = "CREATE TABLE IF NOT EXISTS Alternatives" +\
                "(id INTEGER(2) PRIMARY KEY NOT NULL AUTO_INCREMENT," +\
                "name VARCHAR(155) NOT NULL," +\
                "code_barre BIGINT(13) NOT NULL," +\
                "url VARCHAR(155) NOT NULL," +\
                "nutriscore INTEGER(2) NOT NULL," +\
                "product_id INTEGER(2) NOT NULL," +\
                "CONSTRAINT fk_product FOREIGN KEY (product_id)" +\
                "REFERENCES Products(id)" +\
                ")"
        self.icursor.execute(table)

    def insert_alternative(self, data):
        """Insert values into Alternatives table."""
        insert = "INSERT INTO Alternatives (name, code_barre, url, " +\
            "nutriscore, product_id) VALUES (%s, %s, %s, %s, %s)"
        self.icursor.execute(insert, data)
        self.connector.commit()

    def get_one_alternative(self, product):
        """Return the alternative products that
        have cat_id = %s and nutrition_score < %s."""
        select = "SELECT * FROM Alternatives WHERE " +\
            "product_id = %s AND nutriscore < %s"
        data = (product[5], (product[4]), )
        self.icursor.execute(select, data)
        fetch = self.icursor.fetchone()
        return fetch

    def create_table_products_registered(self):
        """Create table P_Registered if it doesn't exist yet."""
        table = "CREATE TABLE IF NOT EXISTS P_Registered" + \
                "(id INTEGER(2) PRIMARY KEY NOT NULL AUTO_INCREMENT," + \
                "name VARCHAR(155) NOT NULL," + \
                "code_barre BIGINT(13) NOT NULL," + \
                "url VARCHAR(155) NOT NULL," + \
                "nutriscore INTEGER(2) NOT NULL," + \
                "registered_category_id INTEGER(2) NOT NULL," + \
                "CONSTRAINT fk_re_cat FOREIGN KEY " +\
                "(registered_category_id) " +\
                "REFERENCES Categories(id)" + \
                ")"
        self.icursor.execute(table)

    def insert_products_registered(self, data_1):
        """Insert values into P_Registered table."""
        insert = "INSERT INTO P_Registered (name, code_barre, url, " +\
            "nutriscore, registered_category_id) VALUES (%s, %s, %s, %s, %s)"
        self.icursor.execute(insert, data_1)
        self.connector.commit()

    def get_products_registered(self, product):
        """Get the substitution of the given product."""
        select = "SELECT * FROM P_Registered WHERE code_barre = %s"
        data = (product,)
        self.icursor.execute(select, data)
        fetch = self.icursor.fetchone()
        return fetch

    def get_saved_products_registered(self, category):
        """Return registered products that have
        a registered alternative products."""
        select_join = "SELECT * FROM P_Registered " +\
                      "INNER JOIN Registered ON P_Registered.id = " +\
                      "Registered.registered_product_id " +\
                      "WHERE P_Registered.registered_category_id = %s"

        data = (category, )
        self.icursor.execute(select_join, data)
        fetch = self.icursor.fetchall()
        return fetch

    def create_table_registered(self):
        """Create table Registered if it doesn't exist yet."""
        table = "CREATE TABLE IF NOT EXISTS Registered" +\
                "(id INTEGER(2) PRIMARY KEY " +\
                "NOT NULL AUTO_INCREMENT," +\
                "name VARCHAR(155) NOT NULL," +\
                "code_barre BIGINT(13) NOT NULL," +\
                "url VARCHAR(155) NOT NULL," +\
                "nutriscore INTEGER(2) NOT NULL," +\
                "registered_product_id INTEGER(2) NOT NULL," +\
                "CONSTRAINT fk_registered_pro_id FOREIGN KEY " +\
                "(registered_product_id) " +\
                "REFERENCES P_Registered(id)" +\
                ")"
        self.icursor.execute(table)

    def insert_registered(self, data_2):
        """Insert values into Registered table."""
        insert = "INSERT INTO Registered (name, code_barre, url, " +\
            "nutriscore, registered_product_id) VALUES (%s, %s, %s, %s, %s)"
        self.icursor.execute(insert, data_2)
        self.connector.commit()

    def get_registered(self, alternative):
        """Get the substitution of the given product"""
        select = "SELECT * FROM Registered WHERE code_barre = %s"
        data = (alternative, )
        self.icursor.execute(select, data)
        fetch = self.icursor.fetchone()
        return fetch

    def get_saved_registered(self, product):
        """Get the substitution of the given product."""
        query = "SELECT * FROM Registered WHERE registered_product_id = %s"
        data = (product[0], )
        self.icursor.execute(query, data)
        fetch = self.icursor.fetchone()
        return fetch
