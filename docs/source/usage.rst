Usage
=====

Getting Started
-------------

To use Exploralytics in a project::

    from exploralytics import Visualizer

Creating a Visualizer Instance
---------------------------

The Visualizer class is the main interface for creating plots. You can customize its appearance globally::

    viz = Visualizer(
        color="#94C973",           # Main color for plots
        height=768,                # Plot height in pixels
        width=1366,                # Plot width in pixels
        template="simple_white",    # Plotly template
        texts_font_style="Arial",   # Font family
        title_bold=True            # Bold titles
    )

Customization Options
-------------------

Global Parameters
~~~~~~~~~~~~~~~

* ``color``: Main color for plot elements (default: "#94C973")
* ``height``: Height of plots in pixels (default: 768)
* ``width``: Width of plots in pixels (default: 1366)
* ``template``: Plotly template name (default: "simple_white")
* ``texts_font_style``: Font family for text elements
* ``title_bold``: Whether to make titles bold (default: False)

Plot-Specific Parameters
~~~~~~~~~~~~~~~~~~~~~~

Common parameters available for all plots:

* ``title``: Main title of the plot
* ``subtitle``: Subtitle shown below the main title
* ``footer``: Optional footer text

Additional parameters vary by plot type and are documented in the :ref:`examples` section.

Working with Data
---------------

Exploralytics works with pandas DataFrames. Here's how to prepare your data::

    import pandas as pd
    
    # Load your data
    df = pd.read_csv('your_data.csv')
    
    # Create visualizations
    viz.plot_histograms(df)
    viz.plot_correlation_map(df)

Best Practices
------------

1. Data Preparation
~~~~~~~~~~~~~~~~~

* Clean your data before visualization
* Handle missing values appropriately
* Ensure numerical columns are correctly typed

2. Plot Customization
~~~~~~~~~~~~~~~~~~~

* Use consistent styling across related plots
* Choose appropriate color schemes for your data
* Add meaningful titles and subtitles

3. Performance
~~~~~~~~~~~~

* For large datasets, consider using the ``top_n`` parameter
* Use ``specific_cols`` to limit histogram generation
* Be mindful of memory usage with large correlation matrices

Troubleshooting
-------------

Common Issues
~~~~~~~~~~~~

1. **Missing Data**::

    # Handle missing values before plotting
    df = df.dropna()  # or df.fillna(value)

2. **Type Errors**::

    # Ensure correct data types
    df['numeric_column'] = pd.to_numeric(df['numeric_column'], errors='coerce')

3. **Memory Issues**::

    # Limit data size
    df = df.head(1000)  # or use appropriate sampling