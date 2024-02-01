from transformers import pipeline

# Text Sentiment Analysis Application
# This app is a pre-treined machine learning model to text sentiment analysis

# Load the basilene model to sentiment classification

model = pipeline("sentiment-analysis")

# Classifier a input text and return the classificantion and score

def prediction(text):
    """Classifier a input text and return the classificantion and score

    Args:
        text (str): A text to be classified
    """
    
    pred = model([text])
    
    return [pred[0]["label"], pred[0]["score"]]

if __name__=="__main__":
    print(prediction("I am a very good man. I am so happy."))
    