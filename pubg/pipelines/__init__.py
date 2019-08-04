def run_transform_pipeline(df, transform_funcs):
    output = df
    for func in transform_funcs:
        output = output.pipe(func)
    return output
