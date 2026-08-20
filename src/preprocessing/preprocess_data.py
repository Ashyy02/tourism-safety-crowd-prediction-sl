import pandas as pd


def preprocess_data(input_file, output_file):
    """
    Load, clean and prepare tourism data for machine learning.
    """

    data = pd.read_csv(input_file)

    # Remove duplicate records
    data = data.drop_duplicates()

    # Handle missing numerical values
    numerical_columns = data.select_dtypes(
        include=["int64", "float64"]
    ).columns

    for column in numerical_columns:
        data[column] = data[column].fillna(data[column].median())

    # Handle missing categorical values
    categorical_columns = data.select_dtypes(
        include=["object"]
    ).columns

    for column in categorical_columns:
        if not data[column].mode().empty:
            data[column] = data[column].fillna(
                data[column].mode()[0]
            )

    # Save processed data
    data.to_csv(output_file, index=False)

    print("Data preprocessing completed successfully.")


if __name__ == "__main__":
    print("Tourism Safety and Crowd Prediction - Data Preprocessing")
