# crypto-checker

🔍 Простая утилита на Python для проверки баланса криптовалютных кошельков (BTC и ETH) с помощью открытых API.

## Установка

1. Клонируйте репозиторий:
git clone https://github.com/1life1chance/crypto-checker.git

cd crypto-checker
-------------------
2. Установите зависимости:
pip install -r requirements.txt

shell
--------------------

## Использование

python crypto_checker.py <coin> <address>

- `<coin>` — `btc` или `eth`
- `<address>` — адрес кошелька

---------------------

### Примеры

python crypto_checker.py btc 1BoatSLRHtKNngkdXEXXXXXXXXXXXX
python crypto_checker.py eth 0xde0B295669a9FD93d5F28DXXXXXXXXXXXXXXX

------------------------


## Примечание

Для проверки баланса ETH требуется API-ключ от [Etherscan](https://etherscan.io/myapikey).  
Вставьте его вместо `YourApiKeyToken` в коде `crypto_checker.py`.

---

## Лицензия

MIT

