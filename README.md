Introduction
------------
This project is a Django (Python's web framework) app that allows users to sign-up and trade a virtual currency, which will just be an arbitrary number to start. The currency fluctuate in price based on the orders given by users. There are two types of orders giving four total options in all. A buy limit order, buy market order, sell limit order, and sell market order. Each of these orders move the price of a market in a different way that is implemented in this project. The users’ orders move the market price for the virtual currency in the same way, so in this way this program resembles a real market. This program is part of a school project so users from different laptops or PCs can be connected to the same market, interacting with one another. All orders are logged and time-stamped in a continually updating file that only admin have access to. Admin should also be able to stop the market or prevent new orders from being entered.

Virtual Currency
------------
The name of the virtual currency is VGC. The program have a starting amount of currency and a starting price. Both of these values are set using the Django administration and admin is also able to change the amount of currency units available even after users enter the market. For example, admin should be able to choose to start the program and set the amount of units of VGC available to 10,000 (or any other number) at a price of $1.00 (or any other number). After users enter the market admin should be able to add or subtract VGC from the market. It should be possible for me to add 90,000 (or any other number) VGC units to the market. 

Django user registration and login with form validation

Registration / Login
------
![index](https://i.imgur.com/PuXZnKW.png)

Success
------
![success](https://i.imgur.com/7QYAYor.png)
