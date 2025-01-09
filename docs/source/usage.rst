Usage Guide
==========

Basic Concepts
-------------

The core of exploralytics is the ``Visualizer`` class, which provides methods for creating various types of plots.

Initialization
-------------

.. code-block:: python

   from exploralytics import Visualizer

   # Create a visualizer with default settings
   viz = Visualizer()

   # Or customize the appearance
   viz = Visualizer(
       color="#2E75B6",      # Main color theme
       height=400,           # Default plot height
       width=800,           # Default plot width
       title_bold=True,     # Bold titles
       texts_font_style='Arial'  # Font family
   )

Creating Plots
-------------

Histogram
^^^^^^^^

.. code-block:: python

   # Single histogram
   fig = viz.plot_histogram(
       df,
       x_col='values',
       title='Distribution',
       show_mean=True,
       show_median=True
   )

Bar Plot
^^^^^^^

.. code-block:: python

   # Bar plot with highlighted values
   fig = viz.plot_bar(
       df,
       x_col='category',
       y_col='values',
       highlight_top_n=(3, "green"),
       highlight_low_n=(2, "red")
   )

Correlation Analysis
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Correlation with target variable
   fig = viz.plot_correlation_with_target(
       df,
       target_column='target',
       title='Feature Correlations'
   )

Displaying Plots
--------------

All plotting methods return a Plotly Figure object that can be:

.. code-block:: python

   # Displayed in a notebook
   fig.show()

   # Saved to a file
   fig.write_html("plot.html")
   fig.write_image("plot.png")