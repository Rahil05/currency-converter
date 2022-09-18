from requests import get
from pprint import PrettyPrinter

# this program contains 2 APIs
API_KEY_curr = '22ad9672d907de1cef43cb81'
API_KEY_crypto = 'da8bd4f8534c75274f3ac30816933658'
BASE_URL_curr = "https://v6.exchangerate-api.com/"
BASE_URL_crypto = 'http://api.coinlayer.com/api/'

printer = PrettyPrinter()

def get_currencies():
    #endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url_curr = BASE_URL_curr + "v6/" + API_KEY_curr + "/latest/USD"
    data_curr = get(url_curr).json()['conversion_rates']
    
    #printer.pprint(data)
    #print(data)
   # data = list(data.items())
   # data.sort()
    
    return data_curr

data_curr = get_currencies()

def get_crypto():

  url_crypto = BASE_URL_crypto + 'live?access_key=' + API_KEY_crypto
  data_crypto = get(url_crypto).json()['rates']
  #print(data_crypto)
  return data_crypto

data_crypto = get_crypto()

def get_currencyid():

    Currency_id1 = list(data_curr.keys())
  
    Currency_id = Currency_id1 
    
    return  Currency_id

Currency_id = get_currencyid()

def get_cryptoid():

    Crypto_id1 = list(data_crypto.keys())
   
    Crypto_id = Crypto_id1 
    return Crypto_id
    

Crypto_id = get_cryptoid()

def main():
 

    print("Welcome to Currency/Crypto Converter")
    print("List of commands: q or 1(to quit), Currency Conv(2), Crypto Conv(3), Crypto to Currency(4),Currency/Crypto(Exchange rate)(5) Currency/Crypto_id(6), Currency/Crypto_data(7)")
    while True:


        Command = input("Enter Command: ")
        if Command == 'q':
          print("Thank You")
          break
       
        elif Command == '6':
            _id = input("Currency id: 1, Crypto id: 2: ")
            if _id == '1':
             print(Currency_id)
            elif _id =='2':
             print(Crypto_id)
        elif Command == '7': 
            data1 = input("Currency_data:1, Crypto_data:2 : ")
            if data1 =='1':

               print(data_curr)
            elif data1 == '2':
                print(data_crypto)
        elif Command == '5':
          Exch_rate = input("Exch rate currency=1, Exch rate crypto=2: ") 
          if Exch_rate == '1':

            Exch_rate_curr = input("Enter Currency_id: ")
            print(1/data_curr[Exch_rate_curr],'USD')
          elif Exch_rate == '2':
            Exch_rate_crypto = input("Enter Crypto id: ")
            print(data_crypto[Exch_rate_crypto],'USD')

        elif Command == '2':

          currency1_id = input("Enter curreny1:")
          currency1_id = currency1_id.upper()
          if currency1_id not in Currency_id:
            
            print("Invalid Currency1id")
            continue
          currency2_id = input('Enter currency2:')
          currency2_id = currency2_id.upper()
          if currency2_id  not in Currency_id:
            print("Invalid Currency2id")
            
          else:
            Amount = float(input("Enter Amount:"))
          
            currency1 = data_curr[currency1_id]
            currency2 = data_curr[currency2_id]
            
            Exchange_value = Amount*(currency2/currency1)
            print(Exchange_value,currency2_id)

        elif Command == '3':

          crypto1_id = input("Enter crypto1:")
          if crypto1_id not in Crypto_id:
            
            print("Invalid crypto1id")
            continue
          crypto2_id = input('Enter crypto2:')
          if crypto2_id  not in Crypto_id:
            print("Invalid Crypto2id")
            
          else:
            Amount_curr = float(input("Enter Amount:"))
          
            crypto1 = data_crypto[crypto1_id]
            crypto2 = data_crypto[crypto2_id]
            
            Exchange_value = Amount_curr*(crypto1/crypto2)
            print(Exchange_value,crypto2_id)
          
        elif Command == '4':
            Amount_crypto = float(input("Enter Amount:"))
            Crypto = input("Enter Crypto:")
            Exch_to = input("Exchange to: ")
            
            Crypto_Value = Amount_crypto*data_crypto[Crypto]*data_curr[Exch_to]
            print(Crypto_Value)


        else:
          print("Invalid Command")
        

main()

