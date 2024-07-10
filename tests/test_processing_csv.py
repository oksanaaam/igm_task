import pandas as pd
from processing_csv import group_by_text_columns


def test_group_by_text_columns() -> None:
    grouped_data = group_by_text_columns('test-1.csv')

    # Assertions
    assert isinstance(grouped_data, pd.DataFrame), "Returned object is not a DataFrame"
    assert grouped_data.shape[0] == 10, "Expected 10 rows in grouped data"  # Adjust based on your CSV data

    # Check if all 'Text' values are unique in the grouped data
    assert grouped_data['Text'].is_unique, "Grouped 'Text' values are not unique"

    # Check if all rows have the correct columns
    expected_columns = {'Text', 'Numeric1', 'Numeric2', 'Numeric3', 'AdditionalText'}
    assert set(
        grouped_data.columns) == expected_columns, f"Expected columns {expected_columns}, but got {set(grouped_data.columns)}"
