import pandas as pd
from datetime import datetime

def clean_ticket_data(file_path):
    df = pd.read_excel(file_path)
    
    # Convert dates
    df['Created_Date'] = pd.to_datetime(df['Created_Date'])
    df['Resolved_Date'] = pd.to_datetime(df['Resolved_Date'])
    
    # Calculate Ticket Aging (in days)
    df['Aging_Days'] = (df['Resolved_Date'] - df['Created_Date']).dt.days
    
    # Identify SLA Status
    df['SLA_Status'] = df.apply(lambda x: 'Met' if x['Aging_Days'] <= 2 else 'Breached', axis=1)
    
    # First Contact Resolution (FCR) - Logic check
    df['Is_FCR'] = df['Interaction_Count'] == 1
    
    return df

if __name__ == "__main__":
    data = clean_ticket_data('data/raw_tickets.xlsx')
    data.to_csv('data/processed_tickets.csv', index=False)