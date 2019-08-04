from numpy import linalg
import pandas

from pubg.deaths import definitions as pubg_deaths_definitions


def kill_distance(deaths_df):
    """
    Return a Series containing the distance between killer and victim for each
    death
    Args:
        deaths_df:

    Returns:
        (pandas.Series)
    """
    X = (
        deaths_df[pubg_deaths_definitions.VICTIM_X] -
        deaths_df[pubg_deaths_definitions.KILLER_X]
    )
    Y = (
        deaths_df[pubg_deaths_definitions.VICTIM_Y] -
        deaths_df[pubg_deaths_definitions.KILLER_Y]
    )
    return (
        pandas.DataFrame({'x': X, 'y': Y}, index=deaths_df.index)
        .apply(lambda xy: linalg.norm(xy.values), axis=1)
    )


def is_suicide(deaths_df):
    """
    Returns a boolean Series indicating whether the death was a suicide for
    each row. Ignores cases where the players are unknown.
    Args:
        deaths_df:

    Returns:
        (pandas.Series)
    """
    return (
        (
                deaths_df[pubg_deaths_definitions.KILLER_NAME] ==
                deaths_df[pubg_deaths_definitions.VICTIM_NAME]
        ) &
        deaths_df[pubg_deaths_definitions.KILLER_NAME].notnull()
    )
