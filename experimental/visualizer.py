import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
from plotly.subplots import make_subplots

from .utils import identify_num_rows

class Visualizer:
    """
    A class to create and customize data visualizations using Plotly.

    This class provides methods to generate various plots with consistent styling and formatting. It allows customization of plot colors, dimensions, and templates.

    Attributes
    ----------
    color : str
        Color code for plot elements (default: "#94C973")
    height : int
        Height of the plot in pixels (default: 768)
    width : int
        Width of the plot in pixels (default: 1366)
    template : str
        Plotly template name (default: "plotly_white")
    """

    def __init__(self, color = "#94C973", height = 768, width = 1366, template = "plotly_white", colorscale=px.colors.diverging.Earth, style = None): 
        # Initialize visualization parameters
        self.color = color          # Set default color for plot elements
        self.height = height        # Set default plot height
        self.width = width          # Set default plot width
        self.template = template    # Set default plotly template
        self.colorscale = colorscale
        

    def plot_histograms(self, df, specific_cols=[], num_cols=1, title='How distributed the numerical values are?', 
                 subtitle='Histogram of each column with numerical data type', show_mean=False, show_median=False):
        """
        Create multiple histogram subplots for numerical columns in a dataframe.

        Creates a grid of histograms showing the distribution of numerical data. Can optionally show mean and median lines on each histogram.

        Parameters
        ----------
        df : pandas.DataFrame
            Input dataframe containing the data to plot
        specific_cols : list, optional
            List of specific columns to plot (default: empty list, plots all numerical columns)
        num_cols : int, optional
            Number of columns in the subplot grid (default: 1)
        title : str, optional
            Main title of the plot
        subtitle : str, optional
            Subtitle of the plot
        show_mean : bool, optional
            Whether to show mean line on histograms (default: False)
        show_median : bool, optional
            Whether to show median line on histograms (default: False)

        Returns
        -------
        plotly.graph_objects.Figure
            Figure containing the histogram subplots
        """

        # Select columns based on input: either use specific columns or all numerical columns
        if len(specific_cols) >= 1:
            numerical_columns = [column for column in specific_cols if df[column].dtypes in ['int64', 'float64']]
        else:
            numerical_columns = df.select_dtypes(include=np.number).columns.tolist()

        # Calculate number of rows needed based on number of columns and subplots
        num_rows = identify_num_rows(numerical_columns, desired_num_col=num_cols)
    
        # Create subplot grid
        fig = make_subplots(rows=num_rows,
                          cols=num_cols,
                          subplot_titles=numerical_columns,
                          )

        # Create histogram for each numerical column
        for index, col_name in enumerate(numerical_columns):
            # Calculate subplot position
            row = index // num_cols + 1    # Determine row number for current subplot
            col = index % num_cols + 1     # Determine column number for current subplot

            # Add histogram trace
            fig.add_trace(go.Histogram(x=df[col_name],
                                  autobinx=True,
                                  name=col_name,
                                  marker_color=self.color,
                                  ),
                      row=row,
                      col=col)
          
            # Add mean line if requested
            if show_mean:
                fig.add_vline(x=df[col_name].mean(),
                          line_color="#D3D3D3",  
                          line_dash="solid",
                          row=row,
                          col=col)
              
            # Add median line if requested
            if show_median:
                fig.add_vline(x=df[col_name].median(),
                          line_color="#D3D3D3",  
                          line_dash="dot",
                          row=row,
                          col=col)
            
            # Update subplot annotations font size
            fig.update_annotations(font_size=12)

        # Update overall figure layout
        fig.update_layout(title_text=f"{title}<br><sup>{subtitle}<sup>",
                        showlegend=False,
                        height=self.height,
                        width=self.width,
                        title_x=0.5,
                        template=self.template
                      )
        return fig
    
    def plot_correlation_map(self, df, title: str = 'How correlated the numerical values are?', subtitle: str = 'Correlation matrix of columns with numerical data type'):
        """
        Create a correlation matrix heatmap showing relationships between numerical columns.

        Generates a triangular heatmap visualization where each cell shows the correlation between two variables. 
        Only shows the lower triangle to avoid redundancy. 
        Includes hover text and annotations for correlation values.

        Parameters
        ----------
        df : pandas.DataFrame
            Input dataframe containing the numerical columns to correlate
        title : str, optional
            Main title for the plot (default: 'How correlated the numerical values are?')
        subtitle : str, optional
            Subtitle to display below main title (default: 'Correlation matrix of columns with numerical data type')

        Returns
        -------
        plotly.graph_objects.Figure
            Figure containing the correlation heatmap
        """
        # Calculate correlation matrix and round values to 2 decimal places
        corr = df.corr().round(2)  
        
        # Create mask for upper triangle to avoid redundant information
        mask = np.triu(np.ones_like(corr, dtype=bool))
        
        # Apply mask to correlation matrix - sets upper triangle to NaN
        df_mask = corr.mask(mask)

        # Create custom hover text showing correlation between each pair of variables
        hovertext = [[f"{col1} vs {col2}<br>Correlation: {val:.2f}" 
                      if not pd.isna(val) else "" 
                      for col2, val in zip(df_mask.columns, row)]
                    for col1, row in zip(df_mask.index, df_mask.values)]

        # Create annotated heatmap with custom settings
        fig = ff.create_annotated_heatmap(
            z=df_mask.to_numpy(),           # Correlation values
            x=df_mask.columns.tolist(),     # Column names for x-axis
            y=df_mask.columns.tolist(),     # Column names for y-axis
            colorscale=self.colorscale,     # Color scheme for heatmap
            showscale=True,                 # Show color scale
            ygap=1,                         # Gap between y-axis cells
            xgap=1,                         # Gap between x-axis cells
            hoverongaps=False,              # Disable hover on empty cells
            hoverinfo='text',               # Use custom hover text
            text=hovertext                  # Custom hover text
        )

        # Move x-axis labels to bottom of plot
        fig.update_xaxes(side="bottom")

        # Update overall figure layout
        fig.update_layout(
            title_text=f"{title}<br><sup>{subtitle}</sup>", 
            title_x=0.5,                    # Center title
            width=self.width, 
            height=self.height,
            xaxis_showgrid=False,           # Hide x-axis gridlines
            yaxis_showgrid=False,           # Hide y-axis gridlines
            xaxis_zeroline=False,           # Hide x-axis zero line
            yaxis_zeroline=False,           # Hide y-axis zero line
            yaxis_autorange='reversed',     # Reverse y-axis order
            template=self.template,
            xaxis=dict(
                tickangle=90,               # Rotate x-axis labels 90 degrees
            ),
        )

        # Format cell annotations - remove NaN values and format numbers
        for i in range(len(fig.layout.annotations)):
            if fig.layout.annotations[i].text == 'nan':
                fig.layout.annotations[i].text = ""    # Replace NaN with empty string
            else:
                try:
                    value = float(fig.layout.annotations[i].text)
                    fig.layout.annotations[i].text = f"{value:.2f}"    # Format to 2 decimal places
                except ValueError:
                    pass

        return fig

    def plot_correlation_with_target(self, df: pd.DataFrame,
        target_column: str,
        title: str = 'How correlated the features are with the target?',
        subtitle: str = 'Correlation coefficient of each feature'
    ) -> go.Figure:
        """
        Create a horizontal bar chart showing how each feature correlates with a target variable.

        This visualization helps identify which features have strong positive or negative 
        relationships with the target variable. Positive correlations are shown in blue,
        negative in light red. Values range from -1 (perfect negative correlation) to 
        1 (perfect positive correlation).

        Parameters
        ----------
        df : pandas.DataFrame
            Input dataframe containing numerical columns to analyze
        target_column : str
            Name of the column to compare other features against
        title : str, optional
            Main title for the plot (default: 'How correlated the features are with the target?')
        subtitle : str, optional
            Subtitle to display below main title (default: 'Correlation coefficient of each feature')

        Returns
        -------
        plotly.graph_objects.Figure
            Interactive bar chart showing correlation coefficients
        """
        # Calculate correlations with target and sort them
        correlations = df.corr()[target_column].sort_values()
        # Remove target column's correlation with itself (always 1)
        correlations = correlations.drop(target_column)  

        # Assign colors based on correlation direction:
        # Light red for negative correlations, blue for positive
        colors = ['#FF9999' if c < 0 else '#2E75B6' for c in correlations]

        # Initialize empty figure
        fig = go.Figure()

        # Add horizontal bar trace
        fig.add_trace(
            go.Bar(
                y=correlations.index,        # Feature names on y-axis
                x=correlations.values,       # Correlation values on x-axis
                orientation='h',             # Make bars horizontal
                marker_color=colors,         # Color bars based on correlation
                text=[f'{x:.2f}' for x in correlations.values],  # Show correlation values
                textposition='outside',      # Place text outside of bars
            )
        )

        # Configure figure layout
        fig.update_layout(
            title_text=f"{title}<br><sup>{subtitle}</sup>",  # Set two-line title
            title_x=0.5,                    # Center the title
            xaxis=dict(
                title='Correlation Coefficient',
                zeroline=True,              # Show zero reference line
                zerolinewidth=2,            # Make zero line thicker
                gridwidth=1,                # Width of grid lines
                tickformat='.2f'            # Show values to 2 decimal places
            ),
            yaxis=dict(
                title='Features',
                autorange="reversed"        # Reverse feature order to match correlation matrix
            ),
            # Set dynamic height based on number of features, minimum 400px
            height=max(400, len(correlations) * 30),  
            showlegend=False,               # Hide legend
            template=self.template          # Use class-defined template
        )

        return fig
