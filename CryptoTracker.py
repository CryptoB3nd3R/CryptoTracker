from requests import get, post
from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
from rich.console import Console;
from rich.table import Table
from time import sleep
import os, re

console = Console()
_Set_Currency = 'USD'


def Head():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(f"""
 ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗       ████████╗██████╗  ██╗  ██╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗      ╚══██╔══╝██╔══██╗ ██╗██╔╝
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║ █████╗  ██║   ██████╔╝ ████╔╝ 
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║ ╚════╝  ██║   ██╔══██╗ ██╗ ██╗
╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝         ██║   ██║  ██║ ██╗  ██╗
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝          ╚═╝   ╚═╝  ╚═╝ ╚═╝  ╚═╝
                   [bold white] By CryptoB3nD3R                                         
""", style='bold yellow', justify='left')



def Starter():
    console.log('Started CryptoCurrency Live Price [bold orange]...[/bold orange]')
    try:
        CryptoCLP_Core()
    except KeyboardInterrupt:
        Head();console.log('-- USER Interrupt\n\n');exit()

def Currency(Currency_price, set_sleep):
    if set_sleep == 60:
        set_sleep = "60 Sec"
    elif set_sleep == 60 * 2:
        set_sleep = "120 Sec"
    console.print("[bold magenta]Crypto Tracker [/bold magenta]!", "", '\n')
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("ID", style="bold dim", width=6)
    table.add_column("Pair", style="bold green", min_width=20)
    table.add_column("Price (USD)", style="bold Yellow", min_width=12, justify="right")
    table.add_column("Refresh Rate", style="bold green", min_width=12, justify="right")
    for id, operation in enumerate(Currency_price, start=1):
        Currency_Name = str(operation).split(":")[0]
        PriceUSD = str(operation).split(":")[1]
        table.add_row(f'{id}', f'{str(Currency_Name)}', f"{str(PriceUSD)}$", f'{str(set_sleep)}')
    console.print(table)


def CryptoCLP_Core():
    _Max_Calls = 7574
    set_sleep = 60
    i = 0
    Currency_price = list()
    while i != _Max_Calls:
        sleep(set_sleep)
        BTC = get(f'https://min-api.cryptocompare.com/data/price?fsym=btc&tsyms={_Set_Currency}').json()
        ETH = get(f'https://min-api.cryptocompare.com/data/price?fsym=eth&tsyms={_Set_Currency}').json()
        LTC = get(f'https://min-api.cryptocompare.com/data/price?fsym=ltc&tsyms={_Set_Currency}').json()
        DGB= get(f'https://min-api.cryptocompare.com/data/price?fsym=dgb&tsyms={_Set_Currency}').json()
        OOE= get(f'https://min-api.cryptocompare.com/data/price?fsym=ooe&tsyms={_Set_Currency}').json()
        DOGE= get(f'https://min-api.cryptocompare.com/data/price?fsym=doge&tsyms={_Set_Currency}').json()
        XRP= get(f'https://min-api.cryptocompare.com/data/price?fsym=xrp&tsyms={_Set_Currency}').json()
        BNB = get(f'https://min-api.cryptocompare.com/data/price?fsym=bnb&tsyms={_Set_Currency}').json()


        if "You are over your rate limit please upgrade your account!" in BTC:
            set_sleep = 60 * 2
            try:
                err_msg = BTC['Message']
            except:
                err_msg = 0
        else:
            Currency_price.append('BTC/USDT:' + str(BTC[_Set_Currency]) + f":{(BTC[_Set_Currency])}")
            Currency_price.append('ETH/USDT:' + str(ETH[_Set_Currency]) + f":{(ETH[_Set_Currency])}")
            Currency_price.append('LTC/USDT:' + str(LTC[_Set_Currency]) + f":{(LTC[_Set_Currency])}")
            Currency_price.append('DGB/USDT:' + str(DGB[_Set_Currency]) + f":{(DGB[_Set_Currency])}")
            Currency_price.append('OOE/USDT:' + str(OOE[_Set_Currency]) + f":{(OOE[_Set_Currency])}")
            Currency_price.append('DOGE/USDT:' + str(DOGE[_Set_Currency]) + f":{(DOGE[_Set_Currency])}")
            Currency_price.append('XRP/USDT:' + str(XRP[_Set_Currency]) + f":{(XRP[_Set_Currency])}")
            Currency_price.append('BNB/USDT:' + str(BNB[_Set_Currency]) + f":{(BNB[_Set_Currency])}")


            Head()
            Currency(Currency_price, set_sleep)
            Currency_price.clear()
        i += 1
    Head()
    console.print(f'''
[!] Error, I think we mistakenly do a ddos instead of fetching cryptocurrency prices\n
Error Message: {err_msg}
\n\n[!] Try again after 5 minutes to run the tool''')


Head();
Starter()
