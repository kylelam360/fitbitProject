import pandas as pd
import os


def update_master(master_path, new_batch_path):
    """
    update_master updates aggregation of earlier csv datasets (master dataset csv) with the most recent batch

    :param master_path: path for aggregate of earlier csv dataset(s)
    :param new_batch_path: path for new batch to update master csv dataset
    :return: aggregated csv dataset that becomes new master csv dataset
    """
    if os.path.exists(master_path):
        master = pd.read_csv(master_path)
    else:
        master = pd.DataFrame()

    new_batch = pd.read_csv(new_batch_path)
    updated = pd.concat([master, new_batch]).drop_duplicates()
    updated.to_csv(master_path, index=False)
    print(f"Updated master path: {master_path}")


# Aggregating batch datasets for fitbit into master csv datasets
# Note: "Wide" csv datasets are missing first day's data contained in "Narrow" csv datasets
datasets = [
    "master_dailyActivity.csv",
    "master_dailyCalories.csv",
    "master_dailyIntensities.csv",
    "master_dailySteps.csv",
    "master_heartrate_seconds.csv",
    "master_hourlyCalories.csv",
    "master_hourlyIntensities.csv",
    "master_hourlySteps.csv",
    "master_minuteCaloriesNarrow.csv",
    "master_minuteCaloriesWide.csv",
    "master_minuteIntensitiesNarrow.csv",
    "master_minuteIntensitiesWide.csv",
    "master_minuteMETsNarrow.csv",
    "master_minuteSleep.csv",
    "master_minuteStepsNarrow.csv",
    "master_minuteStepsWide.csv",
    "master_sleepDay.csv",
    "master_weightLogInfo.csv"
]


# Base path goes up one level: 'archive/' folder containing batch files is a sibling directory to the folder
# containing master csv datasets
base_batch_path = "../archive/"

batch_folders = [
    "mturkfitbit_export_3.12.16-4.11.16/Fitabase Data 3.12.16-4.11.16",
    "mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16"
]

# Iterate over batch datasets to update each corresponding master csv dataset with new batch data
for batch_folder in batch_folders:
    for dataset in datasets:

        # Convert master filename to corresponding batch filename
        batch_filename = dataset.replace("master_", "").replace(".csv", "_merged.csv")

        batch_file = f"{base_batch_path}{batch_folder}/{batch_filename}"

        # Check if path exists for csv datasets not in first batch that are in the second
        if os.path.exists(batch_file):
            print(f"Updating {dataset} with batch {batch_file} ...")
            update_master(dataset, batch_file)
        else:
            continue
