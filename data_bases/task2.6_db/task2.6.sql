--first view, table products
CREATE OR REPLACE VIEW products_category_view AS
    SELECT category_id, product_title, price FROM products
        WHERE category_id = 18
        ORDER BY price
    WITH CHECK OPTION ;

SELECT * FROM products_category_view;

DROP VIEW products_category_view;

--second view, table order_status and order
CREATE OR REPLACE VIEW canceled_orders AS
    SELECT order_id, total, created_at, updated_at FROM orders
    JOIN order_status ON orders.order_status_order_status_id = order_status.order_status_id
    WHERE order_status.status_name = 'Canceled';

SELECT * FROM canceled_orders;

DROP VIEW canceled_orders;

--third view, table products and categories
CREATE OR REPLACE VIEW products_category_title AS
    SELECT product_title, in_stock, price FROM products
    JOIN categories ON products.category_id = categories.category_id
    WHERE categories.category_title LIKE '%1'
    ORDER BY in_stock desc ;

SELECT * FROM products_category_title;

DROP VIEW products_category_title;

--materialize view
CREATE MATERIALIZED VIEW best_users AS
    SELECT first_name|| ' ' ||last_name as full_name,
           country FROM users
    LEFT JOIN carts ON users.user_id = carts.users_user_id
    LEFT JOIN orders ON carts.cart_id = orders.carts_cart_id
    GROUP BY full_name, country
    ORDER BY count(orders.order_id) desc
    WITH NO DATA ;

REFRESH MATERIALIZED VIEW best_users;

SELECT * FROM best_users;

DROP MATERIALIZED VIEW best_users;
