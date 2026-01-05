import pandas as pd

# Load scored risk data
df = pd.read_excel("C:/Users/sanan/Desktop/GRC - Automation/Day - 4/risk_register_scored.xlsx")

# Count risk ratings
risk_counts = df["Risk_Rating"].value_counts().reset_index()
risk_counts.columns = ["Risk_Rating", "Count"]

# Calculate total risks
total_risks = risk_counts["Count"].sum()
risk_counts["Percentage"] = round((risk_counts["Count"] / total_risks) * 100, 2)

# Create executive summary
summary = pd.DataFrame({
    "Metric": [
        "Total Risks Count",
        "High Risks",
        "Medium Risks",
        "Low Risks"
    ],
    "Value": [
        total_risks,
        df[df["Risk_Rating"] == "High"].shape[0],
        df[df["Risk_Rating"] == "Medium"].shape[0],
        df[df["Risk_Rating"] == "Low"].shape[0]
    ]
})

# Export summary report
with pd.ExcelWriter("risk_summary_report.xlsx", engine="openpyxl") as writer:
    summary.to_excel(writer, sheet_name="Executive Summary", index=False)
    risk_counts.to_excel(writer, sheet_name="Risk Distribution", index=False)

print("Executive risk summary report generated successfully.")