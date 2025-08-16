# Stock Market Prediction with Machine Learning

<img width="1050" height="550" alt="image" src="https://github.com/user-attachments/assets/c83dabdc-e2ef-4ec9-aebf-2bd3da5a67e1" />

## About

Developed ML/DL based a web application for stock price prediction based on real-time data. Our Stock Price Prediction with Machine Learning website, utilizing linear regression and Django, enables users to predict stock prices based on real-time data. With easy-to-use interfaces and insightful graphs, users can make informed investment decisions.

## Introduction

Welcome to Stock Price Prediction with Machine Learning! My website, powered by linear regression and a Django App, provides real-time data of stock prices on the home page. To predict stock prices, simply navigate to the prediction page, enter a valid ticker value and the number of days you want to predict, and click the predict button. This page displays the predicted stock price along with the details of the searched ticker. We also generate a unique QR Code for easy access to the predicted results. On the prediction page, you'll find two graphs: the left graph shows the real-time stock price of the searched ticker for the past day, while the right graph displays the predicted stock price for the specified number of days. Additionally, our Ticker Info page provides comprehensive details about all the valid tickers accepted by the application.

## Aim

**Title:** Using data analysis to predict stock price

**Aim:** To predict stock prices according to real-time data values fetched from API.

## Objective

Develop a web application for stock price prediction based on real-time data.

## Scope

The project is applicable to any business organization, providing users with stock price prediction capabilities and comprehensive summary data.

## Technology Used

- **Languages:** HTML, CSS, JavaScript, Python
- **Framework:** Bootstrap, Django
- **Machine Learning Algorithms:** Multiple Linear Regression
- **ML/DL Libraries:** NumPy, Pandas, scikit-learn
- **Database:** SQLite
- **APIs:** Yahoo Finance API, REST API
- **IDE:** VS Code, Jupyter Notebook

## Project Installation

### STEP 1: Clone the repository from GitHub
```bash
git clone https://github.com/mian-arsal138/-using-data-analysis-to-predict-stock-price.git
```

### STEP 2: Change the directory to the repository
```bash
cd -using-data-analysis-to-predict-stock-price
```

### STEP 3: Create a virtual environment (For Windows)
```bash
python -m venv virtualenv
```

### STEP 4: Activate the virtual environment (For Windows)
```bash
virtualenv\Scripts\activate
```

### STEP 5: Install the dependencies
```bash
pip install -r requirements.txt
```

### STEP 6: Migrate the Django project (For Windows)
```bash
python manage.py migrate
```

### STEP 7: Run the application (For Windows)
```bash
python manage.py runserver
```

## Features

- **Real-time Stock Data:** Get live stock prices and market data
- **Stock Price Prediction:** Predict future stock prices using machine learning
- **Interactive Graphs:** Visualize historical and predicted stock data
- **QR Code Generation:** Easy access to prediction results
- **Comprehensive Ticker Information:** Detailed information about all supported tickers
- **User-friendly Interface:** Modern, responsive design with Bootstrap

## Project Structure

```
-Stock-market-Prediction-with-Machine-Learning-Django/
├── app/                    # Main Django application
│   ├── Data/              # CSV files with ticker data
│   ├── static/            # CSS, JS, and image files
│   ├── templates/         # HTML templates
│   ├── models.py          # Database models
│   └── views.py           # View functions
├── core/                  # Django project settings
│   ├── settings.py        # Project configuration
│   └── urls.py           # URL routing
├── requirements.txt       # Python dependencies
└── manage.py             # Django management script
```

## Usage

1. **Home Page:** View real-time stock prices and market overview
2. **Search Page:** Enter a ticker symbol and number of days for prediction
3. **Results Page:** View predicted prices with interactive graphs
4. **Ticker Info:** Browse comprehensive information about all supported tickers

## Screenshots

### Homepage with active stocks
<img width="1042" height="614" alt="image" src="https://github.com/user-attachments/assets/785a3861-a2b8-4f29-9971-124dec8e65be" />

<img width="1042" height="640" alt="image" src="https://github.com/user-attachments/assets/67179074-5923-44b9-97de-1d6cba0093d1" />

### Search ticker value page
<img width="1043" height="572" alt="image" src="https://github.com/user-attachments/assets/b3896833-af68-45ca-8f33-cd1d62e185ce" />

### Result page with information and prediction graph
<img width="1042" height="571" alt="image" src="https://github.com/user-attachments/assets/e409b8cd-ed7c-4fb9-9b8b-8ef47b8c567f" />

<img width="1048" height="626" alt="image" src="https://github.com/user-attachments/assets/ef4a8319-7496-4777-9734-1903db1f980d" />

### All ticker symbols and names
<img width="1043" height="588" alt="image" src="https://github.com/user-attachments/assets/e69d8628-8594-43dd-b92b-3adedf265634" />

### Error page
<img width="1044" height="605" alt="image" src="https://github.com/user-attachments/assets/55c85d29-be31-4fb5-8b01-6c03c150c9ce" />

## Conclusion

Our Stock Price Prediction with Machine Learning website, utilizing linear regression and Django, enables users to predict stock prices based on real-time data. With easy-to-use interfaces and insightful graphs, users can make informed investment decisions. We provide comprehensive ticker information and ensure accurate predictions through our machine learning algorithms.

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License.

## Thank you!
