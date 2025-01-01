# exploralytics/main.py

import pandas as pd
import numpy as np
from exploralytics.visualize import Visualizer

def create_sample_data():
    """Create sample data for demonstration."""
    np.random.seed(42)
    
    # Create a dataset with different types of distributions
    n_samples = 1000
    df = pd.DataFrame({
        'normal': np.random.normal(0, 1, n_samples),
        'uniform': np.random.uniform(-3, 3, n_samples),
        'exponential': np.random.exponential(2, n_samples),
        'sales': np.random.normal(100, 15, n_samples),
        'date': pd.date_range('2023-01-01', periods=n_samples)
    })
    
    # Add some correlations
    df['correlated'] = df['normal'] * 0.7 + np.random.normal(0, 0.3, n_samples)
    
    return df

def main():
    """Main function to demonstrate visualizations."""
    # Create sample data
    df = create_sample_data()
    
    # Initialize visualizer
    viz = Visualizer(color='#006400')  
    
    # 1. Distribution plots
    dist_fig = viz.plot_histograms(
        df,
        title='Distribution Analysis',
        num_cols=3,
        subtitle='Looking at different variable distributions'
    )
    dist_fig.show()
    
    # # 2. Correlation analysis
    # corr_fig = viz.plot_correlation(
    #     df[['normal', 'uniform', 'exponential', 'correlated']],
    #     title='Correlation Analysis'
    # )
    # corr_fig.show()
    
    # # 3. Time series analysis
    # time_fig = viz.plot_time_series(
    #     df,
    #     date_column='date',
    #     value_column='sales',
    #     title='Sales Over Time'
    # )
    # time_fig.show()
    
    # Custom styling example
    viz.update_style(font_size=14, title_x=1)
    custom_fig = viz.plot_histograms(
        df,
        title='Custom Styled Plot',
        columns=['normal', 'uniform'],
        num_cols=2,
        subtitle='With larger font size'
    )
    custom_fig.show()

if __name__ == "__main__":
    main()