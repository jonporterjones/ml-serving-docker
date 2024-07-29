import pickle

import numpy as np


def load_model():
    """
    Load a previously built model from disk.x

    This module is not used anywhere in the deployment.
    Provided only to demonstrate the trained model is used.
    """

    # 0,1,2 (Setosa, Versicolour, and Virginica)
    output_classes = {
        0: "Setosa",
        1: "Versicolour",
        2: "Virginica"
    }

    model = pickle.load(open('./resources/model.pkl', mode='r+b'))

    prediction = model.predict_proba([[7.2, 3.6, 4.1, 5.0],[3.1, 2.7, 0.1, 3.0]])
    
    #Outputs will be the predicted output class and probability
    predicted_max_args = np.argmax(prediction, axis=1)
    predicted_classes = [output_classes[arg] for arg in predicted_max_args]

    predicted_probabilities = np.max(prediction, axis=1)

    for predicted_class, predicted_probability in zip(predicted_classes, predicted_probabilities):
        print(predicted_class)
        print(round(predicted_probability,2))
        print('')
        
    #return(zip(max_classes, max_predictions))
    #print(prediction) # Prints the predicted label.
    #print(model.classes_) # Prints the possible output classes.
    #print(output_classes[prediction[0]])

if __name__ =="__main__":
    load_model()