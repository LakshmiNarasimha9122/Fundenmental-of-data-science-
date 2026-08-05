import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

OUTPUT = Path("outputs")
OUTPUT.mkdir(exist_ok=True)

# ---------------------------------------------------------
# Common EDA function
# ---------------------------------------------------------
def perform_eda(name, df, target, categorical_cols=None):
    print("\n" + "=" * 70)
    print(name.upper())
    print("=" * 70)

    print("\n1. Dataset shape:")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    print("\n2. Data types:")
    print(df.dtypes)

    print("\n3. Missing values:")
    print(df.isnull().sum())

    print("\n4. Duplicate rows:")
    print(df.duplicated().sum())

    numeric = df.select_dtypes(include="number")

    print("\n5. Statistical summary:")
    summary = numeric.agg(["mean", "median", "min", "max", "std"]).T
    print(summary.round(2))
    summary.to_csv(OUTPUT / f"{name}_statistics.csv")

    # Remove duplicate rows if present
    df = df.drop_duplicates().copy()

    # ---------------- Charts ----------------
    # Histograms for numeric columns
    numeric.hist(figsize=(12, 8), bins=8)
    plt.suptitle(f"{name} - Numeric Histograms")
    plt.tight_layout()
    plt.savefig(OUTPUT / f"{name}_histograms.png", dpi=150)
    plt.close()

    # Box plots for numeric columns
    plt.figure(figsize=(12, 6))
    numeric.boxplot()
    plt.title(f"{name} - Box Plot")
    plt.xticks(rotation=30)
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig(OUTPUT / f"{name}_boxplot.png", dpi=150)
    plt.close()

    # Categorical bar chart
    if categorical_cols:
        for col in categorical_cols:
            plt.figure(figsize=(7, 5))
            df[col].value_counts().plot(kind="bar")
            plt.title(f"{name} - {col} Distribution")
            plt.xlabel(col)
            plt.ylabel("Count")
            plt.xticks(rotation=20)
            plt.tight_layout()
            plt.savefig(OUTPUT / f"{name}_{col}_bar.png", dpi=150)
            plt.close()

    # Scatter plots: every numeric feature against target
    if target in numeric.columns:
        for col in numeric.columns:
            if col != target:
                plt.figure(figsize=(7, 5))
                plt.scatter(df[col], df[target])
                plt.xlabel(col)
                plt.ylabel(target)
                plt.title(f"{name} - {col} vs {target}")
                plt.grid(True, alpha=0.3)
                plt.tight_layout()
                plt.savefig(OUTPUT / f"{name}_{col}_vs_{target}.png", dpi=150)
                plt.close()

    # Correlation matrix
    corr = numeric.corr()
    corr.to_csv(OUTPUT / f"{name}_correlation.csv")

    plt.figure(figsize=(8, 6))
    plt.imshow(corr, cmap="coolwarm", aspect="auto")
    plt.colorbar(label="Correlation")
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.title(f"{name} - Correlation Matrix")
    plt.tight_layout()
    plt.savefig(OUTPUT / f"{name}_correlation.png", dpi=150)
    plt.close()

    print("\nCorrelation with target:")
    print(corr[target].sort_values(ascending=False).round(3))

    print("\nEDA completed. Files saved in:", OUTPUT.resolve())


# ---------------------------------------------------------
# 1. Education Analytics
# ---------------------------------------------------------
education = pd.DataFrame({
    "Student_ID": ["S01","S02","S03","S04","S05","S06","S07","S08","S09","S10",
                   "S11","S12","S13","S14","S15","S16","S17","S18","S19","S20"],
    "Attendance": [92,55,78,60,88,47,95,72,50,83,66,90,58,76,62,85,45,80,68,53],
    "Study_Hours": [5,2,4,3,5,1,6,3,2,4,3,5,2,4,3,5,1,4,3,2],
    "Internal_Marks": [45,24,38,28,42,20,48,35,22,40,30,44,25,36,29,41,18,39,32,23],
    "Result": ["Pass","Fail","Pass","Fail","Pass","Fail","Pass","Pass","Fail","Pass",
               "Fail","Pass","Fail","Pass","Fail","Pass","Fail","Pass","Pass","Fail"]
})

perform_eda(
    "education",
    education,
    "Internal_Marks",
    ["Result"]
)

# ---------------------------------------------------------
# 2. Healthcare Analytics
# ---------------------------------------------------------
healthcare = pd.DataFrame({
    "Patient_ID": ["P01","P02","P03","P04","P05","P06","P07","P08","P09","P10",
                   "P11","P12","P13","P14","P15","P16","P17","P18","P19","P20"],
    "Age": [45,32,55,28,60,40,52,35,48,30,62,38,50,27,58,42,46,34,53,29],
    "Sugar_Level": [145,98,180,90,200,120,165,105,155,95,210,115,170,88,190,130,150,100,175,92],
    "BP": [130,118,145,110,150,125,140,120,135,115,155,122,142,108,148,128,132,116,144,112],
    "BMI": [28,23,31,22,34,26,30,24,29,23,35,25,30,21,33,27,28,24,31,22],
    "Disease_Status": ["Yes","No","Yes","No","Yes","No","Yes","No","Yes","No",
                       "Yes","No","Yes","No","Yes","No","Yes","No","Yes","No"]
})

perform_eda(
    "healthcare",
    healthcare,
    "Sugar_Level",
    ["Disease_Status"]
)

# ---------------------------------------------------------
# 3. Retail Sales
# ---------------------------------------------------------
retail = pd.DataFrame({
    "Product_ID": ["PR01","PR02","PR03","PR04","PR05","PR06","PR07","PR08","PR09","PR10",
                   "PR11","PR12","PR13","PR14","PR15","PR16","PR17","PR18","PR19","PR20"],
    "Category": ["Grocery","Snacks","Dairy","Fruits","Vegetables","Grocery","Snacks","Dairy",
                 "Fruits","Vegetables","Grocery","Snacks","Dairy","Fruits","Vegetables",
                 "Grocery","Snacks","Dairy","Fruits","Vegetables"],
    "Price": [50,30,45,60,40,80,25,55,70,35,90,20,65,75,45,100,35,50,80,30],
    "Quantity_Sold": [20,35,18,25,30,15,40,16,22,28,12,45,14,20,26,10,32,19,18,35],
    "Discount": [5,3,2,5,4,6,3,2,5,4,6,2,3,5,4,7,3,2,6,3],
    "Revenue": [1000,1050,810,1500,1200,1200,1000,880,1540,980,1080,900,910,1500,1170,1000,1120,950,1440,1050]
})

perform_eda(
    "retail",
    retail,
    "Revenue",
    ["Category"]
)

# ---------------------------------------------------------
# 4. Banking Loan Approval
# ---------------------------------------------------------
banking = pd.DataFrame({
    "Customer_ID": ["C01","C02","C03","C04","C05","C06","C07","C08","C09","C10",
                    "C11","C12","C13","C14","C15","C16","C17","C18","C19","C20"],
    "Income": [45000,25000,60000,22000,50000,30000,70000,28000,55000,24000,
               65000,35000,48000,26000,75000,32000,52000,27000,68000,23000],
    "Credit_Score": [720,580,750,560,710,600,780,590,730,570,760,620,700,585,790,610,725,575,770,555],
    "Loan_Amount": [200000,150000,300000,120000,250000,180000,350000,160000,270000,130000,
                    320000,200000,240000,140000,400000,190000,260000,150000,330000,125000],
    "Employment_Type": ["Salaried","Self-employed","Salaried","Unemployed","Salaried","Self-employed",
                        "Salaried","Self-employed","Salaried","Unemployed","Salaried","Self-employed",
                        "Salaried","Unemployed","Salaried","Self-employed","Salaried","Self-employed",
                        "Salaried","Unemployed"],
    "Loan_Status": ["Approved","Rejected","Approved","Rejected","Approved","Rejected","Approved","Rejected",
                    "Approved","Rejected","Approved","Rejected","Approved","Rejected","Approved","Rejected",
                    "Approved","Rejected","Approved","Rejected"]
})

perform_eda(
    "banking",
    banking,
    "Credit_Score",
    ["Employment_Type", "Loan_Status"]
)

# ---------------------------------------------------------
# 5. Agriculture Crop Yield
# ---------------------------------------------------------
agriculture = pd.DataFrame({
    "Farm_ID": ["F01","F02","F03","F04","F05","F06","F07","F08","F09","F10",
                "F11","F12","F13","F14","F15","F16","F17","F18","F19","F20"],
    "Rainfall_mm": [850,600,900,500,780,650,920,720,550,800,880,620,760,940,580,820,700,960,540,790],
    "Temperature": [28,32,27,34,29,31,26,30,33,28,27,32,29,26,33,28,30,25,34,29],
    "Fertilizer_kg": [60,45,65,40,55,48,70,52,42,58,62,46,54,72,44,60,50,75,41,56],
    "Soil_Type": ["Loamy","Sandy","Loamy","Sandy","Clay","Sandy","Loamy","Clay","Sandy","Loamy",
                  "Loamy","Sandy","Clay","Loamy","Sandy","Clay","Clay","Loamy","Sandy","Clay"],
    "Crop_Yield_kg": [3200,2100,3500,1800,3000,2300,3700,2800,1900,3100,3400,2200,2950,3800,2000,3150,2700,3900,1850,3050]
})

perform_eda(
    "agriculture",
    agriculture,
    "Crop_Yield_kg",
    ["Soil_Type"]
)

print("\nALL FIVE DATASETS COMPLETED SUCCESSFULLY.")
