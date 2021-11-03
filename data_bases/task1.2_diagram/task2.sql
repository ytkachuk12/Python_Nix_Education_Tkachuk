--Find all customer info(name, surname, address, phone) by id
EXPLAIN SELECT customers.first_name||' '||customers.second_name AS full_name,
       address.street||' '|| address.house AS full_address,
       city.city_name,
       phone.city_city_code||' '|| phone.phone_number AS customer_phone
    FROM customers
        JOIN address ON customers.address_customer_id = address.address_id
        JOIN city ON address.city_city_id =  city.city_id
        RIGHT JOIN phone ON address.address_id = phone.address_phone_id
    WHERE customer_id = 2
GROUP BY full_name, full_address, city.city_name, city.city_code, customer_phone
;

CREATE INDEX idx_Customers_first_name_second_name ON customers(first_name, second_name);
CREATE INDEX idx_Address_street_house_city_city_id ON address(street, house, city_city_id);
CREATE INDEX idx_Phone_phone_number ON phone(phone_number);


--find all customers rented all cars with current brand and model in current time period
SELECT customers.first_name||' '||customers.second_name AS full_name
    FROM customers
        JOIN rent ON customers.customer_id = rent.customers_customer_id
        JOIN car ON rent.car_car_id = car.car_id
        JOIN model ON car.model_model_id = model.model_id
        JOIN brand ON model.brand_brand_id = brand.brand_id
    WHERE brand.brand_name = 'brand11'
        AND model.car_name = 'car_name1'
        AND rent.date_rent BETWEEN '2020-03-30' AND '2021-04-30'
GROUP BY full_name
ORDER BY full_name
;

CREATE INDEX idx_rent_date_rent ON rent(date_rent);
CREATE INDEX idx_Brand_brand_name ON brand(brand_name);
CREATE INDEX idx_Model_car_name ON model(car_name);


--Find all cars(number and price) and engine description that has current engine (engine_id)
SELECT car.car_namber, car.model_model_id, car.car_price, engine.volume, engine.injection
    FROM car
        JOIN model ON car.model_model_id = model.model_id
        JOIN engine ON model.engine_engine_id = engine.engine_id
    WHERE engine.engine_id = 2
GROUP BY car.car_namber, car.model_model_id, car.car_price, engine.volume, engine.injection
ORDER BY car.car_price
;

CREATE INDEX idx_Car_car_namber_car_price ON car(car_namber, car_price);
