grc_applicable = input("Is GRC applicable? (Yes/No): ")
data_class = input("Data classification (Public/Restricted): ")
sensitive = input("Sensitive data involved? (Yes/No): ")

if grc_applicable != "Yes":
    risk = "No Risk"
elif data_class == "Restricted" or sensitive == "Yes":
    risk = "High Risk"
else:
    risk = "Medium Risk"

print("Calculated Risk Significance:", risk)