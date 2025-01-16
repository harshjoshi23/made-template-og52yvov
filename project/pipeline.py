import pandas as pd
import requests
from sqlalchemy import create_engine
import io
import os

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    raw_data = pd.read_csv(io.StringIO(response.text))
    return raw_data

def clean_data(df, key_column):
    if key_column in df.columns:
        cleaned_df = df.dropna(subset=[key_column])
    else:
        cleaned_df = df  
    return cleaned_df

def ensure_directory(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def store_data(df, db_name, table_name):
    ensure_directory(db_name) 
    engine = create_engine(f'sqlite:///{db_name}')
    df.to_sql(table_name, con=engine, index=False, if_exists='replace')

def main():
    # URLs
    facilities_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/prisons/facilities.csv'
    us_data_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'
    systems_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/prisons/systems.csv'
    us_states_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/refs/heads/master/us-states.csv'

    # Fetch data from URLs
    facilities_df = fetch_data(facilities_url)
    us_data_df = fetch_data(us_data_url)
    systems_df = fetch_data(systems_url)
    us_states_df = fetch_data(us_states_url)

    # Clean data
    facilities_df = clean_data(facilities_df, 'facility_name')
    us_data_df = clean_data(us_data_df, 'cases')  
    systems_df = clean_data(systems_df, 'total_inmate_cases')
    us_states_df = clean_data(us_states_df, 'state')  # Assuming 'state' is a key column

    # Store data in SQLite database
    store_data(facilities_df, '../data/covid_data.sqlite', 'facilities')
    store_data(us_data_df, '../data/covid_data.sqlite', 'us_data')
    store_data(systems_df, '../data/covid_data.sqlite', 'systems')
    store_data(us_states_df, '../data/covid_data.sqlite', 'us_states')

if __name__ == "__main__":
    main()
