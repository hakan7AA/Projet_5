CREATE TABLE Categories (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(155) NOT NULL,
                PRIMARY KEY (id)
);


CREATE TABLE Products (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(155) NOT NULL,
                codebar VARCHAR(13) NOT NULL,
                url VARCHAR(155) NOT NULL,
                nutriscore INT NOT NULL,
                category_id INT NOT NULL,
                PRIMARY KEY (id)
);


CREATE TABLE Alternatives (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(155) NOT NULL,
                code_barre BIGINT NOT NULL,
                url VARCHAR(155) NOT NULL,
                nutriscore INT NOT NULL,
                product_id INT NOT NULL,
                PRIMARY KEY (id)
);


CREATE TABLE P_Registered (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(155) NOT NULL,
                code_barre BIGINT NOT NULL,
                url VARCHAR(155) NOT NULL,
                nutriscore INT NOT NULL,
                registered_category_id INT NOT NULL,
                PRIMARY KEY (id)
);


CREATE TABLE Registered (
                id INT AUTO_INCREMENT NOT NULL,
                url VARCHAR(155) NOT NULL,
                name VARCHAR(155) NOT NULL,
                code_barre BIGINT NOT NULL,
                nutriscore INT NOT NULL,
                registered_product_id INT NOT NULL,
                PRIMARY KEY (id)
);


ALTER TABLE Products ADD CONSTRAINT categories_products_fk
FOREIGN KEY (category_id)
REFERENCES Categories (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE Alternatives ADD CONSTRAINT products_alternatives_fk
FOREIGN KEY (product_id)
REFERENCES Products (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE P_Registered ADD CONSTRAINT categories_p_registered_fk
FOREIGN KEY (registered_category_id)
REFERENCES Categories (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE Registered ADD CONSTRAINT p_registered_registered_fk
FOREIGN KEY (registered_product_id)
REFERENCES P_Registered (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;