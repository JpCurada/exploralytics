"""
Style configurations and functions for Exploralytics visualizations.

This module provides:
1. Default style settings for consistent plot appearance
2. Style application functions
3. Color scheme definitions
"""

from typing import Dict, Optional
import plotly.graph_objects as go


# Default style settings
DEFAULT_STYLE = {
    # Font settings
    'font_size': 12,
    'font_family': 'Arial, sans-serif',
    'title_size': 16,
    
    # Layout settings
    'title_x': 0.5,  # Center title
    'width': 800,
    'height': 600,
    
    # Margins
    'margins': {
        'left': 50,
        'right': 50,
        'top': 80,
        'bottom': 50
    },
    
    # Colors
    'color_scale': 'RdBu',  # Red to Blue scale for correlations
    'background_color': 'white',
    'grid_color': '#E5E5E5',
    
    # Grid settings
    'show_grid': True,
    'grid_width': 1,
    
    # Legend settings
    'show_legend': True,
    'legend_position': {
        'x': 1.02,
        'y': 1,
        'xanchor': 'left',
        'yanchor': 'top'
    }
}

# Color palettes for different types of data
COLOR_PALETTES = {
    'categorical': [
        '#636EFA', '#EF553B', '#00CC96', '#AB63FA', 
        '#FFA15A', '#19D3F3', '#FF6692', '#B6E880'
    ],
    'sequential': [
        '#F0F921', '#FABA39', '#F48849', '#DE5F65', 
        '#BC3F86', '#8C2981', '#4F127B', '#000004'
    ],
    'diverging': [
        '#2A788E', '#7AD4E6', '#B6EEF4', '#FFFFFF',
        '#F8B7A1', '#E45641', '#B40426'
    ]
}


def apply_style(
    fig: go.Figure,
    title: str,
    style: Dict,
    height: Optional[int] = None,
    width: Optional[int] = None
) -> go.Figure:
    """
    Apply consistent styling to a plotly figure.

    Args:
        fig: Plotly figure to style
        title: Title for the plot
        style: Dictionary of style settings
        height: Custom height (default: None, uses style default)
        width: Custom width (default: None, uses style default)

    Returns:
        Styled plotly figure

    Examples:
        >>> fig = go.Figure()
        >>> styled_fig = apply_style(fig, "My Plot", DEFAULT_STYLE)
    """
    fig.update_layout(
        # Title settings
        title={
            'text': title,
            'x': style['title_x'],
            'xanchor': 'center',
            'font': {
                'size': style['title_size'],
                'family': style['font_family']
            }
        },
        
        # Size settings
        height=height or style['height'],
        width=width or style['width'],
        
        # Margins
        margin=style['margins'],
        
        # Background colors
        paper_bgcolor=style['background_color'],
        plot_bgcolor=style['background_color'],
        
        # Font settings
        font=dict(
            size=style['font_size'],
            family=style['font_family']
        ),
        
        # Legend settings
        showlegend=style['show_legend'],
        legend=style['legend_position']
    )
    
    # Update axes with grid settings
    fig.update_xaxes(
        showgrid=style['show_grid'],
        gridwidth=style['grid_width'],
        gridcolor=style['grid_color'],
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor='black'
    )
    
    fig.update_yaxes(
        showgrid=style['show_grid'],
        gridwidth=style['grid_width'],
        gridcolor=style['grid_color'],
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor='black'
    )
    
    return fig


def get_color_palette(
    palette_type: str = 'categorical',
    num_colors: Optional[int] = None
) -> list:
    """
    Get a color palette for plots.

    Args:
        palette_type: Type of palette ('categorical', 'sequential', 'diverging')
        num_colors: Number of colors needed (default: None, returns full palette)

    Returns:
        List of color hex codes

    Examples:
        >>> colors = get_color_palette('categorical', 3)
        >>> print(colors)  # First 3 categorical colors
    """
    if palette_type not in COLOR_PALETTES:
        raise ValueError(
            f"Invalid palette type. Choose from: {list(COLOR_PALETTES.keys())}"
        )
    
    palette = COLOR_PALETTES[palette_type]
    
    if num_colors:
        # Repeat palette if more colors needed
        return (palette * (num_colors // len(palette) + 1))[:num_colors]
    
    return palette


def create_custom_style(**kwargs) -> Dict:
    """
    Create custom style by modifying default settings.

    Args:
        **kwargs: Style parameters to override

    Returns:
        Dictionary with custom style settings

    Examples:
        >>> custom = create_custom_style(font_size=14, show_grid=False)
    """
    custom_style = DEFAULT_STYLE.copy()
    custom_style.update(kwargs)
    return custom_style