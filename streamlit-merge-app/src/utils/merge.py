def merge_data(file1, file2, file3):
    import pandas as pd

    # Read the Excel files
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)
    df3 = pd.read_excel(file3)

    # Merge the DataFrames
    merged_df = pd.concat([df1, df2, df3], ignore_index=True)

    return merged_df