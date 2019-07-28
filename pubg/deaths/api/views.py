
def suicides(deaths_df):
    """
    Return a DataFrame of all suicides. Excludes cases where either player
    was not known
    Args:
        deaths_df:

    Returns:
        (pandas.DataFrame)
    """
    is_suicide = (
        (deaths_df['killer_name'] == deaths_df['victim_name']) &
        deaths_df['killer_name'].notnull()
    )
    return deaths_df[is_suicide]
