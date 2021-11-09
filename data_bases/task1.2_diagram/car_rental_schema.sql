CREATE TABLE if NOT EXISTS customers
(
    customer_id SERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL ,
    second_name VARCHAR(50) NOT NULL ,
    address_customer_id INT NOT NULL
);

CREATE TABLE if NOT EXISTS address
(
    address_id SERIAL NOT NULL PRIMARY KEY ,
    city_city_id INT NOT NULL,
    street VARCHAR(50),
    house VARCHAR(10)
);

CREATE TABLE if NOT EXISTS city
(
    city_id SERIAL NOT NULL PRIMARY KEY,
    city_name VARCHAR(50) NOT NULL ,
    city_code VARCHAR(10) UNIQUE NOT NULL
);

CREATE TABLE if NOT EXISTS phone
(
    phone_id SERIAL NOT NULL PRIMARY KEY,
    address_phone_id INT NOT NULL,
    phone_number VARCHAR(10),
    city_city_code VARCHAR(10) NOT NULL
);


CREATE TABLE if NOT EXISTS rent
(
    rent_id SERIAL NOT NULL PRIMARY KEY,
    car_car_id INT NOT NULL ,
    customers_customer_id INT NOT NULL,
    date_rent DATE NOT NULL ,
    period_renting INT NOT NULL
);

CREATE TABLE if NOT EXISTS car
(
    car_id SERIAL NOT NULL PRIMARY KEY,
    car_namber VARCHAR(20) UNIQUE NOT NULL,
    model_model_id INT NOT NULL,
    car_price double precision
);

CREATE TABLE if NOT EXISTS model
(
    model_id SERIAL NOT NULL PRIMARY KEY,
    brand_brand_id INT NOT NULL ,
    car_name VARCHAR(20) NOT NULL,
    engine_engine_id INT,
    transmission_transmission_id INT,
    color VARCHAR(50)
);

CREATE TABLE if NOT EXISTS brand
(
    brand_id INT PRIMARY KEY,
    brand_name VARCHAR(50)
);

CREATE TABLE if NOT EXISTS engine
(
    engine_id INT PRIMARY KEY,
    volume INT,
    injection VARCHAR(10)
);

CREATE TABLE if NOT EXISTS transmission
(
    transmission_id INT PRIMARY KEY,
    transmission_type VARCHAR(10)
);

CREATE TABLE if NOT EXISTS branch
(
    branch_id SERIAL NOT NULL PRIMARY KEY,
    address_branch_id INT NOT NULL
);

CREATE TABLE if NOT EXISTS car_branch
(
    car_car_id INT NOT NULL,
    branch_branch_id INT NOT NULL
);

ALTER TABLE customers ADD CONSTRAINT address_customer_id_fk FOREIGN KEY(address_customer_id) REFERENCES address (address_id);
ALTER TABLE address ADD CONSTRAINT city_city_id_fk FOREIGN KEY (city_city_id) REFERENCES city (city_id);
ALTER TABLE phone ADD CONSTRAINT address_phone_id_fk FOREIGN KEY (address_phone_id) REFERENCES address (address_id);
ALTER TABLE phone ADD CONSTRAINT city_city_code_fk FOREIGN KEY (city_city_code) REFERENCES city (city_code);
ALTER TABLE rent ADD CONSTRAINT car_car_id_fk FOREIGN KEY (car_car_id) REFERENCES car (car_id);
ALTER TABLE rent ADD CONSTRAINT customers_customer_id_fk FOREIGN KEY (customers_customer_id) REFERENCES customers (customer_id);
ALTER TABLE car ADD CONSTRAINT model_model_id_fk FOREIGN KEY (model_model_id) REFERENCES model (model_id);
ALTER TABLE model ADD CONSTRAINT brand_brand_id_fk FOREIGN KEY (brand_brand_id) REFERENCES brand (brand_id);
ALTER TABLE model ADD CONSTRAINT engine_engine_id_fk FOREIGN KEY (engine_engine_id) REFERENCES engine (engine_id);
ALTER TABLE model ADD CONSTRAINT transmission_transmission_id_fk FOREIGN KEY (transmission_transmission_id) REFERENCES transmission(transmission_id);
ALTER TABLE branch ADD CONSTRAINT address_branch_id_fk FOREIGN KEY (address_branch_id) REFERENCES address(address_id);
ALTER TABLE car_branch ADD CONSTRAINT car_car_id_fk FOREIGN KEY (car_car_id) REFERENCES car(car_id);
ALTER TABLE car_branch ADD CONSTRAINT branch_branch_id_fk FOREIGN KEY (branch_branch_id) REFERENCES branch(branch_id);
