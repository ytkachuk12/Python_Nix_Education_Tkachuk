-- Написать 2 любые хранимые процедуры.
-- В них использовать транзакции для insert, update, delete.

-- Changes the coast of the car by the amount of the discount
-- takes discount(0 < discount < 1) and car_id
-- if discount not in proper amount - rollback
CREATE OR REPLACE PROCEDURE change_car_price(
    id INT,
    discount double precision
)
    LANGUAGE plpgsql
    AS
$$
    BEGIN
        if discount > 1 OR discount < 0 then
            raise notice 'Wrong discount. It should be 0 < discount < 1';
            rollback ;
        end if;

            UPDATE car SET
            car_price = car.car_price * discount
            WHERE car_id = id;

        commit ;
    END ;
$$;

call change_car_price(4, 0.9);


-- Insert values in the city table
CREATE OR REPLACE PROCEDURE insert_city_value(
    id INT,
    name VARCHAR(50),
    code VARCHAR(10)
)
    LANGUAGE plpgsql
    AS
$$
    declare
        check_id INT;
    BEGIN
        SELECT city_id
        INTO check_id
        FROM city
        WHERE city_id = id;

        if found then
            raise notice 'The city already in data base';
            rollback ;
        else
            INSERT INTO city(city_id, city_name, city_code)
            VALUES (id, name, code);
            commit ;
        end if;
    end;
$$;
end ;

CALL insert_city_value(11, 'new city', '0777');