class Noti:

    def send_telegram_message(message):
        ''' Send telegram message to experimenter
        message: personal_code, string
        '''

        import urllib, requests
        url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (
        'keyhere', 'chatid', urllib.parse.quote_plus(message))
        _ = requests.get(url, timeout=10)