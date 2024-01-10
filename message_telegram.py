import requests

def send_message(city_number):
    # Set the Telegram API token.
    apiToken = "6162486281:AAHoNI5RkKInxqkRqwouMhLzLy6H5mfGS5E"

    # Set the chat ID of the channel you want to send the message to.
    chatID1 = "6578526417"
    chatID2 = '6656405705'

    # Set the text message you want to send.
    if city_number == '1':
        message = '- Madrid' + '\n' + '- TIPO DE CITA : ASILO-OFICINA DE ASILO Y REFUGIO."nueva normalidad” Expedición/Renovación Documentos.C/ Pradillo 40'
    elif city_number == '2':
        message = '- Cáceres' + '\n' + '- TIPO DE CITA : POLICIA - SOLICITO DE ASILO'
    elif city_number == '3':
        message = '- Albacete' + '\n' + '- TIPO DE CITA : POLICIA - SOLICITO DE ASILO'
    elif city_number == '4':
        message = '- Valladolid' + '\n' + '- TIPO DE CITA : POLICIA - SOLICITO DE ASILO'
    elif city_number == '5':
        message = '- Segovia' + '\n' + '- TIPO DE CITA : POLICIA - SOLICITO DE ASILO'

    # Create the request body.
    sendData1 = {
        "chat_id": chatID1,
        "text": message
    }
    sendData2 = {
    "chat_id": chatID2,
    "text": message
    }

    telegramURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    # Send the request to the Telegram API.
    response1 = requests.post(telegramURL, sendData1)
    response2 = requests.post(telegramURL, sendData2)

    # Check the response status code.
    if response1.status_code == 200:
        # The message was successfully sent.
        print("Message sent successfully!")
    else:
        # An error occurred.
        print("Error sending message: {}".format(response1.status_code))

    # Check the response status code.
    if response2.status_code == 200:
        # The message was successfully sent.
        print("Message sent successfully!")
    else:
        # An error occurred.
        print("Error sending message: {}".format(response2.status_code))

  
# if __name__ == '__main__':
    # send_message(city_number = '')