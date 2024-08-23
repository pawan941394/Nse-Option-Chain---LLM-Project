import pandas as pd
import json
import requests
def data_extractor(option):

    url = f'https://195.3.220.223/api/option-chain-indices?symbol=NIFTY&__cpo=aHR0cHM6Ly93d3cubnNlaW5kaWEuY29t'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8'
            }

    response = requests.get(url)
    rawdata = pd.DataFrame(response)
    rawop = pd.DataFrame(rawdata['filtered']['data']).fillna(0)


    # *********************************
    url_g = f"https://webapi.niftytrader.in/webapi/option/fatch-option-chain?symbol={option}"
    request = session.get(url_g, headers=headers)
    request.raise_for_status()
    response_2 = session.get(url_g, headers=headers).json()
    rawdata_2 = pd.DataFrame(response_2)
    rawop_2 = pd.DataFrame(rawdata_2['resultData']['opDatas']).fillna(0)
    call_delta_list = []
    call_theta_list = []
    call_gamma_list = []
    put_delta_list = []
    put_theta_list = []
    put_gamma_list = []
    for i in range(len(rawop)):
        call_delta_list.append(rawop_2['call_delta'][i])
        call_theta_list.append(rawop_2['call_theta'][i])
        call_gamma_list.append(rawop_2['call_gamma'][i])
        put_delta_list.append(rawop_2['put_delta'][i])
        put_theta_list.append(rawop_2['put_theta'][i])
        put_gamma_list.append(rawop_2['put_gamma'][i])
    # /***************    Data Gethering *******************/
    data = []
    call_oi_list = []
    call_coi_list = []
    call_last_price_list = []
    call_iv_list = []
    call_volumne_list = []

    put_oi_list = []
    put_coi_list = []
    put_last_price_list = []
    put_iv_list = []
    put_volumne_list = []
    strike_price_list =[]
    underlying_price = 0
    for i in range(len(rawop)):
        calloi = callcoi = cltp = putoi = putcoi = pltp = 0
        strike_price_list.append(rawop['strikePrice'][i])
        underlying_price =rawop['PE'][i]['underlyingValue']
        
        call_oi_list.append(rawop['CE'][i]['openInterest'])
        call_coi_list.append(rawop['CE'][i]['changeinOpenInterest'])
        call_last_price_list.append(rawop['CE'][i]['lastPrice'])
        call_iv_list.append(rawop['CE'][i]['impliedVolatility'])
        call_volumne_list.append(rawop['CE'][i]['totalTradedVolume'])

        put_oi_list.append(rawop['PE'][i]['openInterest'])
        put_coi_list.append(rawop['PE'][i]['changeinOpenInterest'])
        put_last_price_list.append(rawop['PE'][i]['lastPrice'])
        put_iv_list.append(rawop['PE'][i]['impliedVolatility'])
        put_volumne_list.append(rawop['PE'][i]['totalTradedVolume'])

    # Data for the table
    data = {
        "Delta (Calls)": call_delta_list,
        "Theta (Calls)": call_theta_list,
        "Gamma (Calls)": call_gamma_list,
        "IV (Calls)":call_iv_list,
        "OI (Calls)": call_oi_list,
        "Changing OI (Calls)":call_coi_list,
        "LTP (Calls)": call_last_price_list,
        "Volume (Calls)": call_volumne_list,
        "Strike Price": strike_price_list,
        "Delta (Puts)": put_delta_list,
        "Theta (Puts)":put_theta_list,
        "Gamma (Puts)":put_gamma_list,
        "IV (Puts)": put_iv_list,
        "OI (Puts)": put_oi_list,
        "Changing OI (Puts)": put_coi_list,
        "LTP (Puts)": put_last_price_list,
        "Volume (Puts)": put_volumne_list,
    }

    # Convert to DataFrame
    df = pd.DataFrame(data)
    df['Gamma (Calls)'] = df['Gamma (Calls)'].apply(lambda x: '{:.5f}'.format(x) if pd.notnull(x) else x)
    df['Gamma (Puts)'] = df['Gamma (Puts)'].apply(lambda x: '{:.5f}'.format(x) if pd.notnull(x) else x)
    return {'df':df, 'underlying_price':underlying_price}


def calculate_atm_price(selected_option, underlying_price):
    atm_price = 0
    temp_und = underlying_price
    get_first = list(str(temp_und).split("."))[0]
    get_first_digit = str(get_first)
    last_two_dig = int(get_first_digit[-2:])

    if selected_option == 'NIFTY':
        if last_two_dig < 25:
            atm_price = int(underlying_price) - last_two_dig 
        elif last_two_dig <= 50:
            atm_price = int(underlying_price) - last_two_dig + 50
        elif last_two_dig <= 75:
            atm_price = int(underlying_price) - last_two_dig + 50
        else:
            atm_price = int(underlying_price) - last_two_dig + 100
    elif selected_option == 'BANKNIFTY':
        if last_two_dig < 50:
            atm_price = int(underlying_price) - last_two_dig
        else:
            atm_price = int(underlying_price) - last_two_dig + 100

    return atm_price


def calculate_pcr(df):
    # Ensure df is not empty
    if df.empty:
        return None

    # Calculate the sum of open interest (OI) for calls and puts
    call_oi_sum = df['OI (Calls)'].sum()
    
    put_oi_sum = df['OI (Puts)'].sum()
    # Handle division by zero
    if call_oi_sum == 0:
        return None  # Or handle it in a way that suits your application

    # Calculate PCR
    pcr = put_oi_sum / call_oi_sum
    
    # Round PCR to 2 decimal places
    pcr_rounded = round(pcr, 3)
    return pcr_rounded
