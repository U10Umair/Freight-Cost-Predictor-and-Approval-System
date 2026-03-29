# import joblib
# import pandas as pd

# # MODEL_PATH='D:\ML projects\freight_cost_prediction\models\predict_freight_model.pkl'

# MODEL_PATH = r"D:\ML projects\models\predict_freight_model.pkl"

# def load_model(model_path:str=MODEL_PATH):
#     """
#     load trained freight cost prediction model
#     """
#     with open(model_path,"rb") as f:
#         model=joblib.load(f)
#     return model
    
    
# def predict_freight_cost(input_data):
#     """
#     predict freight cost for new vendor invoices
    
#     parameters
#     ----------
#     input data: dictionary
    
#     returns
#     -------
#     pd.Dataframe with predicted freight cost
    
#     """
#     model=load_model()
#     input_df=pd.DataFrame(input_data)
#     input_df['Predicted_Freight']=model.predict(input_df).round()
    
#     return input_df

# if __name__ == "__main__":
    
#     sample_data={
#         "Dollars":[18500,9000,3000,200]
#     }
    
#     prediction=predict_freight_cost(sample_data)
#     print(prediction)


import joblib
from pathlib import Path
import pandas as pd

# Correct relative path (works both locally and on Streamlit Cloud)
def get_model_path(filename):
    return Path(__file__).parent.parent / "models" / filename

def load_model():
    model_path = get_model_path("predict_freight_model.pkl")
    
    if not model_path.exists():
        raise FileNotFoundError(f"Model not found at: {model_path}")
        
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model


def predict_freight_cost(input_data):
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df['Predicted_Freight'] = model.predict(input_df).round()
    return input_df


# For testing locally
if __name__ == "__main__":
    sample_data = {"Dollars": [18500, 9000, 3000, 200]}
    prediction = predict_freight_cost(sample_data)
    print(prediction)
    
    