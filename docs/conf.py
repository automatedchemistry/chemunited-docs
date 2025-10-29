# Configuration file for the Sphinx documentation builder.

project = 'Chemunited'
copyright = '2025, X'
author = 'X'
release = '0.1.0'

# Add extensions
extensions = [
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinxcontrib.video',
    'sphinxext.opengraph',
]

# Use Markdown and reStructuredText
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Theme
html_theme = 'furo'

# Add custom static files (for custom CSS, logos, etc.)
html_static_path = ['_static']

# Optional: add your logo and favicon
html_logo = "_static/chemunited.svg"
html_favicon = "_static/favicon.ico"

# MyST markdown settings (for more flexible formatting)
myst_enable_extensions = [
    "colon_fence",  # ::: blocks
    "deflist",      # definition lists
    "linkify",      # auto link URLs
    "substitution", # variable placeholders
]

# Custom CSS (optional)
html_css_files = [
    'custom.css',
]
