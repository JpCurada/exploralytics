import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'exploralytics'
copyright = '2024, John Paul Curada'
author = 'John Paul Curada'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'