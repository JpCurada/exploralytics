def identify_num_rows(
    columns: list[str], 
    desired_num_col: int
) -> int:
    """
    Calculate how many rows are needed to display a set of plots in a grid layout.

    Determines the number of rows needed to fit all plots when organizing them into 
    columns. Handles both when plots divide evenly into columns and when they don't.

    Parameters
    ----------
    columns : list
        List of items that need to be arranged in a grid
    desired_num_col : int
        Number of columns to arrange the plots into

    Returns
    -------
    int
        Number of rows needed for the grid layout
    """
    # If plots divide evenly into columns, use simple division
    if (len(columns) % desired_num_col) == 0:
        num_rows = len(columns) // desired_num_col
    # If plots don't divide evenly, add an extra row to fit remaining plots
    else:
        num_rows = (len(columns) // desired_num_col) + 1
    
    return num_rows