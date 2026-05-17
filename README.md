# Store Sales - Time Series Forecasting

Kaggle competition: predict store sales for Corporación Favorita across multiple stores and product families.

## Project Structure

```
Store Sales/
├── data/
│   ├── raw/                    # original Kaggle data (not committed)
│   └── processed/              # intermediate feature tables
│
├── src/                        # reusable logic modules
│   ├── data.py                 # load and merge all raw tables
│   ├── features.py             # feature engineering (lag, rolling, calendar, promotion)
│   ├── model.py                # model training and prediction interface
│   └── evaluate.py             # RMSLE metric and time-series cross-validation helpers
│
├── scripts/                    # pipeline entry points, run in order
│   ├── 01_eda.py               # exploratory data analysis, outputs plots
│   ├── 02_build_features.py    # run feature engineering, save to data/processed/
│   ├── 03_train.py             # train model, save to outputs/models/
│   ├── 04_predict.py           # generate submission CSV
│   └── 05_validate.py          # walk-forward time-series validation
│
├── outputs/
│   ├── models/                 # saved model files
│   ├── submissions/            # submission CSVs
│   └── plots/                  # EDA and evaluation charts
│
├── config.py                   # paths, hyperparameters, constants
└── requirements.txt
```

## Usage

Run scripts in order:

```bash
python scripts/01_eda.py
python scripts/02_build_features.py
python scripts/03_train.py
python scripts/04_predict.py
```

## Data

Download from [Kaggle](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data) and place in `data/raw/`.

| File | Description |
|------|-------------|
| train.csv | Training sales data |
| test.csv | Test data (dates to predict) |
| stores.csv | Store metadata (city, type, cluster) |
| oil.csv | Daily oil prices |
| holidays_events.csv | Holidays and events |
| transactions.csv | Daily transaction counts |

## Evaluation

RMSLE (Root Mean Squared Log Error)