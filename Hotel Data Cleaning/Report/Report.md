# Data Cleaning Report: Hotel Booking Demand Dataset

---

## 📌 Executive Summary

The Hotel Booking Demand dataset consists of 119,390 records and 32 columns collected from July 2015 to August 2017. The dataset contains detailed information on hotel bookings including reservation status, customer demographics, booking channels, and more.

The objective of this task was to clean the dataset to make it analysis-ready by identifying and addressing missing values, duplicates, outliers, inconsistencies, and data integrity issues. Key cleaning actions included:
- Handling missing values in `children`, `agent`, `company`, and `country` columns
- Removing duplicate records
- Treating outliers in key numerical columns
- Resolving data inconsistencies (e.g., total guests = 0)

---

## 📊 Data Quality Assessment

### Dataset Overview:
- **Initial Rows**: 119,390
- **Columns**: 32
- **Data Types**: Mixed (numerical, categorical, datetime)

### Identified Issues:
| Issue Type               | Affected Columns                        | Severity |
|--------------------------|------------------------------------------|----------|
| Missing Values           | `children`, `agent`, `company`, `country` | Moderate |
| Duplicates               | ~100+ duplicate rows                     | Moderate |
| Outliers                 | `lead_time`, `adr`                       | High     |
| Inconsistent Values      | `adults`, `children`, `babies` = 0      | High     |

---

## 🧹 Cleaning Methodology

### 1. Handling Missing Values:
| Column     | Strategy Used                                      |
|------------|----------------------------------------------------|
| `children` | Replaced NaN with 0 (assume no children)           |
| `agent`    | Replaced NaN with 0 (no agent)                     |
| `company`  | Replaced NaN with 0 (no company)                   |
| `country`  | Filled with mode value (or 'Unknown' if applicable)|

### 2. Duplicate Removal:
- Found **`100+`** duplicate rows using `df.duplicated()`
- Removed using `df.drop_duplicates()`

### 3. Outlier Treatment:
- Focused columns: `lead_time`, `adr`, `adults`, `babies`
- Applied **IQR method** and visualized with boxplots
- Removed/capped extreme values based on domain logic

### 4. Data Inconsistency Fixes:
- Removed records where total guests (`adults + children + babies`) == 0
- Standardized country codes (where inconsistencies found)
- Ensured logical consistency in stay durations

---

## 📈 Results and Impact

### Before Cleaning:
- **119,390** rows
- Missing values in 4 columns
- Duplicates: ~100+
- Outliers in lead time & ADR (ADR > 5000, lead_time > 500)

### After Cleaning:
- **~118,500** rows
- Missing values handled
- No duplicate records
- Outliers treated
- All rows pass guest count and consistency checks

---

## ✅ Recommendations

### For Future Data Collection:
- Enforce validation rules at data entry (e.g., total guests > 0)
- Standardize country code formats at the source
- Ensure agents and companies are logged consistently

### For Ongoing Maintenance:
- Implement periodic data audits
- Create automated data cleaning scripts for incoming data
- Track and log data quality metrics over time

---

