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


# Finding number of unique id's for each dataset
# for dataset in datasets:
#     df = pd.read_csv(dataset)
#     unique_ids = df["Id"].nunique()
#     print(f"Unique User IDs in {dataset}: {unique_ids}")


# Finding min and max MET value by each unique user id
df = pd.read_csv("master_minuteMETsNarrow.csv")
result = df.groupby('Id')['METs'].agg(['min', 'max']).reset_index()
print(result)

# Finding mode of MET values
mode_value = df['METs'].mode().iloc[0]
print(f"Mode of METs: is {mode_value}")

# Count of mode MET value
count_10 = (df['METs'] == 10).sum()
print(f"Number of METs == 10: {count_10}")

# Determining if 0's in dataset are real due to infrequency in visual
print((df['METs'] == 0).sum())
print(df[df['METs'] == 0].head())