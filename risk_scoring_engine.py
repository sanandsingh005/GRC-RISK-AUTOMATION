import pandas as pd

# Load Excel
df = pd.read_excel("C:/Users/sanan/Desktop/GRC - Automation/Day - 3/risk_register.xlsx")

def calculate_residual_risk(inherent, control):
    """
    Residual Risk = Inherent Risk * (1 - Control Effectiveness / 5)
    """
    return round(inherent * (1 - control / 5), 2)

def risk_rating(residual):
    if residual >= 3.5:
        return "High"
    elif residual >= 1.5:
        return "Medium"
    else:
        return "Low"

def process_risk(row):
    grc = str(row["GRC_Applicable"]).strip().lower()

    if grc != "yes":
        return pd.Series(["No Risk", 0, "None"])

    inherent = int(row["Inherent_Risk"])
    control = int(row["Control_Effectiveness"])

    residual = calculate_residual_risk(inherent, control)
    rating = risk_rating(residual)

    return pd.Series([residual, inherent, rating])

# Apply engine
df[["Residual_Risk", "Inherent_Risk_Score", "Risk_Rating"]] = df.apply(
    process_risk, axis=1
)

# Save output
df.to_excel("risk_register_scored.xlsx", index=False)

print("Risk scoring engine executed successfully.")