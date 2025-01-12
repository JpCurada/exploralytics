Welcome to Exploralytics's documentation!
====================================

**Exploralytics** is a powerful data visualization library built on top of Plotly, designed to create beautiful, interactive visualizations with minimal code. It provides a consistent API and styling across different types of plots while maintaining full customization capabilities.

.. image:: https://badge.fury.io/py/exploralytics.svg
    :target: https://badge.fury.io/py/exploralytics
    :alt: PyPI version

.. image:: https://readthedocs.org/projects/exploralytics/badge/?version=latest
    :target: https://exploralytics.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Features
--------

* Easy-to-use interface for creating complex visualizations
* Consistent styling and customization options
* Interactive plots powered by Plotly
* Support for various plot types:
    * Histograms with distribution analysis
    * Correlation matrices
    * Feature correlation analysis
    * Horizontal bar plots
    * Dot plots with reference lines

Getting Started
--------------

To get started with Exploralytics, check out the following sections:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   examples

Quick Example
------------

Here's a quick example of using Exploralytics::

    from exploralytics import Visualizer
    import pandas as pd

    # Initialize the visualizer
    viz = Visualizer()

    # Create a simple histogram
    viz.plot_histograms(
        df,
        title='Data Distribution',
        show_mean=True,
        show_median=True
    )

Contributing
-----------

Contributions are welcome! Please feel free to submit a Pull Request.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`