from dateutil import relativedelta
import pandas as pd

# unitTime looks something like this '6:03'
def convertTimetoNumbers(unitTime):
  parts = unitTime.split(":")
  m, s = int(parts[0]) , int(parts[1])
  return m * 60 + s

def convertSecondsToMinutes(time):
  m = int(time // 60)
  s = int(time % 60)
  return f"{m}:{s}"

df = pd.read_csv('./python-foundation/tmm19.csv')

print('Analysis Tata Mumbai Marathon 19')
print(df.head())

print('Clean Up');

df.drop(df.columns[[5,6,7,10,11,12,13,15,16,18,19,20,21,26,27]], axis=1,  inplace=True)

print('Removed 15 Columns');

print(df.head())

print('\n########## BASIC ##########\n')


print("\n1. What is the average pace across all laps?")
# avg_pace = df['Avg Pace']

df["pace_seconds"] = df["Avg Pace"].apply(convertTimetoNumbers)
average_pace_in_seconds = df['pace_seconds'].mean();
avg_pace_rounded = round(average_pace_in_seconds, 2)
# convert back to timeunits
print("Average Pace: ", convertSecondsToMinutes(avg_pace_rounded))

print("\n2. Which lap had the highest cadence?")
max_cadeance = df['Avg Run Cadence'].max()
# print(df["Avg Run Cadence"].head())
print(max_cadeance)
print(df[df['Avg Run Cadence']==max_cadeance])
# seconda variant
#idMaxCadance  = df["Avg Run Cadence"].idxmax()
# print(df.iloc[idMaxCadance])
print("\n3. How many laps had a pace faster than 5:15?")
threshold_in_sec = convertTimetoNumbers("5:15")
laps_faster =  df[df['pace_seconds'] < threshold_in_sec ]
print('Laps ran faster than 5:15 ', len(laps_faster))





print("\n4. Show only laps where Total Ascent > 0")
print("\n5. Sort laps by Avg Pace (slowest to fastest)")
print("\n6. Find laps where you slowed down compared to the previous lap")

print("7. Split the race into 3 segments (early/mid/late) and compare average pace per segment")
print("8. What's the average stride length for laps faster vs slower than 5:20?")

print("9. Add a column pace_seconds converting Avg Pace (mm:ss string) to total seconds")
print("10. Add a column fatigue_index = pace_seconds of current lap minus lap 1's pace_seconds")

print("11. At which lap did your performance peak? Define 'peak' yourself and justify it.")
print("12. Plot pace over laps as a line chart (use matplotlib)")


