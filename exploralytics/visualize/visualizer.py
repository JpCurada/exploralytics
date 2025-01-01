"""
Core visualization module for creating interactive plots with Plotly.
Provides a unified interface for data visualization tasks.
"""

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from typing import List, Optional, Union, Dict

from .utils import (
    check_data,
    get_number_columns,
    calc_subplot_size,
    identify_plot_layout,
    suggest_bin_count,
    validate_color
)
from .style import (
    DEFAULT_STYLE,
    apply_style,
    get_color_palette,
    create_custom_style
)


class Visualizer:
    """
    Create interactive data visualizations using Plotly.

    This class provides methods for common data visualization tasks,
    maintaining consistent styling while allowing customization.

    Attributes:
        color: Main color used in plots
        height: Default height for plots in pixels
        width: Default width for plots in pixels
        style: Dictionary of plot styling settings

    Examples:
        >>> import pandas as pd
        >>> from exploralytics.visualize import Visualizer
        >>> 
        >>> # Create sample data
        >>> df = pd.DataFrame({
        ...     'A': [1, 2, 3],
        ...     'B': [4, 5, 6]
        ... })
        >>> 
        >>> # Initialize visualizer and create plot
        >>> viz = Visualizer()
        >>> fig = viz.plot_histograms(df, title='Data Distribution')
        >>> fig.show()
    """

    def __init__(
        self,
        color: str = '#94C973',
        height: int = 600,
        width: int = 800,
        style: Optional[Dict] = None
    ):
        """
        Initialize the visualization tool.

        Args:
            color: Main color for plots (default: '#94C973')
            height: Default plot height in pixels (default: 600)
            width: Default plot width in pixels (default: 800)
            style: Custom style settings (default: None, uses default style)

        Raises:
            ValueError: If provided color is not a valid hex code
        """
        # Validate color format
        if not validate_color(color):
            raise ValueError(
                "Color must be a valid hex code (e.g., '#94C973')"
            )
        
        self.color = color
        self.height = height
        self.width = width
        self.style = style or DEFAULT_STYLE.copy()

    def plot_distributions(
        self,
        data: pd.DataFrame,
        title: str,
        subtitle: str = '',
        columns: Optional[List[str]] = None,
        layout: Optional[Dict] = None
    ) -> go.Figure:
        """
        Create distribution plots for numerical columns.

        Combines histograms, box plots, and density curves for comprehensive
        distribution analysis.

        Args:
            data: DataFrame containing the data to plot
            title: Main title for the plot
            subtitle: Additional text below title (default: '')
            columns: Specific columns to plot (default: None, uses all numeric)
            layout: Custom layout settings (default: None)

        Returns:
            Plotly figure object containing distribution plots

        Raises:
            ValueError: If data is empty or no numeric columns found

        Examples:
            >>> viz = Visualizer()
            >>> fig = viz.plot_distributions(
            ...     df,
            ...     title='Feature Distributions',
            ...     subtitle='Dataset Overview'
            ... )
            >>> fig.show()
        """
        # Validate input data
        check_data(data)
        number_cols = get_number_columns(data, columns)
        
        # Get optimal layout
        n_rows, n_cols = identify_plot_layout(len(number_cols))
        
        # Calculate dimensions
        total_height = n_rows * 300  # 300px per row
        
        # Create subplot figure
        fig = make_subplots(
            rows=n_rows,
            cols=n_cols,
            subplot_titles=number_cols,
            vertical_spacing=0.1
        )
        
        # Add plots for each column
        for idx, col_name in enumerate(number_cols):
            row = (idx // n_cols) + 1
            col = (idx % n_cols) + 1
            
            # Add histogram
            hist_values, hist_bins = np.histogram(
                data[col_name].dropna(),
                bins=suggest_bin_count(data[col_name])
            )
            
            fig.add_trace(
                go.Histogram(
                    x=data[col_name],
                    name=f'{col_name} (Histogram)',
                    marker_color=self.color,
                    opacity=0.7,
                    showlegend=False
                ),
                row=row,
                col=col
            )
            
            # Add box plot
            fig.add_trace(
                go.Box(
                    x=data[col_name],
                    name=f'{col_name} (Box)',
                    marker_color=self.color,
                    boxpoints='outliers',
                    orientation='h',
                    showlegend=False
                ),
                row=row,
                col=col
            )
        
        # Update layout
        title_text = f"{title}<br><sup>{subtitle}</sup>" if subtitle else title
        
        return apply_style(
            fig=fig,
            title=title_text,
            style=self.style,
            height=total_height,
            width=self.width
        )