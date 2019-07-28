import pandas

from pubg.deaths import definitions as pubg_deaths_definitions

FIELDS = {
    'killed_by', 'str',
    'killer_name', 'str',
    'killer_placement', 'float64',
    'killer_position_x', 'float64',
    'killer_position_y', 'float64',
    'map', 'str',
    'match_id', 'str',
    'time', 'int64',
    'victim_name', 'str',
    'victim_placement', 'float64',
    'victim_position_x', 'float64',
    'victim_position_y', 'float64',
}

MISSING_VALUES = ['#unknown']


def read_deaths_file_to_dataframe(filepath, **kwargs):
    # Read data
    df = pandas.read_csv(
        filepath,
        na_values=MISSING_VALUES,
        skip_blank_lines=True,
        **kwargs
    )
    # Normalize all coordinates to metres from 0
    # Metres are standard unit for distance in PUBG
    position_field_mappings = (
        (pubg_deaths_definitions.KILLER_X, 'killer_position_x'),
        (pubg_deaths_definitions.KILLER_Y, 'killer_position_y'),
        (pubg_deaths_definitions.VICTIM_X, 'victim_position_x'),
        (pubg_deaths_definitions.VICTIM_Y, 'victim_position_y'),
    )
    for new_name, old_name in position_field_mappings:
        # Int64 type allows null values
        df[new_name] = (df[old_name] // 100).astype('Int64')
        df.drop(old_name, axis='columns', inplace=True)

    return df
