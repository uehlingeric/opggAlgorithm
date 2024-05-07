import pandas as pd
import numpy as np
import keras
import joblib

def load_assets(preprocessor_path, model_path):
    """
    Load the preprocessor and model from disk.
    """
    # Load the preprocessor
    preprocessor = joblib.load(preprocessor_path)
    
    # Load the model
    model = keras.models.load_model(model_path)
    
    return preprocessor, model

def make_predictions(data, preprocessor, model):
    """
    Make predictions on the input data using the loaded preprocessor and model.
    
    Parameters:
        data (pd.DataFrame): Input data for which predictions are to be made.
        preprocessor (ColumnTransformer): Preprocessor loaded from disk.
        model (tensorflow.keras.Model): Model loaded from disk.
        
    Returns:
        np.array: Predictions generated by the model.
    """
    # Apply preprocessing
    processed_data = preprocessor.transform(data)
    
    game_length = processed_data[:, 0:1]  # first column: game length
    performance_features = processed_data[:, 1:]  # rest of the columns: performance features

    # Make predictions using the model with multiple inputs
    predictions = model.predict([game_length, performance_features])
    
    return predictions