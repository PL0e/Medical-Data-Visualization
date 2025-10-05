# Medical Data Visualizer

A Python data analysis project that visualizes and analyzes medical examination data to explore relationships between cardiovascular disease, body measurements, blood markers, and lifestyle choices.

## Project Overview

This project is part of the freeCodeCamp Data Analysis with Python certification. It uses pandas, matplotlib, and seaborn to create visualizations from medical examination data.

## Dataset Description

The dataset contains medical examination data with the following features:

- **Age**: Patient age in days (Objective Feature)
- **Height**: Patient height in cm (Objective Feature)
- **Weight**: Patient weight in kg (Objective Feature)
- **Gender**: Categorical code (Objective Feature)
- **Systolic blood pressure** (ap_hi): Examination Feature
- **Diastolic blood pressure** (ap_lo): Examination Feature
- **Cholesterol**: 1=normal, 2=above normal, 3=well above normal
- **Glucose**: 1=normal, 2=above normal, 3=well above normal
- **Smoking**: Binary (Subjective Feature)
- **Alcohol intake**: Binary (Subjective Feature)
- **Physical activity**: Binary (Subjective Feature)
- **Cardiovascular disease**: Binary (Target Variable)

## How to Run

1. **Download the dataset**:
   \`\`\`bash
   Run the download_data.py script
   \`\`\`

2. **Generate visualizations**:
   \`\`\`bash
   Run the medical_data_visualizer.py script
   \`\`\`

3. **View results**:
   - `catplot.png`: Categorical plot showing counts of health factors by cardiovascular disease status
   - `heatmap.png`: Correlation heatmap of all features

## Features

### Data Processing
- Calculates BMI and adds an 'overweight' column
- Normalizes cholesterol and glucose values (0=good, 1=bad)
- Filters out incorrect data (invalid blood pressure, outlier heights/weights)

### Visualizations

#### Categorical Plot
Shows the distribution of health factors (cholesterol, glucose, smoking, alcohol, physical activity, overweight) split by cardiovascular disease presence.

#### Correlation Heatmap
Displays correlations between all features with the upper triangle masked for clarity.

## Technologies Used

- **pandas**: Data manipulation and analysis
- **matplotlib**: Plotting and visualization
- **seaborn**: Statistical data visualization
- **numpy**: Numerical operations

## Project Structure

\`\`\`
/scripts
  ├── download_data.py          # Downloads the medical examination dataset
  └── medical_data_visualizer.py # Main analysis and visualization script
\`\`\`

## Learning Outcomes

- Data cleaning and preprocessing
- Feature engineering (BMI calculation)
- Data normalization techniques
- Creating categorical plots with seaborn
- Generating correlation matrices and heatmaps
- Filtering outliers using percentiles
- Working with medical/health datasets
