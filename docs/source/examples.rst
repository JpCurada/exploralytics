Examples
========

Basic Examples
------------

Simple Histogram
^^^^^^^^^^^^^

.. code-block:: python

   import pandas as pd
   from exploralytics import Visualizer

   # Create sample data
   df = pd.DataFrame({
       'values': range(100)
   })

   # Create visualization
   viz = Visualizer()
   fig = viz.plot_histogram(
       df,
       x_col='values',
       title='Sample Distribution'
   )
   fig.show()

Feature Analysis
--------------

.. code-block:: python

   # Load your dataset
   df = pd.read_csv('your_data.csv')

   # Create visualizer
   viz = Visualizer(color="#2E75B6")

   # Plot correlations with target
   fig = viz.plot_correlation_with_target(
       df,
       target_column='target',
       title='Feature Importance'
   )
   fig.show()

Categorical Analysis
-----------------

.. code-block:: python

   # Create bar plot with highlights
   fig = viz.plot_bar(
       df,
       x_col='category',
       y_col='sales',
       title='Sales by Category',
       highlight_top_n=(3, "green")
   )
   fig.show()