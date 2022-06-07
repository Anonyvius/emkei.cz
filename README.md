# emkei.cz

emkei.cz is a spammer / WIP API that uses the website [emkei.cz](https://emkei.cz/) to send emails from any address, to any address.
It uses the 2captcha API to bypass the hCaptcha proposed by the website

## Prerequisites

- have python3+ installed.
- [2captcha](https://2captcha.com/) API key with balance

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages requests and twocaptcha.

```bash
> pip3 install requests
> pip3 install twocaptcha 
```

## Installation

Use `git clone` to download the repository to your local machine

```bash
> git clone https://github.com/Anonyvius/emkei.cz
```

## Usage

Open the config.json and edit the variables to your preferences.

```json
{
    "sender_name": "Google Admin",
    "sender_email": "admin@gmail.com",
    "receiver_email": "template_email@gmail.com",
    "subject": "Test email",
    "message": "this is a test",
    "api_key": "YOUR 2CAPTCHA API KEY",
    "balance_stop": 1.0
}
```

`threads` defines the amout of concurrent threads that will be used to send emails.
`apiKey` is your 2captcha API key.
`balance_stop` automatically stops the program if your 2captcha balance dips below a certain number.
Everything else should be self explanatory

Execute the auto.py

```bash
> python3 auto.py
```

![output](https://i.imgur.com/kAa6gAY.png)
![received email](https://i.imgur.com/tZhqZOc.png)

(the emails are very likely to go into the spam folder. There is currently no fix for this that I am aware of.)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Disclaimer
This repository is for research purposes only, the use of this code is your responsibility.

I take NO responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again, ALL files available here are for EDUCATION and/or RESEARCH purposes ONLY.