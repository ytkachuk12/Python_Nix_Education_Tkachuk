--1. Сравнить цену каждого продукта n с средней ценой продуктов в категории
--продукта n. Использовать window function. Таблица результата должна
--содержать такие колонки: category_title, product_title, price, avg.
drop function compare_price();

CREATE OR REPLACE FUNCTION compare_price()
RETURNS table(
    n_category_title VARCHAR,
    n_product_title VARCHAR,
    n_price double precision,
    average double precision,
    difference double precision
)
LANGUAGE plpgsql
    AS
$$
    declare
        values record;
    BEGIN
        for values in (
            SELECT product_title,
                    price,
                    category_title,
                    AVG(price) OVER (PARTITION BY category_title) AS average
            FROM products
            JOIN categories ON products.category_id = categories.category_id
            )
        loop
            n_category_title := values.category_title;
            n_product_title := values.product_title;
            n_price := values.price;
            average := values.average;
            difference := values.price - values.average;
            return next;
        end loop;
    end;
$$;
end;

SELECT * FROM compare_price();


--2. Добавить 2 любых триггера и обработчика к ним, использовать транзакции.
CREATE OR REPLACE FUNCTION check_price()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
    BEGIN
        IF NEW.price < 0 then
            RAISE 'Incorrect price';
        end if;
        if OLD.price * 2 < NEW.price then
            RAISE 'The new price is twice as high as the previous one';
        elsif NEW.price * 2 < OLD.price then
            RAISE 'The discount is to high. The new price is twice as lower as the previous one';
        end if;

        RETURN NEW;
    end;
$$;
end;

CREATE TRIGGER before_update_price
  BEFORE UPDATE
  ON products
  FOR EACH ROW
  EXECUTE PROCEDURE check_price();

UPDATE products
SET price = 40
WHERE product_id = 1;


CREATE TABLE old_emails (
   id SERIAL PRIMARY KEY ,
   user_id INT NOT NULL,
   old_email VARCHAR(40) NOT NULL,
   changed_date TIMESTAMP(6) NOT NULL,
   FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE OR REPLACE FUNCTION Check_user_email()
    RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
    BEGIN
        if NEW.email = OLD.email then
            RAISE notice 'Its the same email';
            rollback ;
        else
            INSERT INTO old_emails(user_id,old_email,changed_date)
		 VALUES(OLD.user_id,OLD.email,now());
        end if;

        RETURN NEW;
    end;
$$;
end;


CREATE TRIGGER update_user_email
  BEFORE UPDATE
  ON users
  FOR EACH ROW
  EXECUTE PROCEDURE Check_user_email();

UPDATE users
SET email = 'new_email@gmail.com'
WHERE user_id = 2;