import pandas as pd
import json
import requests
import time

def data_extractor(symbol):
    count = 0
    while True:
        try:
            # nse option chain 
            url = f'https://www.nseindia.com/api/option-chain-indices?symbol={symbol}'
            headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8'
                        }
            session = requests.session()
            request =  session.get(url , headers= headers)
            json_con =  request.json()
            df =  pd.DataFrame(json_con)
            data =  pd.DataFrame(df['filtered']['data'])
            
            pe_data_frame = data['PE']
            ce_data_frame = data['CE']
            underlying_price = 0
            # ce list 
            ce_iv_list =[]
            ce_oi_list=[]
            ce_chg_list=[]
            ce_ltp_list=[]
            ce_vol_list=[]

            # pe list 
            pe_iv_list =[]
            pe_oi_list=[]
            pe_chg_list=[]
            pe_ltp_list=[]
            pe_vol_list=[]


            strike_price_list = []
            for i in range(len(pe_data_frame)):
                underlying_price =  pe_data_frame[i]['underlyingValue']
                strike_price_list.append(data['strikePrice'][i])
                # ce_list 
                ce_iv_list.append(ce_data_frame[i]['impliedVolatility'])
                ce_oi_list.append(ce_data_frame[i]['openInterest'])
                ce_chg_list.append(ce_data_frame[i]['changeinOpenInterest'])
                ce_ltp_list.append(ce_data_frame[i]['lastPrice'])
                ce_vol_list.append(ce_data_frame[i]['totalTradedVolume'])
                # pe_list 
                pe_iv_list.append(pe_data_frame[i]['impliedVolatility'])
                pe_oi_list.append(pe_data_frame[i]['openInterest'])
                pe_chg_list.append(pe_data_frame[i]['changeinOpenInterest'])
                pe_ltp_list.append(pe_data_frame[i]['lastPrice'])
                pe_vol_list.append(pe_data_frame[i]['totalTradedVolume'])



            # option geeks 
            url = f'https://webapi.niftytrader.in/webapi/option/fatch-option-chain?symbol={symbol}'
            headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8'
                        }
            session = requests.session()
            request =  session.get(url , headers= headers)
            json_con =  request.json()
            df =  pd.DataFrame(json_con['resultData']['opDatas'])
            ce_delta_list=[]
            ce_theta_list=[]
            ce_gamma_list=[]
            pe_delta_list=[]
            pe_theta_list=[]
            pe_gamma_list=[]
            for i in range(len(df)):
                ce_delta_list.append(df['call_delta'][i])
                ce_theta_list.append(df['call_theta'][i])
                ce_gamma_list.append(df['call_gamma'][i])

                pe_delta_list.append(df['put_delta'][i])
                pe_theta_list.append(df['put_theta'][i])
                pe_gamma_list.append(df['put_gamma'][i])
            data = {
                "Delta (Calls)": ce_delta_list,
                "Theta (Calls)": ce_theta_list,
                "Gamma (Calls)": ce_gamma_list,
                "IV (Calls)":ce_iv_list,
                "OI (Calls)": ce_oi_list,
                "Changing OI (Calls)":ce_chg_list,
                "LTP (Calls)": ce_ltp_list,
                "Volume (Calls)": ce_vol_list,
                "Strike Price": strike_price_list,
                "Delta (Puts)": pe_delta_list,
                "Theta (Puts)":pe_theta_list,
                "Gamma (Puts)":pe_gamma_list,
                "IV (Puts)": pe_iv_list,
                "OI (Puts)": pe_oi_list,
                "Changing OI (Puts)": pe_chg_list,
                "LTP (Puts)": pe_ltp_list,
                "Volume (Puts)": pe_vol_list,
                }
            table_data =  pd.DataFrame(data)
            table_data['Gamma (Calls)'] = table_data['Gamma (Calls)'].apply(lambda x: '{:.5f}'.format(x) if pd.notnull(x) else x)
            table_data['Gamma (Puts)'] = table_data['Gamma (Puts)'].apply(lambda x: '{:.5f}'.format(x) if pd.notnull(x) else x)
            return {'table_data':table_data, 'underlying_price':underlying_price}
        
        except:
            print("trying again", count)
            time.sleep(5)
            count+=1



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
