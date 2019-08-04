from pubg.deaths import definitions as pubg_deaths_definitions
from pubg.deaths.api import features as pubg_deaths_api_features


def suicides(deaths_df):
    """
    Return a DataFrame of all suicides. Excludes cases where either player
    was not known
    Args:
        deaths_df:

    Returns:
        (pandas.DataFrame)
    """
    is_suicide = pubg_deaths_api_features.is_suicide(deaths_df)
    return deaths_df[is_suicide]


def exclude_null_positions(deaths_df):
    """
    Exclude entries where either the play or victim position is unknown
    Args:
        deaths_df:

    Returns:
        (pandas.DataFrame)
    """
    no_null_position = (
        deaths_df[pubg_deaths_definitions.KILLER_X].notnull() &
        deaths_df[pubg_deaths_definitions.KILLER_Y].notnull() &
        deaths_df[pubg_deaths_definitions.VICTIM_X].notnull() &
        deaths_df[pubg_deaths_definitions.VICTIM_Y].notnull()
    )
    return deaths_df[no_null_position]


def add_kill_distance(deaths_df):
    """
    Return the input DataFrame with a new column for the kill distance
    Args:
        deaths_df:

    Returns:
        (pandas.DataFrame)
    """
    kill_distance_series = pubg_deaths_api_features.kill_distance(deaths_df)
    deaths_df[pubg_deaths_definitions.KILL_DISTANCE] = kill_distance_series
    return deaths_df


def restrict_to_map(deaths_df, mapname):
    """
    Restrict the DataFrame to entries on the given game map
    Args:
        deaths_df:
        mapname: A valid map name

    Returns:
        (pandas.DataFrame)
    """
    on_map = deaths_df[pubg_deaths_definitions.MAPNAME] == mapname
    return deaths_df[on_map]
