import pandas as pd


def _transform(path_temp_csv):

    # read temp dataset
    dataset = pd.read_csv(path_temp_csv)
    
    # Transformations - atributes
    dataset["name"] = dataset["first_name"] + " " + dataset["last_name"]
    
    dataset.drop(
        ["emp_no", "first_name", "last_name"],
        axis=1,
        inplace=True
    )
    
    # Save data into temp directory
    dataset.to_csv(
        path_temp_csv,
        index=False
    )
