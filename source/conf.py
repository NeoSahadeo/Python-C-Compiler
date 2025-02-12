import sys
from pathlib import Path

sys.path.insert(0, str(Path('..', 'compiler').resolve()))

project = 'Python C Compiler'
copyright = '2025, Neo Sahadeo'
author = 'Neo Sahadeo'
release = '0'

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []


html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
