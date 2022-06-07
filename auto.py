import requests, threading, json
from twocaptcha import TwoCaptcha

config = json.loads(open('config.json', 'r').read())

captcha_config = {
            'apiKey': config['apiKey'],
            'defaultTimeout': 200,
            'recaptchaTimeout': 600,
        }

solver = TwoCaptcha(**captcha_config)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'null'
}

def checkBalance():
    try:
        balance = solver.balance()
    except Exception as e:
        print(e)
        quit()
    if balance < config['balance_stop']:
        print('Not enough credits!')
        return True
    else:
        return False

def sender():
    global counter
    counter = 0
    while True:
        if checkBalance():
            break
        if requests.get('http://emkei.cz/').status_code != 200:
            print('IP blocked!')
            break

        try:
            captcha_response = solver.hcaptcha(sitekey='3fbaf8b1-0fee-45c1-95ec-39b2f57a4fba', url='https://emkei.cz/?hCaptcha')
        except:
            continue

        data = {
            'fromname': config['sender_name'],
            'from': config['sender_email'],
            'rcpt': config['receiver_email'],
            'subject': config['subject'],
            'attachment[]': '(binary)',
            'importance': 'normal',
            'xmailer': '0',
            'current': 'on',
            'charset': 'utf-8',
            'encrypt': 'no',
            'ctype': 'plain',
            'rte': '0',
            'text': config['message'],
            'g-recaptcha-response': captcha_response['code'],
            'h-captcha-response': captcha_response['code'],
            'ok': 'Send'
        }
        
        r = requests.post('https://emkei.cz/?hCaptcha', data=data, headers=headers)
        if 'E-mail sent successfully' in r.text:
            counter += 1
            print(f'{counter} emails send!')
            solver.report(captcha_response['captchaId'], True)
        elif "The hCaptcha test wasn't successful. Please try again." in r.text:
            print('Captcha failed!')
            solver.report(captcha_response['captchaId'], False)
        else:
            print('Unknown error!')
            out = open('error.html', 'w').write(r.text)

for i in range(config['threads']):
    threading.Thread(target=sender).start()
