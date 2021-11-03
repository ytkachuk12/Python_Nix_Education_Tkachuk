-- Создать 2 функции
-- (одна из них должна возвращать таблицу,
-- одна из них должна использовать циклы, одна из них должна использовать курсор).


-- Returns a table containing the customers rents
-- (rent_id, car_id, date and total price of rent)
CREATE OR REPLACE FUNCTION customer_rentals(customer_id INT)
RETURNS table(
    c_rent_id INT,
    car_id INT,
    rental_date date,
    period INT,
    total_price double precision
             )
LANGUAGE plpgsql
    AS
$$
    declare
        values record;
    begin
        for values in (
            SELECT rent.rent_id,
                   rent.car_car_id,
                   rent.customers_customer_id,
                   rent.date_rent,
                   rent.period_renting,
                   car.car_price
            FROM rent
                JOIN car ON rent.car_car_id = car.car_id
            WHERE rent.customers_customer_id = customer_id
        )
        loop
            c_rent_id := values.rent_id;
            car_id := values.car_car_id;
            rental_date := values.date_rent;
            period := values.period_renting;
            total_price := values.period_renting * values.car_price;

            return next ;
        end loop;
    end;
$$;
END ;

SELECT * FROM customer_rentals(3);


-- func with cursor
CREATE OR REPLACE FUNCTION search_customer (search_id INT,
                                            new_name VARCHAR,
                                            new_surname VARCHAR)
RETURNS VOID
LANGUAGE plpgsql
    AS
$$
declare
	cur cursor
	    for select * from customers;
begin
	for rec in cur loop
		if rec.customer_id = search_id then
			raise notice 'The customer is found';
			UPDATE customers SET
			                     first_name = new_name,
			                     second_name = new_surname
				WHERE customer_id = rec.customer_id;
		elsif not found then
			raise notice 'Sorry, The customer is not found';
			rollback;
		end if;

	end loop;
end;
$$;

select * from search_customer(
    100000,
    'petr',
    'petrov');

select * from search_customer(
    1,
    'max',
    'petrov');

