import pandas as pd

def extract_csv_text(uploaded_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    # return the DataFrame as a string representation    
    return df.to_string()
