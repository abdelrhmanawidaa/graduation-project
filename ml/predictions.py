

def getPredictions(quantity,cho,cho0,cho1,cho2,cho3,cho4,cho5,cho6,cho7,cho8,cho9,cho11,cho12,cho13,cho14):
    import pickle
    
    model = pickle.load(open("dumbs/titanic_survival_ml_model.sav", "rb"))
    scaled = pickle.load(open("dumbs/scaler.sav", "rb"))
    prediction = model.predict(scaled.transform([[quantity,cho0,cho,cho1,cho2,cho3,cho4,cho5,cho6,cho7,cho8,cho9,cho11,cho12,cho13,cho14]]))    
 
    if prediction == 0:
        return "You don't have diabetes"
    elif prediction == 1: 
        return "You have diabetes"
    else:
        return "error"
