![image](https://github.com/user-attachments/assets/5f050d17-2943-47ac-95a6-b2e61a62c21e)![image](https://github.com/user-attachments/assets/1643f10e-d8e0-45f2-bb4c-684ce4b230fc)# NSE Option Chain Fetcher With Gen AI📈

![image](https://github.com/user-attachments/assets/9272742d-50b8-4cf7-bc47-70635395bb27)


<!-- Replace with the URL to your screenshot -->

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Contributing](#contributing)

## Overview
**NSE Option Chain Fetcher** is a tool designed to fetch and analyze option chain data from the NSE (National Stock Exchange) API. This project allows users to access real-time and calculate the parameters on real time and Gen AI which help you to get the insight of the data.

## Features
- **Real-time Data Fetching**: Retrieves the latest option chain data for specified stocks from NSE.
- **Different Parameters Calculating**: Interactive dashboard which will help you to calculate the different parameter's on real time data.
- **Gen AI**: Gen AI chat bot which is designed to get to know more about market. 
- **Error Handling**: Includes mechanisms to handle common issues such as HTTP 401 Unauthorized errors

## Process
- **Signup Step**: Signup first with simple username and password.
 ![image](https://github.com/user-attachments/assets/1e53797f-243f-4375-9347-e237e56f2f12)
- **Login Step**: Login with your username and password.
  ![image](https://github.com/user-attachments/assets/b884d17c-020a-414a-8580-d6e4cc865bc5)
- **Live Dashboard**: Login with your username and password.
  ![image](https://github.com/user-attachments/assets/b884d17c-020a-414a-8580-d6e4cc865bc5)
![image](https://github.com/user-attachments/assets/62e8812d-2763-4590-8181-d624c4590753)
- **Gen AI Chatbot**: Gen AI Chat bot with live market data.
![image](https://github.com/user-attachments/assets/352de91f-051b-4f36-9e0a-1ef40eb341f5)



## Installation

### Prerequisites
Before you can run this tool, you need to have the following installed:
- Python 3.8 or above
- NSE API access (API key from NSE)
- Required Python libraries

### Step-by-Step Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/nse-option-chain-fetcher.git
    cd nse-option-chain-fetcher
    ```

2. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your NSE API key:
    - In your project directory, create a `.env` file or directly export it in your terminal:
      ```bash
      export NSE_API_KEY='your-nse-api-key'
      ```

## Usage

1. To run the application, navigate to the project directory and run the following command:
    ```bash
    python nse_option_chain_fetcher.py
    ```

2. The application will fetch the option chain data based on the stock symbol you provide.

3. The fetched data will be saved into a CSV file in the `data` directory.

## Dependencies

The key dependencies for this project are:
- `requests` for making HTTP requests to the NSE API.
- `pandas` for handling and analyzing data.

You can find all the dependencies listed in the `requirements.txt` file.

## Configuration

Make sure to configure your **NSE API key** as an environment variable:
```bash
export NSE_API_KEY='your-nse-api-key'
