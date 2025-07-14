import requests
import argparse

def get_btc_balance(address):
    url = f"https://blockchain.info/q/addressbalance/{address}"
    response = requests.get(url)
    if response.status_code == 200:
        balance_satoshi = int(response.text)
        return balance_satoshi / 1e8  # Convert to BTC
    else:
        raise Exception(f"Error fetching BTC balance: {response.text}")

def get_eth_balance(address):
    url = f"https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": "YourApiKeyToken"  # Replace with your actual Etherscan API key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        result = response.json()
        if result["status"] == "1":
            balance_wei = int(result["result"])
            return balance_wei / 1e18  # Convert to ETH
        else:
            raise Exception(f"Error from Etherscan: {result['message']}")
    else:
        raise Exception(f"Error fetching ETH balance: {response.text}")

def main():
    parser = argparse.ArgumentParser(description="Check cryptocurrency wallet balance.")
    parser.add_argument("coin", choices=["btc", "eth"], help="Cryptocurrency: btc or eth")
    parser.add_argument("address", help="Wallet address")
    args = parser.parse_args()

    try:
        if args.coin == "btc":
            balance = get_btc_balance(args.address)
            print(f"BTC Balance for {args.address}: {balance:.8f} BTC")
        elif args.coin == "eth":
            balance = get_eth_balance(args.address)
            print(f"ETH Balance for {args.address}: {balance:.8f} ETH")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
