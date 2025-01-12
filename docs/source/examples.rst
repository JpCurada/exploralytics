Examples
========

This page contains comprehensive examples for each plot type available in Exploralytics.

Setting Up Example Data
----------------------

First, let's create some sample data to use in our examples::

    import pandas as pd
    import numpy as np
    
    # Create sample numerical data
    np.random.seed(42)
    data = {
        'sales': np.random.normal(1000, 200, 1000),
        'profit': np.random.normal(300, 80, 1000),
        'customers': np.random.normal(500, 150, 1000),
        'marketing_spend': np.random.normal(200, 50, 1000),
        'satisfaction': np.random.normal(4.2, 0.5, 1000)
    }
    df = pd.DataFrame(data)
    
    # Create sample categorical data
    categories = {
        'product_category': ['Electronics', 'Clothing', 'Food', 'Books', 'Sports'],
        'revenue': [120000, 85000, 65000, 45000, 35000]
    }
    df_categories = pd.DataFrame(categories)

1. Histogram Plots
----------------

Single Column Histogram
~~~~~~~~~~~~~~~~~~~~~

Create a histogram for a single column::

    viz.plot_histograms(
        df,
        specific_cols=['sales'],
        title='Sales Distribution',
        subtitle='Distribution of sales values',
        show_mean=True,
        show_median=True
    )

Multiple Column Histograms
~~~~~~~~~~~~~~~~~~~~~~~~

Create histograms for multiple columns in a grid::

    viz.plot_histograms(
        df,
        num_cols=2,
        title='Key Metrics Distribution',
        subtitle='Distribution of various business metrics',
        show_mean=True
    )

2. Correlation Matrix
-------------------

Create a correlation heatmap::

    viz.plot_correlation_map(
        df,
        title='Correlation Analysis',
        subtitle='Relationship between different metrics',
        footer='Data from Q3 2023'
    )

Customization options:

* Custom color scale
* Interactive hover information
* Automatic handling of upper triangle

3. Correlation with Target
------------------------

Analyze feature correlations with a target variable::

    viz.plot_correlation_with_target(
        df,
        target_column='profit',
        title='Profit Correlations',
        subtitle='How different metrics correlate with profit',
        footer='Based on 2023 data'
    )

Features:

* Automatic sorting by correlation strength
* Color coding for positive/negative correlations
* Interactive tooltips

4. Horizontal Bar Plot
--------------------

Simple Category Distribution
~~~~~~~~~~~~~~~~~~~~~~~~~

Create a simple horizontal bar plot::

    viz.plot_hbar(
        df_categories,
        x_col='product_category',
        title='Product Categories',
        subtitle='Distribution of product categories'
    )

Advanced Bar Plot
~~~~~~~~~~~~~~~

Create a bar plot with highlighting and reference line::

    viz.plot_hbar(
        df_categories,
        x_col='product_category',
        y_col='revenue',
        title='Revenue by Category',
        subtitle='Total revenue for each product category',
        add_hline=True,                    # Add mean line
        top_n=3,                           # Show only top 3
        highlight_top_n=(2, '#2E75B6'),    # Highlight top 2 in blue
        highlight_low_n=(1, '#FF9999')     # Highlight bottom 1 in red
    )

5. Dot Plot
----------

Basic Dot Plot
~~~~~~~~~~~~

Create a simple dot plot::

    viz.plot_dot(
        df_categories,
        x_col='product_category',
        y_col='revenue',
        title='Revenue by Category',
        subtitle='Revenue distribution across product categories'
    )

Advanced Dot Plot
~~~~~~~~~~~~~~~

Create a dot plot with reference line and highlighting::

    viz.plot_dot(
        df_categories,
        x_col='product_category',
        y_col='revenue',
        title='Revenue by Category',
        subtitle='Revenue distribution across product categories',
        add_hline_at=('Average', 70000),    # Add reference line
        highlight_top_n=(2, '#2E75B6'),     # Highlight top 2
        highlight_low_n=(1, '#FF9999')      # Highlight bottom 1
    )

Real-World Examples
-----------------

Sales Analysis
~~~~~~~~~~~~

Here's a complete example analyzing sales data::

    # Load sales data
    sales_data = pd.read_csv('sales.csv')
    
    # Create visualizer
    viz = Visualizer(template='plotly_white')
    
    # Distribution of sales
    viz.plot_histograms(
        sales_data,
        specific_cols=['daily_sales'],
        title='Daily Sales Distribution',
        show_mean=True
    )
    
    # Sales by category
    viz.plot_hbar(
        sales_data,
        x_col='category',
        y_col='total_sales',
        title='Sales by Category',
        highlight_top_n=(3, '#2E75B6')
    )
    
    # Correlation analysis
    viz.plot_correlation_map(
        sales_data,
        title='Sales Metrics Correlation'
    )

Customer Analysis
~~~~~~~~~~~~~~~

Example of customer data analysis::

    # Load customer data
    customer_data = pd.read_csv('customers.csv')
    
    # Customer satisfaction distribution
    viz.plot_histograms(
        customer_data,
        specific_cols=['satisfaction_score'],
        title='Customer Satisfaction Distribution'
    )
    
    # Correlation with satisfaction
    viz.plot_correlation_with_target(
        customer_data,
        target_column='satisfaction_score',
        title='Factors Affecting Satisfaction'
    )