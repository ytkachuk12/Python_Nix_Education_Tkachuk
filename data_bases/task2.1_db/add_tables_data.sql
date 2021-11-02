COPY users FROM '/usr/src/users.csv' DELIMITER ',' CSV;
COPY carts FROM '/usr/src/carts.csv' DELIMITER ',' CSV;
COPY cart_products FROM '/usr/src/cart_products.csv' DELIMITER ',' CSV;
COPY order_status FROM '/usr/src/order_status.csv' DELIMITER ',' CSV;
COPY orders FROM '/usr/src/orders.csv' DELIMITER ',' CSV;
COPY categories FROM '/usr/src/categories.csv' DELIMITER ',' CSV;
COPY products FROM '/usr/src/products.csv' DELIMITER ',' CSV;