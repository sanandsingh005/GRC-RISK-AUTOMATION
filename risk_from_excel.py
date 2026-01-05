import os
print("Running from:", os.getcwd())


import pandas as pd

# Load Excel file
df = pd.read_excel(r"C:\Users\sanan\Desktop\GRC - Automation\risk_register.xlsx",engine="openpyxl")

def calculate_risk(row):
    grc = str(row.get("GRC_Applicable", "")).strip().lower()
    data_class = str(row.get("Data_Classification", "")).strip().lower()
    sensitive = str(row.get("Sensitive_Data", "")).strip().lower()

    if grc != "yes":
        return "No Risk"
    elif data_class == "restricted" or sensitive == "yes":
        return "High Risk"
    else:
        return "Medium Risk"

# Apply risk logic
df["Risk_Significance"] = df.apply(calculate_risk, axis=1)

# Save updated Excel
output_file = "risk_register_with_risk.xlsx"
df.to_excel(output_file, index=False)
print(f"File created: {output_file}")


print(" Risk significance calculation completed successfully.")

