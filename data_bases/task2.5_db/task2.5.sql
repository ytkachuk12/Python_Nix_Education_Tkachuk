--by default enable_seqscan param is on, but to be shore set it on
set enable_seqscan = on;


EXPLAIN SELECT user_id FROM users
    WHERE user_id = 500;

CREATE INDEX idx_users_user_id ON users USING btree(user_id);
DROP INDEX idx_users_user_id;


EXPLAIN SELECT user_id, email, password FROM users
WHERE email = 'input email' AND password = 'input password';

CREATE UNIQUE INDEX idx_users_email_password ON users USING btree(email, password);
--the same result for commented expression down
--CREATE UNIQUE INDEX idx_users_email_password ON users USING btree(email) INCLUDE (password);
DROP INDEX idx_users_email_password;


EXPLAIN SELECT users.first_name, carts.total
    FROM users JOIN carts ON user_id = users_user_id
    WHERE carts.timestamp > '2020-03-13'
    GROUP BY users.first_name, carts.total;

CREATE UNIQUE INDEX idx_Carts_users_user_id_timestamp ON carts(users_user_id, timestamp);


EXPLAIN SELECT Products.product_title, cart_product.carts_cart_id FROM products
    JOIN cart_product  ON products.product_id = cart_product.products_product_id
    JOIN carts ON cart_id = cart_product.carts_cart_id
    JOIN orders o ON o.carts_cart_id = cart_id
    WHERE o.order_status_order_status_id != 5
    GROUP BY products.product_title, cart_product.carts_cart_id
    ORDER BY count(product_title) desc
    LIMIT 10;

CREATE INDEX idx_products_product_title ON products(product_title);
CREATE INDEX idx_Orders_order_status_order_status_id ON orders(order_status_order_status_id);


EXPLAIN SELECT price, in_stock FROM products
    WHERE in_stock IN (15, 30)
    ORDER BY price desc
    LIMIT 10;

--67.71
CREATE INDEX idx_products_in_stock_price ON products(in_stock, price);
--66.93
CREATE INDEX idx_products_in_stock_price ON products(in_stock, price) WHERE in_stock IN (15, 30);

DROP INDEX idx_products_in_stock_price;