Visualization Types
================

This page details all available visualization types in exploralytics.

Histograms
---------

Single Histogram
^^^^^^^^^^^^^

.. code-block:: python

   viz.plot_histogram(
       df,
       x_col='column_name',
       title='Distribution',
       subtitle='Optional subtitle',
       show_mean=True,
       show_median=True
   )

Multiple Histograms
^^^^^^^^^^^^^^^^

.. code-block:: python

   viz.plot_histograms(
       df,
       specific_cols=['col1', 'col2'],
       num_cols=2,
       show_mean=True
   )

Bar Plots
--------

Basic Bar Plot
^^^^^^^^^^^

.. code-block:: python

   viz.plot_bar(
       df,
       x_col='category',
       y_col='values'
   )

Highlighted Bar Plot
^^^^^^^^^^^^^^^^^

.. code-block:: python

   viz.plot_bar(
       df,
       x_col='category',
       y_col='values',
       highlight_top_n=(3, "green"),
       highlight_low_n=(2, "red")
   )

Correlation Analysis
-----------------

Target Correlation
^^^^^^^^^^^^^^^

.. code-block:: python

   viz.plot_correlation_with_target(
       df,
       target_column='target',
       title='Correlation Analysis'
   )

Customization
-----------

All plots can be customized using the Visualizer initialization parameters:

.. code-block:: python

   viz = Visualizer(
       color="#custom_color",
       height=custom_height,
       width=custom_width,
       title_bold=True/False,
       texts_font_style='custom_font'
   )