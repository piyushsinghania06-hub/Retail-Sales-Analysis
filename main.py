from src.data_cleaning import clean_data
from src.visualization import sales_visualization
from src.prediction_model import sales_prediction

# Load and clean data
df = clean_data()

# Visualizations
sales_visualization(df)

# Prediction
sales_prediction(df)
