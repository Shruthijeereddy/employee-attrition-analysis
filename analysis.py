import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("STEP 1: Loading dataset...")

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

print("Dataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

# Visualization style
sns.set(style="whitegrid")

# -------------------------------
# Chart 1: Attrition Distribution
# -------------------------------
print("STEP 2: Showing Attrition Distribution")

plt.figure(figsize=(6,4))
sns.countplot(x="Attrition", data=df)
plt.title("Employee Attrition Distribution")
plt.show()

# -------------------------------
# Chart 2: Attrition by Department
# -------------------------------
print("STEP 3: Showing Department Analysis")

plt.figure(figsize=(8,5))
sns.countplot(x="Department", hue="Attrition", data=df)
plt.title("Attrition by Department")
plt.xticks(rotation=30)
plt.show()

# -------------------------------
# Chart 3: Monthly Income
# -------------------------------
print("STEP 4: Showing Income Distribution")

plt.figure(figsize=(7,4))
sns.histplot(df["MonthlyIncome"], bins=30, kde=True)
plt.title("Monthly Income Distribution")
plt.show()

# -------------------------------
# Chart 4: Job Satisfaction
# -------------------------------
print("STEP 5: Showing Job Satisfaction Analysis")

plt.figure(figsize=(6,4))
sns.boxplot(x="Attrition", y="JobSatisfaction", data=df)
plt.title("Job Satisfaction vs Attrition")
plt.show()

# -------------------------------
# Chart 5: Job Role Attrition
# -------------------------------
print("STEP 6: Showing Job Role Analysis")

plt.figure(figsize=(10,5))
sns.countplot(y="JobRole", hue="Attrition", data=df)
plt.title("Attrition by Job Role")
plt.show()

# -------------------------------
# Chart 6: Correlation Heatmap
# -------------------------------
print("STEP 7: Showing Correlation Heatmap")

numeric_df = df.select_dtypes(include=['int64','float64'])

plt.figure(figsize=(10,6))
sns.heatmap(numeric_df.corr(), cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

# -------------------------------
# Business Insights
# -------------------------------
print("STEP 8: Calculating Business Insights")

attrition_rate = (df["Attrition"] == "Yes").mean() * 100
avg_income = df["MonthlyIncome"].mean()
avg_years = df["YearsAtCompany"].mean()

print("\n--- BUSINESS INSIGHTS ---")
print(f"Attrition Rate: {attrition_rate:.2f}%")
print(f"Average Monthly Income: {avg_income:.2f}")
print(f"Average Years at Company: {avg_years:.2f}")

print("ANALYSIS COMPLETED SUCCESSFULLY ✅")