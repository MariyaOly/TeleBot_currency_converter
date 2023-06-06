import telebot
from extensions import APIException, CryptoConverter, values
from config import keys
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.reply_to(message, "Hi! I'm a bot that can provide the price for a specific amount of currency.\n" \
                          "-To convert, send me a message in the following format:\n" \
                          "<currency name you want to know> \n" \
                          "<currency name to know the price in>\n" \
                          "<amount of the first currency>\n\n" \
                          "For example, to get the price of 100 dollars in rubles, send:\n" \
                          "USD RUB 100\n\n" \
                          "-For the currency list: /currency_list")


@bot.message_handler(commands=['currency_list'])
def handle_currency_list(message):
    currency_list = "Available currencies:\n" \
             "- Euro (EUR)\n" \
             "- US Dollar (USD)\n" \
             "- Russian Ruble (RUB)\n" \
             "- Indian Rupee (INR)"

    bot.reply_to(message, currency_list)


@bot.message_handler(content_types=['text'])
def convert_result(message: telebot.types.Message):
    try:
        input_values = message.text.split(' ')

        if len(input_values) != 3:
            raise APIException('Invalid number entered.')

        base, quote, amount = input_values
        result = CryptoConverter.convert(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Incorrect currency entered. Please check the available currencies using /currency_list. \n {e}')
    except Exception as e:
        bot.reply_to(message, f'An error occurred while processing your request. \n {e}')
    else:
        text = f'{amount} {base}({base}) in {quote}({quote}) is: {result}'
        bot.send_message(message.chat.id, text)


bot.polling()


