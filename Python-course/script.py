"""
Created by: Xuan Hong

"""

def custom_sort(data, grouping_col, sorting_col, sorting_value = 'sum', direct = False):
    import pandas as pd
    """
    Given a dataframe, a column and a sorting value, return a sorting dataframe that has been
    grouped by the column and a sorting based on the value desired.
    
    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The dataframe to sample from
    grouping_col : str
        The column to group the data on
    sorting_col : str
        After grouping, the column to sort
    sorting_value : str, optional
        The desired value of the sorting column.The default is the 
        sum value.
    direct : bool, optional
        Sorting direction. The default is False, descending.
         
        
    Returns
    -------
    pandas.core.frame.DataFrame 
        A dataframe with the group by column and the sorting result of the desired value.
        
    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    AssertError
        If the input argument grouping_col is not in the data columns
    AssertError
        If the input argument sorting_col is not in the data columns
    
    Examples
    --------
    >>> custom_sort(helper_data, 'type', 'diameter','sum', False)
	type	diameter
	Cherry	 75.5
    Oak	     56.5

    """
    
    # Checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(data, pd.DataFrame): 
        raise TypeError("The data argument is not of type DataFrame")
    
    # Tests that the the grouping column is in the dataframe
    assert grouping_col in data.columns, "The grouping column does not exist in the dataframe"
    
    # Tests that the the sorting column is in the dataframe
    assert sorting_col in data.columns, "The sorting column does not exist in the dataframe"
    
    
    # compute the groupby object based on the value of interest column
    res = data.groupby(grouping_col).agg({sorting_col:sorting_value})
    
    # sort the values
    res = res.sort_values(by=sorting_col, ascending=direct)
    
    # convert to a dataframe
    res = pd.DataFrame(res)
    
    # reset the index
    res = res.reset_index()
    
    # return the result
    return(res)

