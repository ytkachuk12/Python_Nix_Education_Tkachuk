--Transaction level set

SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

--Table one
BEGIN;

    INSERT INTO Users(email, password,first_name,last_name,middle_name,if_staff,country,city,address)
    VALUES ('Qemail@gmail.com', '84204057691', 'first_name q', 'last_name q', 'middle_name q', 0, 'country 1', 'city 1', 'address 1');

    SAVEPOINT alter_table;

        ALTER TABLE users  ADD phone VARCHAR(50);

    ROLLBACK TO alter_table;

    SAVEPOINT update_l_name;

        UPDATE users SET last_name = 'maximov'
        WHERE last_name LIKE '%1';

        SELECT first_name, last_name FROM users
            WHERE last_name = 'maximov';

    RELEASE update_l_name;

    SAVEPOINT del;

        DELETE FROM users
        WHERE user_id = 4;

    ROLLBACK TO del;

ROLLBACK ;
COMMIT ;


--Table Two
BEGIN ;

    UPDATE categories SET category_title =
        CASE
            WHEN category_title = 'Category 1'
            THEN category_title = 'New Category 1'
            WHEN category_title = 'Category 2'
            THEN category_title = 'New Category 2'
        END ;

    SAVEPOINT new_category_title;

    UPDATE categories SET category_description =
        CASE
            WHEN category_title = 'New Category 1'
            THEN category_description = 'New category description 1'
            WHEN category_title = 'New Category 2'
            THEN category_description = 'New category description 2'
        END ;

    SAVEPOINT change_title_and_description;

        INSERT INTO categories
        VALUES (1111, 'new category', 'new description');

        SELECT * FROM categories;

    ROLLBACK TO change_title_and_description;

        DELETE FROM categories WHERE category_id = 3;

        SELECT * FROM categories;

    ROLLBACK TO change_title_and_description;

COMMIT ;


--Table 3
--START TRANSACTION has the same functionality as BEGIN
START TRANSACTION ;
    SELECT product_id, product_title, in_stock, price FROM  products
    ORDER BY price DESC
    LIMIT 5;

    UPDATE products SET price = price  * 0.9
    where price > 200 AND in_stock > 20;

    SELECT product_id, product_title, in_stock, price FROM  products
    ORDER BY price DESC
    LIMIT 5;

    SAVEPOINT update_price;

    DELETE FROM products
        WHERE in_stock = 0;

    SAVEPOINT del_products_no_stock;

    SELECT in_stock FROM products
        WHERE in_stock = 0;

COMMIT ;
