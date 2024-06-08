import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_openml 

st.write("""
# Boston House Prediction App

This app predicts the **Boston House Price**!
""")

st.write('---')

boston = fetch_openml(name='boston', version=1, parser='auto')

X = pd.DataFrame(boston.data, columns=boston.feature_names)
Y = pd.DataFrame(boston.target, columns=["MEDV"])

# Reshape Y to a 1-dimensional array
Y = Y.values.ravel()

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    features = {}
    for feature_name in X.columns:
        # Check if the feature is numerical
        if pd.api.types.is_numeric_dtype(X[feature_name]):
            features[feature_name] = st.sidebar.slider(feature_name, X[feature_name].min(), X[feature_name].max(), X[feature_name].mean())
        else:
            st.sidebar.write(f"Skipping {feature_name} as it's not numeric.")
    return pd.DataFrame(features, index=[0])

df = user_input_features()

# Main Panel

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

# Select only numeric features for model training
selected_features = df.columns.intersection(X.columns)
X_selected = X[selected_features]

# Build Regression Model
model = RandomForestRegressor()
model.fit(X_selected, Y)
# Apply Model to Make Prediction
prediction = model.predict(df[selected_features])

st.header('Prediction of MEDV')
st.write(prediction)
st.write('---')