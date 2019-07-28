import pandas


def read_and_concat_dfs(filepaths, read_func):
    """
    Read each file in the provided iterable of filepaths and concatenate them
    into on DataFrame.

    The resulting DataFrame will have an Int64Index from 0...N-1
    Args:
        filepaths: iterable of filepaths
        read_func: function which reads each component file into a DataFrame

    Returns:
        (pandas.DataFrame)
    """
    return pandas.concat(
        (read_func(filepath) for filepath in filepaths),
        ignore_index=True
    )
