import pandas as pd

# Sample dataset as described:
data = {
    'age': [39, 50, 38, 53, 28],
    'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 'Private'],
    'fnlwgt': [77516, 83311, 215646, 234721, 338409],
    'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors'],
    'education-num': [13, 13, 9, 7, 13],
    'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-civ-spouse', 'Married-civ-spouse'],
    'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners', 'Prof-specialty'],
    'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Wife'],
    'race': ['White', 'White', 'White', 'Black', 'Black'],
    'sex': ['Male', 'Male', 'Male', 'Male', 'Female'],
    'capital-gain': [2174, 0, 0, 0, 0],
    'capital-loss': [0, 0, 0, 0, 0],
    'hours-per-week': [40, 13, 40, 40, 40],
    'native-country': ['United-States', 'United-States', 'United-States', 'United-States', 'Cuba'],
    'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K']
}

df = pd.DataFrame(data)

# 1. How many people of each race are represented in this dataset?
race_count = df['race'].value_counts()
print(race_count)

# 2. What is the average age of men?
average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
print(average_age_men)

# 3. What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
print(percentage_bachelors)

# 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
percentage_advanced_education_high_income = round((advanced_education & (df['salary'] == '>50K')).mean() * 100, 1)
print(percentage_advanced_education_high_income)

# 5. What percentage of people without advanced education make more than 50K?
no_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
percentage_no_advanced_education_high_income = round((no_advanced_education & (df['salary'] == '>50K')).mean() * 100, 1)
print(percentage_no_advanced_education_high_income)

# 6. What is the minimum number of hours a person works per week?
min_hours = df['hours-per-week'].min()
print(min_hours)

# 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_high_income = df[df['hours-per-week'] == min_hours]
percentage_min_hours_high_income = round((min_hours_high_income['salary'] == '>50K').mean() * 100, 1)
print(percentage_min_hours_high_income)

# 8. What country has the highest percentage of people that earn >50K and what is that percentage?
country_high_income_percentage = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100
country_high_income_percentage = (country_high_income_percentage.idxmax(), round(country_high_income_percentage.max(), 1))
print(country_high_income_percentage)

# 9. Identify the most popular occupation for those who earn >50K in India.
india_high_income_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]
print(india_high_income_occupation)
