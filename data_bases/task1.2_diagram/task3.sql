--Создать 3 представления
--(1 из них должно быть материализированным и хранить данные от "тяжелого" запроса).


--Find all branch info(city, address, phone) by id
CREATE OR REPLACE VIEW branch_info AS
    SELECT address.street||' '|| address.house AS full_address,
           city.city_name,
           phone.city_city_code||' '|| phone.phone_number AS branch_phone
        FROM branch
            JOIN address ON branch.address_branch_id = address.address_id
            JOIN city ON address.city_city_id =  city.city_id
            RIGHT JOIN phone ON address.address_id = phone.address_phone_id
        WHERE branch_id = 2
    GROUP BY full_address, city.city_name, city.city_code, branch_phone
;

SELECT * FROM branch_info;


--Find all customers rented cars at current branch
DROP MATERIALIZED VIEW branch_customers;

CREATE MATERIALIZED VIEW branch_customers AS
    SELECT customers.customer_id,
           customers.first_name|| ' ' ||customers.second_name as full_name
        FROM customers
            JOIN rent ON customers.customer_id = rent.customers_customer_id
            JOIN car ON rent.car_car_id = car.car_id
            JOIN car_branch ON car.car_id = car_branch.car_car_id
            JOIN branch ON car_branch.branch_branch_id = branch.branch_id
        WHERE branch.branch_id = 1
    GROUP BY customers.customer_id, full_name
WITH DATA
;

-- To make sure the data is not out of date - refresh data
REFRESH MATERIALIZED VIEW branch_customers;

SELECT * FROM branch_customers;


-- Calculation the number of rentals for a current car in specific period
CREATE OR REPLACE VIEW count_car_rent AS
    SELECT car.car_namber, car.car_price, count(rent.car_car_id)
        FROM car
            JOIN rent ON car.car_id = rent.car_car_id
        WHERE car.car_id = 2 and
              rent.date_rent BETWEEN '2020-01-30' AND '2021-11-30'
    GROUP BY car.car_namber, car.car_price
    ORDER BY count(rent.car_car_id) DESC
;

SELECT * FROM count_car_rent;