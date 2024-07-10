import pandas as pd


def group_by_text_columns(file_path: str) -> pd.DataFrame:
    """
    This function reads a CSV file and groups all values by the 'Text' and 'AdditionalText' columns present in the file.

    :param file_path: Path to the CSV file
    :return: A DataFrame with grouped data by 'Text' and 'AdditionalText' columns
    """
    df = pd.read_csv(file_path)
    # Get all columns from the DataFrame
    columns = df.columns

    # Filter columns that have 'object' dtype (text columns)
    text_columns = [col for col in columns if df[col].dtype == 'object']

    # Group by text columns
    grouped = df.groupby(list(text_columns)).first().reset_index()

    return grouped


if __name__ == '__main__':
    file_path = 'test-1.csv'
    grouped_data = group_by_text_columns(file_path)
    print(grouped_data)
