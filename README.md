# NSE Option Chain Fetcher 📈

![image](https://github.com/user-attachments/assets/your-image.png)

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
**NSE Option Chain Fetcher** is a tool designed to fetch and analyze option chain data from the NSE (National Stock Exchange) API. This project allows users to access real-time and historical option chain data for various stocks.

## Features
- **Real-time Data Fetching**: Retrieves the latest option chain data for specified stocks from NSE.
- **Historical Data Analysis**: Accesses historical option chain data for in-depth analysis.
- **Error Handling**: Includes mechanisms to handle common issues such as HTTP 401 Unauthorized errors.
- **Data Export**: Saves the fetched data into a CSV file for further analysis or reporting.

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
- `dotenv` for loading environment variables from a `.env` file.

You can find all the dependencies listed in the `requirements.txt` file.

## Configuration

Make sure to configure your **NSE API key** as an environment variable:
```bash
export NSE_API_KEY='your-nse-api-key'
