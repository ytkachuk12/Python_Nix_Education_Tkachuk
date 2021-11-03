--  заполнить таблицу данными


-- Generate random INT from start to stop (for default start is 1)
CREATE OR REPLACE FUNCTION gen_random_num(
    stop INT,
    start INT default 1
    )
RETURNS INT
LANGUAGE plpgsql
    AS
$$
BEGIN
   RETURN floor(random() * (stop-start + 1) + start);
END;
$$;


-- return 'injector' or 'carburetor'
CREATE OR REPLACE FUNCTION return_injection_type()
RETURNS VARCHAR
LANGUAGE plpgsql
    AS
$$
BEGIN
    if random() < 0.5 then
        RETURN 'injector';
    else
        RETURN 'carburetor';
    end if;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_customers(
    num_of_rows INT default 1000
)
LANGUAGE plpgsql
    AS
$$
    declare
        i INT;
        num_of_branches INT;
    begin
        SELECT count(branch_id)
        INTO num_of_branches
        FROM branch;
        for i in 1..num_of_rows loop
            INSERT INTO customers (customer_id,
                                   first_name,
                                   second_name,
                                   address_customer_id)
            VALUES (i,
                    'name' || i,
                    'surname' || i,
                    i + num_of_branches );
        end loop;
    end;
$$;


CREATE OR REPLACE PROCEDURE insert_address(
    num_of_rows INT default 1000
)
LANGUAGE plpgsql
    AS
$$
    declare
        i INT;
    begin
        for i in 1..num_of_rows loop
            INSERT INTO address (address_id,
                                 city_city_id,
                                 street,
                                 house)
            VALUES (i,
                    gen_random_num(100),
                    'street' || gen_random_num(800),
                    gen_random_num(250));
        end loop;
    end;
$$;


CREATE OR REPLACE PROCEDURE insert_branch(
    num_of_rows INT default 1000
)
LANGUAGE plpgsql
    AS
$$
    declare
        i INT;
    BEGIN
        for i in 1..num_of_rows loop
            INSERT INTO branch (branch_id,
                                address_branch_id)
            VALUES (i,
                    i);
        end loop;
    end;
$$;


create procedure insert_city(IN num_of_rows integer DEFAULT 1000)
    language plpgsql
as
$$
declare
        i INT;
    BEGIN
        for i in 1..num_of_rows loop
            INSERT INTO city (city_id,
                              city_name,
                              city_code)
            VALUES (i,
                    'city' || i,
                    '0' || gen_random_num(999));
        end loop;
    end;
$$;


CREATE OR REPLACE PROCEDURE insert_transmission(
    num_of_rows INT default 1000
)
LANGUAGE plpgsql
    AS
$$

    BEGIN
        INSERT INTO transmission (transmission_id,
                                  transmission_type)
        VALUES (1,
                'automatic'
                );

        INSERT INTO transmission (transmission_id,
                                  transmission_type)
        VALUES (2,
                'manual'
                );

    end;
$$;


CREATE OR REPLACE PROCEDURE insert_engine(
    num_of_rows INT default 1000
)
LANGUAGE plpgsql
    AS
$$
    declare
        i INT;
    BEGIN
        for i in 1..num_of_rows loop
            INSERT INTO engine (engine_id,
                                volume,
                                injection)
            VALUES (i,
                    gen_random_num(3000, 1200),
                    return_injection_type());
        end loop;
    end;
$$;


CREATE OR REPLACE PROCEDURE insert_brand(
    num_of_rows INT default 1000
)
LANGUAGE plpgsql
    AS
$$
    declare
        i INT;
    BEGIN
        for i in 1..num_of_rows loop
            INSERT INTO brand (brand_id,
                               brand_name)
            VALUES (i,
                    'brand' || i
                    );
        end loop;
    end;
$$;


CREATE OR REPLACE PROCEDURE insert_model(
    num_of_rows INT default 1000
)
LANGUAGE plpgsql
    AS
$$
    declare
        i INT;
    BEGIN
        for i in 1..num_of_rows loop
            INSERT INTO model (model_id,
                               brand_brand_id,
                               car_name,
                               engine_engine_id,
                               transmission_transmission_id,
                               color)
            VALUES (i,
                    gen_random_num(180),
                    'car_name' || i,
                    gen_random_num(150),
                    gen_random_num(2),
                    'color' || gen_random_num(25));
        end loop;
    end;
$$;


CREATE OR REPLACE PROCEDURE insert_car(
    num_of_rows INT default 1000
)
LANGUAGE plpgsql
    AS
$$
    declare
        i INT;
    BEGIN
        for i in 1..num_of_rows loop
            INSERT INTO car (car_id,
                             car_namber,
                             model_model_id,
                             car_price)
            VALUES (i,
                    gen_random_num(999999, 100000),
                    gen_random_num(300),
                    gen_random_num(100) + random()
                    );
        end loop;
    end;
$$;


-- Each car must be in at least one branch
CREATE OR REPLACE PROCEDURE insert_car_branch(
    num_of_rows INT default 1000
)
LANGUAGE plpgsql
    AS
$$
    declare
        i INT;
    BEGIN
        for i in 1..num_of_rows loop
            INSERT INTO car_branch (car_car_id,
                                    branch_branch_id)
            VALUES (i,
                    gen_random_num(100)
                    );
        end loop;
    end;
$$;


-- Add cars that have been moved from one branch to another
CREATE OR REPLACE PROCEDURE insert_additional_car_branch(
    num_of_rows INT default 1000
)
LANGUAGE plpgsql
    AS
$$
    declare
        i INT;
    BEGIN
        for i in 1..num_of_rows loop
            INSERT INTO car_branch (car_car_id,
                                    branch_branch_id)
            VALUES (gen_random_num(650),
                    gen_random_num(100)
                    );
        end loop;
    end;
$$;


-- The DB contains customers who at least once took a car
CREATE OR REPLACE PROCEDURE insert_rent(
    num_of_rows INT default 1000
)
LANGUAGE plpgsql
    AS
$$
    declare
        i INT;
    BEGIN
        for i in 1..num_of_rows loop
            INSERT INTO rent (rent_id,
                              car_car_id,
                              customers_customer_id,
                              date_rent,
                              period_renting)
            VALUES (i,
                    gen_random_num(650),
                    i,
                    timestamp '2020-01-01' + (random() * (timestamp '2021-11-07' - timestamp '2020-01-01')),
                    gen_random_num(15)
                    );
        end loop;
    end;
$$;


-- Add customers who took car more than once
CREATE OR REPLACE PROCEDURE insert_addition_rent(
    num_of_rows INT default 1000
)
LANGUAGE plpgsql
    AS
$$
    declare
        i INT;
    BEGIN
        for i in 1..num_of_rows loop
            INSERT INTO rent (rent_id,
                              car_car_id,
                              customers_customer_id,
                              date_rent,
                              period_renting)
            VALUES (i + 1000,
                    gen_random_num(650),
                    gen_random_num(1000),
                    timestamp '2020-01-01' + (random() * (timestamp '2021-11-07' - timestamp '2020-01-01')),
                    gen_random_num(15)
                    );
        end loop;
    end;
$$;


CREATE OR REPLACE PROCEDURE insert_phone(
    num_of_rows INT default 1000
)
LANGUAGE plpgsql
    AS
$$
    declare
        i INT;
        citycode VARCHAR;
    BEGIN

        for i in 1..num_of_rows loop
            SELECT city_code
            INTO citycode
            FROM city
                JOIN address ON city.city_id = address.city_city_id
            WHERE address.address_id = i;

            INSERT INTO phone (phone_id,
                               address_phone_id,
                               phone_number,
                               city_city_code)
            VALUES (i,
                    i,
                    '0' || gen_random_num(999999, 100000),
                    citycode
                    );
        end loop;
    end;
$$;


CALL insert_city(100);
CALL insert_address(1100);
CALL insert_branch(100);
CALL insert_customers();
CALL insert_transmission(2);
CALL insert_engine(150);
CALL insert_brand(180);
CALL insert_model(300);
CALL insert_car(650);
CALL insert_car_branch(650);
CALL insert_additional_car_branch(100);
CALL insert_rent();
CALL insert_addition_rent(870);
CALL insert_phone(1100);
