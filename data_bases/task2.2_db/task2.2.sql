--Задание 1 Вывести:
-- 1. всех юзеров(если имеется ввиду имя)
SELECT first_name, middle_name, last_name FROM Users;

-- 1. всех юзеров(все данные)
SELECT * FROM Users;

--2. все продукты(название и описание или все)
SELECT product_title, product_description FROM Products;
SELECT * FROM Products;

--3. все статусы заказов
SELECT status_name FROM Order_status;


--Задание 2
--Вывести заказы, которые успешно доставлены и оплачены
SELECT * FROM Orders WHERE Order_status_order_status_id in(3, 4)


--Задание 3
--Вывести:
--(если задание можно решить несколькими способами, указывай все)
--1. Продукты, цена которых больше 80.00 и меньше или равно 150.00
SELECT * FROM Products WHERE price BETWEEN 80.001 AND 150.00;

--2. заказы совершенные после 01.10.2020 (поле created_at)
SELECT * FROM Orders WHERE created_at > '2020-10-01';

--3. заказы полученные за первое полугодие 2020 года
SELECT * FROM Orders WHERE created_at BETWEEN '2020-01-01' AND '2020-06-30';

--4. подукты следующих категорий Category 7, Category 11, Category 18
SELECT * FROM Products WHERE category_id in (7, 11, 18);
SELECT * FROM Products WHERE category_id = 7 OR  category_id = 11 OR category_id = 18;

--5. незавершенные заказы по состоянию на 31.12.2020
SELECT * FROM Orders WHERE created_at >= '2020-12-31' AND order_status_order_status_id in (1, 2, 3);
-- можно еще перечислить через OR order_status = 1 or order_status..

--6.Вывести все корзины, которые были созданы, но заказ так и не был оформлен.
SELECT * FROM Orders WHERE order_status_order_status_id = 5;


--Задание 4
--Вывести:
--1. среднюю сумму всех завершенных сделок
SELECT AVG(total) AS "Average sum all orders" FROM Orders WHERE order_status_order_status_id = 4;
SELECT SUM(total)/COUNT(order_id) AS "Average" FROM Orders WHERE order_status_order_status_id = 4;

--2. вывести максимальную сумму сделки за 3 квартал 2020
SELECT MAX(total) AS "Max order" FROM Orders WHERE order_status_order_status_id != 5 AND created_at
BETWEEN '2020-07-01' AND '2020-09-30';

