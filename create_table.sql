def create_database(self):
    """Create database if it doesn't exist, then update the connector."""
    self.icursor.execute('CREATE DATABASE IF NOT EXISTS Base_OCP_5')

    self.connector = mysql.connector.connect(host=Host,
                                             user=User,
                                             passwd=Passwd,
                                             database='Base_OCP_5',
                                             buffered=True
                                             )

    self.icursor = self.connector.cursor()


def create_table_categories(self):
    """Create the table Categories if it doesn't exist."""
    table = "CREATE TABLE IF NOT EXISTS Categories" + \
            "(id INTEGER(2) PRIMARY KEY NOT NULL," + \
            "name VARCHAR(155) NOT NULL)"
    self.icursor.execute(table)


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
