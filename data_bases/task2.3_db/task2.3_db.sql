--Задание 1
--Создайте новую таблицу potential customers с полями id, email, name, surname, second_name, city
--не понятно id новой таблицы соответствует id таблицы Users?
--пока так(новый id)

CREATE TABLE IF NOT EXISTS Potential_customers
(
    id SERIAL NOT NULL PRIMARY KEY,
    email VARCHAR(50),
    first_name VARCHAR(50),
    surname VARCHAR(50),
    second_name VARCHAR(50),
    city VARCHAR(50)
);

--Заполните данными таблицу.
INSERT INTO Potential_customers (email, first_name, surname, second_name, city)
VALUES ('email@gmail.com', 'ivan', 'ivanov', 'ivanovich', 'city 17'),
        ('my_mail@gmail.com', 'petr', 'petrov', 'petrovich', 'city 25'),
        ('good_mail@mail.ru', 'stepan', 'stepanov', 'stepanovich', 'saint-petersburg'),
        ('mail@gmail.com', 'jhon', 'blake', NULL, 'city 32');

--Выведите имена и электронную почту потенциальных и существующих пользователей из города city 17
SELECT P.first_name, P.email FROM Potential_customers P WHERE P.city = 'city 17'
UNION
SELECT U.first_name, U.email FROM Users U WHERE U.city = 'city 17';


--Задание 2
--Вывести имена и электронные адреса всех users отсортированных по городам и по имени (по алфавиту)
SELECT first_name, email FROM Users
ORDER BY city, first_name;

--Задание 3
--Вывести наименование группы товаров, общее количество по группе товаров в порядке убывания количества
SELECT C.category_title, count(P.category_id) FROM categories C
    JOIN Products P ON p.category_id = c.category_id
    GROUP BY c.category_title
    ORDER BY count(p.category_id) desc;


--Задание 4
--1. Вывести продукты, которые ни разу не попадали в корзину.
SELECT P.product_title FROM products P
    JOIN cart_product C ON C.products_product_id = p.producrt_id
    WHERE C.carts_cart_id IS NULL
;

--2. Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину попасть могли).
SELECT P.product_title, c.carts_cart_id, o.order_id FROM products P
    JOIN cart_product c ON C.products_product_id = p.producrt_id
    JOIN carts ON cart_id = c.carts_cart_id
    JOIN orders o ON o.carts_cart_id = cart_id
    WHERE o.order_id IS NULL
;

--3. Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.
SELECT P.product_title, c.carts_cart_id FROM products P
    JOIN cart_product c ON C.products_product_id = p.producrt_id
    JOIN carts ON cart_id = c.carts_cart_id
    GROUP BY product_title
    ORDER BY count(product_id) desc
    LIMIT 10
;

--4. Вывести топ 10 продуктов, которые не только добавляли в корзины, но и оформляли заказы чаще всего.
SELECT P.product_title, c.carts_cart_id FROM products P
    JOIN cart_product c ON C.products_product_id = p.producrt_id
    JOIN carts ON cart_id = c.carts_cart_id
    JOIN orders o ON o.carts_cart_id = cart_id
    WHERE o.order_status_order_status_id != 5
    GROUP BY p.product_title
    ORDER BY count(product_title) desc
;

--5. Вывести топ 5 юзеров, которые потратили больше всего денег (total в заказе).
SELECT first_name, last_name, total FROM users
    JOIN carts ON user_id = cart_id
    ORDER BY total desc
    LIMIT 5
;

--6. Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).
SELECT first_name, last_name, count(orders.order_id) FROM users
    LEFT JOIN carts ON users.user_id = carts.users_user_id
    LEFT JOIN orders ON carts.cart_id = orders.carts_cart_id
    GROUP BY first_name, last_name
    ORDER BY count(orders.order_id) desc
    LIMIT 5
;

--7. Вывести топ 5 юзеров, которые создали корзины, но так и не сделали заказы.
SELECT first_name, last_name FROM users
    JOIN carts ON user_id = cart_id
    JOIN orders  ON orders.carts_cart_id = cart_id
    WHERE orders.order_status_order_status_id = 5
    GROUP BY last_name, first_name
    ORDER BY count(orders.order_id) desc
    LIMIT 5
;


drop table  potential_customers;