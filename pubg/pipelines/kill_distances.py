from pubg import pipelines as pubg_pipelines
from pubg.deaths import (io as pubg_deaths_io,
                         definitions as pubg_deaths_definitions)
from pubg.deaths.api import (features as pubg_deaths_api_features,
                             transforms as pubg_deaths_api_transforms)

"""
Build dataset for investigating the distances at which players were killed
"""

TRANSFORM_PIPELINE = (
    pubg_deaths_api_transforms.exclude_null_positions,
    pubg_deaths_api_transforms.add_kill_distance
)


def build_kill_distance_dataset(input_filename, output_filename):
    deaths_df = pubg_deaths_io.read_deaths_file_to_dataframe(
        input_filename
    )
    transformed = pubg_pipelines.run_transform_pipeline(
        deaths_df, TRANSFORM_PIPELINE
    )
    pubg_deaths_io.save_file_to_csv(transformed, output_filename)
