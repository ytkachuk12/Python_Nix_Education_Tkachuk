--1. Создать функцию, которая сетит shipping_total = 0 в таблице order,
-- если город юзера равен x. Использовать IF clause

-- вариант быстрее но без if (который здесь не нужен)
CREATE OR REPLACE FUNCTION set_shipping_for_current_city(current_city VARCHAR)
    RETURNS void
    LANGUAGE plpgsql AS
$$
    declare
        values record;
    begin
        for values in (
            SELECT order_id, shipping_total, users.city
            FROM orders
                     JOIN carts ON orders.carts_cart_id = carts.cart_id
                     JOIN users ON carts.users_user_id = users.user_id
            WHERE users.city = current_city
        )
        loop
                UPDATE orders SET shipping_total = 30
                    WHERE values.order_id = orders.order_id;
        end loop;
    end;
$$;

-- вариант медленнее но с if
CREATE OR REPLACE FUNCTION set_shipping_for_current_city(current_city VARCHAR)
    RETURNS void
    LANGUAGE plpgsql AS
$$
    declare
        values record;
    begin
        for values in (
            SELECT order_id, shipping_total, users.city
            FROM orders
                     JOIN carts ON orders.carts_cart_id = carts.cart_id
                     JOIN users ON carts.users_user_id = users.user_id
        )
        loop
            if values.city = current_city then
                UPDATE orders SET shipping_total = 0
                    WHERE values.order_id = orders.order_id;
            end if;
        end loop;
    end;
$$;

SELECT * FROM set_shipping_for_current_city('x');


--2. Написать 2 любые хранимые процедуры с использованием условий, циклов и транзакций.
CREATE OR REPLACE PROCEDURE set_in_stock(
    check_product_id INT,
    sold INT
)
LANGUAGE plpgsql AS
$$
    declare
        new_in_stock INT;
    begin
        UPDATE products SET in_stock = in_stock - sold
        WHERE product_id = check_product_id
        RETURNING in_stock
        INTO new_in_stock;

        if new_in_stock > 0 then
            commit ;
        elsif new_in_stock = 0 then
            commit ;
            raise notice 'Product with id % - sold', check_product_id;
        else
            raise notice 'Incorrect data';
            rollback ;
        end if;
    end;
$$;

call set_in_stock(3, 5) ;


CREATE OR REPLACE PROCEDURE discount(
    discount double precision
)

    LANGUAGE plpgsql AS
$$
    declare
        values record;
    BEGIN
        if discount > 1 OR discount < 0 then
            raise notice 'Wrong discount. It should be 0 < discount < 1';
            rollback ;
        end if;
        for values in (
            SELECT product_id,price FROM products
            WHERE price > 100.00
        )
        loop
            UPDATE products SET
            price = values.price * discount
            WHERE product_id = values.product_id;
        end loop ;
    END ;
$$;

call discount(1.2);