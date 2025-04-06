import pandas as pd
import numpy as np
import requests
import os

os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)


response = requests.get("https://jsonplaceholder.typicode.com/users")
api_data = response.json()

flattened_data = []

for user in api_data:
    flattened_data.append({
        "ID": user["id"],
        "Name": user["name"],
        "Username": user["username"],
        "Email": user["email"],
        "Street": user["address"]["street"],
        "Suite": user["address"]["suite"],
        "City": user["address"]["city"],
        "Zipcode": user["address"]["zipcode"],
        "Latitude": user["address"]["geo"]["lat"],
        "Longitude": user["address"]["geo"]["lng"],
        "Phone": user["phone"],
        "Website": user["website"],
        "Company_Name": user["company"]["name"],
        "Company_CatchPhrase": user["company"]["catchPhrase"],
        "Company_BS": user["company"]["bs"]
    })

df = pd.DataFrame(flattened_data)
df.to_csv("input/api_data.csv", index=False)
print("Full API data saved to 'api_full_users.csv'.")

company_info = []

for user in api_data:
    company_info.append({
        "Name": user["name"],
        "Company_Name": user["company"]["name"]
    })

df_company = pd.DataFrame(company_info)
df_company.to_csv("output/User_company_name.csv", index=False)
print("Company info saved to 'User_company_name.csv'.")

df = pd.read_csv("input/data.csv")

df_cleaned = df.drop_duplicates()

df['Salary_After_Tax'] = df['Salary'] * 0.9

df['Salary'].fillna(df['Salary'].median(), inplace=True)

df.to_csv('output/updated_employees.csv', index=False)
print("New column added and missing salaries filled!")

df_cleaned.to_csv('output/data_cleaned.csv', index=False)
print("Cleaned data saved to 'data_cleaned.csv'.")

df.to_json("output/employees_data.json", orient="records", indent=4)
print("CSV data converted and saved to 'employees_data.json'.")

