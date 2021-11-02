CREATE TABLE if NOT EXISTS Carts
(
    cart_id INT NOT NULL PRIMARY KEY,
    Users_user_id INT NOT NULL,
    subtotal DECIMAL,
    total DECIMAL,
    timestamp TIMESTAMP(2),
    FOREIGN KEY (Users_user_id) REFERENCES Users(user_id)
);


CREATE TABLE if NOT EXISTS Order_status
(
    order_status_id INT NOT NULL PRIMARY KEY,
    status_name VARCHAR(255) NOT NULL
);


CREATE TABLE if NOT EXISTS Users
(
    user_id serial NOT NULL PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    middle_name VARCHAR(255),
    if_staff SMALLINT,
    country VARCHAR(255),
    city VARCHAR(255),
    address TEXT
);


CREATE TABLE if not exists Orders
(
    order_id serial NOT NULL PRIMARY KEY,
    Carts_cart_id INT NOT NULL,
    Order_status_order_status_id INT NOT NULL,
    shipping_total DECIMAL,
    total DECIMAL,
    created_at TIMESTAMP(2),
    updated_at TIMESTAMP(2),
    FOREIGN KEY (Carts_cart_id) REFERENCES Carts(cart_id),
    FOREIGN KEY (Order_status_order_status_id) REFERENCES Order_status(order_status_id)
);



CREATE TABLE Products
(
    product_id INT PRIMARY KEY NOT NULL,
	product_title VARCHAR(255),
	product_description TEXT,
	in_stock INT,
	price FLOAT,
	slug VARCHAR(45),
	category_id INT,
	FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);



CREATE TABLE if NOT EXISTS Cart_product
(
    carts_cart_id INT,
    products_product_id INT,
    FOREIGN KEY (Carts_cart_id) REFERENCES Carts(cart_id),
    FOREIGN KEY (Products) REFERENCES Products(product_id)
);



CREATE TABLE Categories
(
    category_id INTEGER PRIMARY KEY NOT NULL,
	category_title VARCHAR(255),
	category_description TEXT
);

