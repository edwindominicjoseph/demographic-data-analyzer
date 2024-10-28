import pandas as pd

# Load and clean the dataset
data = pd.read_csv('C:/Users/edj36/OneDrive/Documents/demographicdata.csv')  # Update with actual file path
data.columns = [col.strip() for col in data.columns]
data.columns = [
    'age', 'workclass', 'fnlwgt', 'education', 'education_num', 
    'marital_status', 'occupation', 'relationship', 'race', 'sex', 
    'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'salary'
]
data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# 1. Count of people by race
race_counts = data['race'].value_counts()

# 2. Average age of men
average_age_men = data[data['sex'] == 'Male']['age'].mean()

# 3. Percentage of people with a Bachelor's degree
bachelors_percentage = (data['education'].value_counts(normalize=True).get('Bachelors', 0)) * 100

# 4. Percentage of people with advanced education (Bachelors, Masters, or Doctorate) making >50K
advanced_education = data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
advanced_education_rich = data[advanced_education & (data['salary'] == '>50K')]
advanced_education_percentage = (len(advanced_education_rich) / len(data[advanced_education])) * 100

# 5. Percentage of people without advanced education making >50K
non_advanced_education = ~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
non_advanced_education_rich = data[non_advanced_education & (data['salary'] == '>50K')]
non_advanced_education_percentage = (len(non_advanced_education_rich) / len(data[non_advanced_education])) * 100

# 6. Minimum number of hours worked per week
min_hours_per_week = data['hours_per_week'].min()

# 7. Percentage of people who work the minimum hours and earn >50K
min_hours_workers = data[data['hours_per_week'] == min_hours_per_week]
min_hours_rich_percentage = (len(min_hours_workers[min_hours_workers['salary'] == '>50K']) / len(min_hours_workers)) * 100

# 8. Country with the highest percentage of people earning >50K
country_counts = data['native_country'].value_counts()
rich_country_counts = data[data['salary'] == '>50K']['native_country'].value_counts()
country_rich_percentage = (rich_country_counts / country_counts * 100).dropna()
highest_earning_country = country_rich_percentage.idxmax()
highest_earning_percentage = country_rich_percentage.max()

# 9. Most popular occupation for those who earn >50K in India
india_rich = data[(data['native_country'] == 'India') & (data['salary'] == '>50K')]
most_common_occupation_india_rich = india_rich['occupation'].mode()[0] if not india_rich.empty else None

# Display results
print("Count of people by race:\n", race_counts)
print("Average age of men:", average_age_men)
print("Percentage with Bachelor's degree:", bachelors_percentage)
print("Percentage with advanced education making >50K:", advanced_education_percentage)
print("Percentage without advanced education making >50K:", non_advanced_education_percentage)
print("Minimum number of hours worked per week:", min_hours_per_week)
print("Percentage of people working minimum hours with >50K salary:", min_hours_rich_percentage)
print("Country with highest percentage of >50K earners:", highest_earning_country, "-", highest_earning_percentage)
print("Most popular occupation for >50K earners in India:", most_common_occupation_india_rich)
