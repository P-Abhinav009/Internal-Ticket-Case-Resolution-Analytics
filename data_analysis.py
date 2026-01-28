import pandas as pd
import numpy as np
from datetime import datetime

def load_and_clean_data(file_path):
    """Loads ticket data and performs initial cleaning."""
    print("--- Loading Data ---")
    df = pd.read_csv(file_path)

    # Convert date columns to datetime objects
    df['Created_Date'] = pd.to_datetime(df['Created_Date'])
    df['Resolved_Date'] = pd.to_datetime(df['Resolved_Date'])

    # Fill missing Resolution Dates with a placeholder for open tickets (optional)
    # Or drop rows where Created_Date is null
    df = df.dropna(subset=['Created_Date'])
    
    return df

def perform_aging_analysis(df):
    """Calculates ticket aging and categorizes them into buckets."""
    print("--- Performing Aging Analysis ---")
    
    # Calculate Resolution Time in days
    # For resolved tickets: Resolved - Created. For open tickets: Today - Created.
    today = pd.Timestamp(datetime.now())
    
    df['Resolution_Time_Days'] = (df['Resolved_Date'] - df['Created_Date']).dt.total_seconds() / (24 * 3600)
    
    # Fill Open Tickets aging based on today's date
    df['Ticket_Age_Days'] = df.apply(
        lambda x: (today - x['Created_Date']).days if pd.isnull(x['Resolved_Date']) else x['Resolution_Time_Days'],
        axis=1
    )

    # Create Aging Buckets
    bins = [0, 1, 3, 7, 14, np.inf]
    labels = ['0-1 Day', '1-3 Days', '3-7 Days', '7-14 Days', '14+ Days']
    df['Aging_Bucket'] = pd.cut(df['Ticket_Age_Days'], bins=bins, labels=labels)

    return df

def calculate_kpis(df):
    """Calculates Key Performance Indicators: SLA Compliance and FCR."""
    print("--- Calculating KPIs ---")

    # 1. SLA Compliance (Threshold: 3 days / 72 hours)
    SLA_THRESHOLD = 3
    df['SLA_Status'] = np.where(df['Ticket_Age_Days'] <= SLA_THRESHOLD, 'Met', 'Breached')

    # 2. First Contact Resolution (FCR) 
    # Logic: If Interaction_Count is 1 and status is Resolved
    df['Is_FCR'] = (df['Interaction_Count'] == 1) & (df['Status'] == 'Resolved')

    # Calculate percentages for the summary
    sla_rate = (df['SLA_Status'] == 'Met').mean() * 100
    fcr_rate = df['Is_FCR'].mean() * 100
    avg_res_time = df['Resolution_Time_Days'].mean()

    print(f"SLA Compliance Rate: {sla_rate:.2f}%")
    print(f"FCR Rate: {fcr_rate:.2f}%")
    print(f"Average Resolution Time: {avg_res_time:.2f} days")

    return df

def generate_report(df, output_path):
    """Saves the processed data for Power BI visualization."""
    df.to_csv(output_path, index=False)
    print(f"--- Processed data saved to {output_path} ---")

if __name__ == "__main__":
    # Define paths
    INPUT_FILE = 'data/sample_data.csv'
    OUTPUT_FILE = 'data/processed_tickets.csv'

    # Run Pipeline
    try:
        raw_data = load_and_clean_data(INPUT_FILE)
        analyzed_data = perform_aging_analysis(raw_data)
        final_data = calculate_kpis(analyzed_data)
        generate_report(final_data, OUTPUT_FILE)
        
        # Displaying a sample of the results
        print("\nAnalysis Preview:")
        print(final_data[['Ticket_ID', 'Ticket_Age_Days', 'Aging_Bucket', 'SLA_Status', 'Is_FCR']].head())
        
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found. Please ensure sample data exists.")