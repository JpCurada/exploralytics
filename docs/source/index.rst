Welcome to exploralytics documentation!
=====================================

A powerful toolkit for data exploration and visualization using Plotly.

.. image:: https://badge.fury.io/py/exploralytics.svg
    :target: https://badge.fury.io/py/exploralytics
    :alt: PyPI version

.. image:: https://readthedocs.org/projects/exploralytics/badge/?version=latest
    :target: https://exploralytics.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Features
--------
* Interactive data visualization with Plotly backend
* Consistent styling and modern design
* Easy-to-use API for common visualization tasks
* Support for various plot types:
  - Histograms (single and multiple)
  - Bar plots with customizable highlighting
  - Correlation analysis plots
  - Multi-subplot layouts

Quick Start
-----------

Installation
^^^^^^^^^^^

.. code-block:: bash

   pip install exploralytics

Basic Usage
^^^^^^^^^^

.. code-block:: python

   from exploralytics import Visualizer

   # Initialize the visualizer
   viz = Visualizer(
       color="#2E75B6",
       height=400,
       width=800,
       title_bold=True
   )

   # Create a simple histogram
   fig = viz.plot_histogram(
       df,
       x_col='values',
       title='Distribution of Values'
   )

   # Display the plot
   fig.show()

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   usage
   visualization
   examples

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api

Links
-----
* `PyPI Package <https://pypi.org/project/exploralytics/>`_
* `Source Code <https://github.com/jpcurada/exploralytics>`_
* `Issue Tracker <https://github.com/jpcurada/exploralytics/issues>`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`