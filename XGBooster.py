import csv
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
from xgboost import XGBRegressor
import matplotlib.pyplot as plt

subjects_df = pd.DataFrame()
targets_df = pd.DataFrame(columns=["Hemoglobin(g/L)"])
metadata_df = pd.DataFrame(columns=["id", "Age", "Height(cm)", "Weight(kg)", "Gender"])
wavelengths = ["660nm", "730nm", "850nm", "940nm"]
with open("Subjects information.csv") as info_file:
    reader = csv.reader(info_file)
    z = 0
    for row in reader:
        if z > 0:
            target = {}
            subjects_info = {}
            subjects_info["id"] = float(row[0])
            subjects_info["Age"] = float(row[2])
            subjects_info["Height(cm)"] = float(row[3])
            subjects_info["Weight(kg)"] = float(row[4])
            if row[5] == "male":
                subjects_info["Gender"] = 1.0
            else:
                subjects_info["Gender"] = 0.0
                
            target["Hemoglobin(g/L)"] = float(row[1])
            targets_df = pd.concat([targets_df, pd.DataFrame([target])], ignore_index=True)
            metadata_df = pd.concat([metadata_df, pd.DataFrame([subjects_info])], ignore_index=True)
            
            
        z += 1

for i in range(58):
    subject = {}
    for w in wavelengths:
        path = f"{w}_features/{i+1}/Biomarker_stats/"
        files = [f"{i + 1}_derivs_ratios_btwn_0-11999.csv", f"{i + 1}_ppg_derivs_btwn_0-11999.csv", f"{i + 1}_ppg_sig_btwn_0-11999.csv", f"{i + 1}_sig_ratios_btwn_0-11999.csv"]
        for file in files:
            with open(path + file) as csvfile:
                reader = csv.reader(csvfile)
                k = 0
                feature_names = []
                feature_values = []
                for row in reader:
                    if k == 0:
                        feature_names = row
                    elif k == 1:
                        feature_values = row
                    elif k > 1:
                        break
                    k += 1
                
                for j in range(1, len(feature_names)):
                    subject[f"{w}_{feature_names[j]}"] = float(feature_values[j])

    subjects_df = pd.concat([subjects_df, pd.DataFrame([subject])], ignore_index=True)

subjects_df = pd.concat([metadata_df, subjects_df], axis=1)

print("NaNs in subjects_df:", subjects_df.isna().sum().sum())
print("NaNs in targets_df:", targets_df.isna().sum().sum())


# 1. Feature selection using f_regression (for continuous target)
selector = SelectKBest(score_func=f_regression, k=30)
subjects_selected = selector.fit_transform(subjects_df, targets_df.values.ravel())

# Get the names of selected features
selected_features = subjects_df.columns[selector.get_support()]
print("Selected features:\n", selected_features)

# 2. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    subjects_selected, targets_df.values.ravel(), test_size=0.3, random_state=41
)

# 3. Train XGBoost Regressor
model = XGBRegressor(random_state=42)
model.fit(X_train, y_train)

# 4. Predict and evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"\nR² score: {r2:.4f}")
print(f"MAE: {mae:.4f}")

# 6. Regression Plot (Predicted vs True values)
plt.figure(figsize=(8, 8))
plt.plot(y_test, y_pred, 'o')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')  # Identity line
plt.text(min(y_test), max(y_test), f'$R^2$ = {r2:.3f}', fontsize=10, color='red')
plt.xlabel("Actual Hemoglobin Values (g/L)")
plt.ylabel("Predicted Hemoglobin Values (g/L)")
plt.title("Predicted vs Actual Hemoglobin Values")
plt.legend()
plt.grid(True)
plt.show()

# 7. Bland-Altman Plot
# Calculate the differences and averages
differences = y_pred - y_test
averages = (y_pred + y_test) / 2

# Calculate the mean and limits of agreement (1.96 * std)
mean_diff = np.mean(differences)
std_diff = np.std(differences)
loa_upper = mean_diff + 1.96 * std_diff
loa_lower = mean_diff - 1.96 * std_diff

# Create Bland-Altman Plot
plt.figure(figsize=(8, 8))
plt.scatter(averages, differences, alpha=0.5)
plt.axhline(mean_diff, color='grey', linestyle='--', label='Mean Difference')
plt.axhline(loa_upper, color='red', linestyle='--', label='Upper Limit of Agreement')
plt.axhline(loa_lower, color='blue', linestyle='--', label='Lower Limit of Agreement')
plt.title('Bland-Altman Plot: Hemoglobin Prediction')
plt.xlabel('Mean of Actual and Predicted (g/L)')
plt.ylabel('Difference (Predicted - Actual) (g/L)')
plt.legend()
plt.grid(True)
plt.show()