import itertools
import hashlib
import os
import datetime
import re


class Customer:
    """Class customer contain customer information"""

    customer_new_id = itertools.count()

    def __init__(self, customer_name: str, customer_phone: str, customer_email: str, customer_address: str):
        self.customer_id = next(Customer.customer_new_id)  # just for simple example(it should be in db)
        self.customer_name = customer_name
        self.customer_phone = self.validate_phone(customer_phone)
        self.customer_email = self.validate_email(customer_email)
        self.customer_address = customer_address

    def __str__(self):
        """Present customer information: name and phone"""
        return f"{self.customer_name} with phone number: {self.customer_phone}"

    def set_customer(self, name, phone, email, address):
        """Set customer info"""
        self.customer_id = next(Customer.customer_new_id)  # just for simple example(it should be in db)
        self.customer_name = name
        self.customer_phone = phone
        self.customer_email = email
        self.customer_address = address

    @staticmethod
    def validate_email(email):
        """Validate email"""
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        return False

    @staticmethod
    def validate_phone(phone):
        """Validate phone"""
        if re.match(r"^(\([0-9]{3}\) ?|[0-9]{3}-)[0-9]{3}-[0-9]{4}$", phone):
            return phone
        return False

    def check_db_fo_email(self):
        """Check if the customer made an order(in past)"""
        pass

    def check_db_fo_phone(self):
        """Check if the customer made an order(in past)"""
        pass

    def get_customer(self):
        """Return customers info"""
        return {"id": self.customer_id, "name": self.customer_name}


class Order:
    """Class order, keep all info about order"""
    order_new_id = itertools.count()

    def __init__(self, meal_quantity, order_address):
        self.order_id = next(Order.order_new_id)  # just for simple example
        self.order = {}
        self.meal_quantity = meal_quantity
        self.order_address = order_address
        self.order_price = 0

    def set_order(self, customer: Customer):
        """Create order and set all info: meal list, price and so on
        Take argument type Customer"""
        self.order.append(Menu.pick_meal() * self.meal_quantity)
        self.order.append(customer)

    def get_order(self):
        """Return ifo about order: menu list, info, customer info"""
        return self.order


class TableOrder:
    """Keep info about ordered table"""
    def __init__(self):
        self.customer_name = None
        self.table_number = None
        self.order_time = None

    def set_table(self, customer: Customer):
        """Book current table for current time
         take argument type Customer"""
        self.customer_name = customer.customer_name
        self.table_number = "current table"
        self.order_time = "On time, if table have not booked yet"

    def get_table(self):
        """Return info about ordered table: table number, booking time and so on"""
        return {"name": self.customer_name, "number": self.table_number, "time": self.order_time}


class Invoice:
    """Class service payment and all about payment"""
    def __init__(self):
        self.payment = Order.get_order().price
        self.order_date_time = datetime.datetime.now()
        self.payment_status = None

    def payment_method(self):
        self.payment_status = "status"

    def get_status(self, order_id):
        """Return payment status"""
        if isinstance(order_id, self.payment.order_id):
            return self.payment_status


class PaymentMethod:
    """Class for payment methods: cash and card"""
    payment_methods = ("credit_card", "cash")

    def __init__(self):
        self.payment_method = None

    def set_payment_method(self):
        """Depends by user choice set payment method"""
        self.payment_method = self.payment_methods[0]

    def get_payment_method(self):
        """Return payment method: cash or credit card"""
        return self.payment_method


class Cash:
    """Cash class take users banknote value"""
    def __init__(self, denomination: float):
        self.denomination = denomination

    def change_count(self, order: Order):
        """Method calculates the required change
        depends on customers banknote and order price"""
        return self.denomination - order.price

    def get_change(self):
        """Return customers change"""
        return self.change_count()


class CreditCard:
    """All info about users card"""
    def __init__(self, card_number: int, card_name: str, card_expire_date: str):
        self.card_number = card_number
        self.card_name = card_name
        self.card_expire_date = card_expire_date

    def valid_card(self, card_number: int, card_name: str, card_expire_data: str):
        """Check is card valid or not"""
        pass

    def get_credit_card(self):
        """Return credit card info"""
        return self.card_number


class Meal:
    """Class keep info about meal:
    name, price, description, photo and so on"""
    meal_new_id = itertools.count()

    def __init__(self, meal_name: str, meal_describe: str, meal_photo, meal_price: float):
        self.meal_id = next(Meal.meal_new_id)
        self.meal_name = meal_name
        self.meal.describe = meal_describe
        self.meal_photo = meal_photo
        self.meal_price = meal_price


class ComboMeals:
    """Combo meals with special price"""
    def __init__(self, combo_name, combo_description, discount, *args: Meal):
        self.combo_meals = []
        for arg in args:
            self.combo_meals.append(arg)
        self.discount = discount
        self.combo_name = combo_name
        self.description = combo_description

    def set_combo_name(self, combo_name, description):
        """Set combo info"""
        self.combo_name = combo_name
        self.description = description

    def discount(self):
        """Calculate discount for combo meal
        return price depends on meals and discount"""
        combo_price = 0
        for meal in self.combo_meals:
            combo_price += meal.price
        return combo_price * self.discount


class Menu:
    """Class contains main menu with all meals"""
    __menu_list = []

    def display_menu(self, meal: Meal):
        """Display all menu info"""
        for meal in self.__menu_list:
            print(meal.meal_id)  # and all other instances

    def pick_meal(self, combo_meals: ComboMeals):
        """Customer choose current meal
        Depends on customer choice
        :return list of meals"""
        if combo_meals:
            return self.__menu_list[combo_meals]
        return self.__menu_list[0]


class RootEmployee:
    """Class of privileged employee
    He can change menu, add or delete personal and so on"""
    root_new_id = itertools.count()

    def __init__(self, name: str, address: str, phone_number: str, email: str, position: str):
        self.root_id = next(RootEmployee.root_new_id)
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.position = position

    @staticmethod
    def set_meal():
        """Root employee has the ability to set, change and delete meal from menu
            *args and **kwargs meal parameters: name, describe, photo etc"""

        # create meal: set name, description, photo, etc
        meal = Meal("*args", "**kwargs")
        Menu.__menu_list.append(meal)

    @staticmethod
    def remove_from_menu(meal: Meal):
        """Root employee has the ability to set, change and delete meal from menu
            *args and **kwargs meal parameters: name, describe, photo etc"""
        if isinstance(meal, Meal):
            Menu.__menu_list.remove(meal)
        else:
            raise TypeError("Not the Meal type!")

    @staticmethod
    def edit_menu(meal: Meal):
        """Root employee has the ability to set, change and delete meal from menu
            *args and **kwargs meal parameters: name, describe, photo etc"""
        if isinstance(meal, Meal):
            for temp in meal.__dict__:
                temp = "new value"
        else:
            raise TypeError("Not a Product type!")

    @staticmethod
    def register_employee():
        """Register new employee person """
        new_employee = Employee("*args", "**kwargs")
        return new_employee


class Employee:
    """Class employee contains all restaurants stuff  """
    employee_new_id = itertools.count()

    def __init__(self, name: str, nic_name: str, password: str):
        self.employee_id = next(Employee.employee_new_id)
        self.name = name
        self.nic_name = nic_name
        self.salt = os.urandom(32)
        self.password_hash = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), self.salt, 100000, dklen=128
        )

    def __authorization(self, nickname, password):
        """authorization take nickname and pass
        generate hash pass and compare with nickname and hash pass from db
        :argument nickname and pass
        """
        new_hash = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), self.salt, 100000, dklen=128
        )
        # log in employee
        if nic_name == self.nic_name and new_hash == self.password_hash:
            # return log in employee
            return "Successfully  logged in"
        return "Invalid nic name or password"

    @staticmethod
    def customers(self):
        """Get information about order: list of meal, price, etc"""
        if Order.get_order():
            pass
        if TableOrder.get_table():
            pass

    @staticmethod
    def today_order_history(*orders):
        """Return info about all served orders or customers"""
        today_orders = []
        while orders:
            today_orders.append({"customer_name": orders.customer_name, "order_price": orders.order_price})


class Delivery(Employee):
    """Class for delivery
    contains info about delivery person and delivery time
    :argument customer info: name, phone, address, change for customer
    order info: price, meal list
    cook info: cook time"""
    def __init__(self, *args):
        self.delivery_time = None
        super().__init__(*args)

    def count_time(self):
        """Count and return delivery time
        depends on customer and restaurant address, traffic jam
        """
        order_address = Order.get_order()
        # count delivery time depends on address
        self.delivery_time = datetime.timedelta
        return self.delivery_time


class KitchenManager(Employee):
    """class for kitchen"""
    meals_out_of_order = []

    def __init__(self, *args):
        self.cook_time = None
        super().__init__(*args)

    def count_time(self, meal):
        """count cook time for current meal
        return time ready meal"""
        self.cook_time = ""
        return self.cook_time

    def meal_out_of_order(self):
        """If there are no some products in the kitchen
        return list of meal that are out of order"""
        self.meals_out_of_order.append("meal")
        return self.meals_out_of_order
