TASK: to write and test a Telegram bot which will implement the following functionality:

1.Bot returns the price of a certain amount of currency (euro, dollar or ruble).

2.When writing the bot you need to use the library pytelegrambotapi.

3.The person must send a message to the bot in the form <name of the currency whose price he wants to know> <name of the currency in which you want to know the price of the first currency> <number of the first currency>.
  
4.When you type /start or /help the user will get instructions on how to use the bot.
  
5.When entering the command /values or currency_list, information about all available currencies should be displayed in a readable form.
  
6.To take exchange rates, it's necessary to use the API and send requests to it using the Requests library.

7.Use JSON library for parsing responses.

8.If user makes a mistake (e.g. wrong or non-existing currency or wrong number), call the written APIException with text explaining the error.
  
9.The text of any error with the type of error should be sent to the user in messages.
  
10.To send requests to API, describe a class with static method get_price(), which takes three arguments: the name of the currency, the price of which we want to know - base, the name of the currency, the price in which we want to know - quote, the amount of currency to be transferred - amount and returns the desired amount of the currency.
  
11.Keep telegramm bot's token in special config (you can use .py file).
  
12.Hide all classes in extensions.py file.
