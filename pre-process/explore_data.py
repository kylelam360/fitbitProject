import pandas as pd

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

for dataset in datasets:
    df = pd.read_csv(dataset)
    unique_ids = df["Id"].nunique()
    print(f"Unique User IDs in {dataset}: {unique_ids}")
