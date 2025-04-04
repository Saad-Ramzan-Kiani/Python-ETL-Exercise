import pandas as pd
import numpy as np
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
api = response.json()

api_data = []
for user in api:
    print(user["name"])
    print(user["email"])
    print(user["company"]["name"])
    
    api_data.append({
        "Name": user["name"],
        "Email": user["email"],
        "Company": user["company"]["name"]
    })


api_df = pd.DataFrame(api_data)
api_df.to_csv("api_users.csv", index=False)
print("API data saved to 'api_users.csv'.")


df = pd.read_csv('data.csv')

df_cleaned = df.drop_duplicates()

df['Salary_After_Tax'] = df['Salary'] * 0.9

df['Salary'].fillna(df['Salary'].median(), inplace=True)

df.to_csv('updated_employees.csv', index=False)
print("New column added and missing salaries filled!")

df_cleaned.to_csv('data_cleaned.csv', index=False)
print("Cleaned data saved to 'data_cleaned.csv'.")
