import streamlit as st
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load your trained model
MODEL_PATH = os.path.join('/content/drive/MyDrive/save', 'plant.h5')
model = load_model(MODEL_PATH)

def model_predict(img_path, model):
    st.write(img_path)
    img = image.load_img(img_path, target_size=(256, 256))

    # Preprocessing the image
    x = image.img_to_array(img)
    x = x / 255.0
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    preds = np.argmax(preds, axis=1)

    class_labels = [
        "Tomato | Bacterial spot",
        "Tomato | Early blight",
        "Tomato | Late blight",
        "Tomato | Leaf Mold",
        "Tomato | Septoria leaf spot",
        "Tomato | Spider mites Two spotted spider mite",
        "Tomato | Target Spot",
        "Tomato | Yellow Leaf Curl Virus",
        "Tomato | Mosaic Virus",
        "Tomato | Healthy"
    ]

    additional_info = [
        {
            "cause": "Bacterial spot is caused by the bacterium Pseudomonas syringae pv. tomato. This pathogen is seedborne and can overwinter in crop residue in temper.",
            "pesticide": "Copper products or copper plus mancozeb",
        },
        {
            "cause": "Early blight is caused by the fungus Alternaria solani. The disease primarily affects leaves and fruit.",
            "pesticide": "Fungicides such as chlorothalonil, mancozeb, or copper-based fungicides",
        },
        {
            "cause": "Late blight is caused by the oomycete Phytophthora infestans. It can rapidly affect tomato plants in wet conditions.",
            "pesticide": "Fungicides like chlorothalonil, mancozeb, or mefenoxam",
        },
        {
            "cause": "Leaf Mold is caused by the fungus Fulvia fulva. It affects primarily the foliage of tomato plants.",
            "pesticide": "Copper-based fungicides",
        },
        {
            "cause": "Septoria leaf spot is caused by the fungus Septoria lycopersici. It affects leaves, leading to small, dark spots with a lighter center.",
            "pesticide": "Fungicides containing chlorothalonil or copper",
        },
        {
            "cause": "Spider mites Two-spotted spider mite damage is caused by Tetranychus urticae. They feed on plant cells, causing stippling and discoloration.",
            "pesticide": "Miticides like abamectin or insecticidal soap",
        },
        {
            "cause": "Target Spot is caused by the fungus Corynespora cassiicola. It leads to circular lesions on leaves.",
            "pesticide": "Fungicides like chlorothalonil",
        },
        {
            "cause": "Yellow Leaf Curl Virus is caused by begomoviruses transmitted by whiteflies. It leads to leaf curling and yellowing.",
            "pesticide": "Insecticides like neonicotinoids and cultural practices to control whiteflies",
        },
        {
            "cause": "Mosaic Virus is caused by various viruses, including Tomato mosaic virus. It results in mottled or mosaic-like patterns on leaves.",
            "pesticide": "There is no specific pesticide for viruses; focus on controlling aphids and whiteflies",
        },
        {
            "cause": "Healthy plant with no significant diseases.",
            "pesticide": "Not applicable for healthy plants",
        },
    ]

    result_label = class_labels[preds[0]]
    result_cause = additional_info[preds[0]]["cause"]
    result_pesticide = additional_info[preds[0]]["pesticide"]

    st.write(f"Prediction: {result_label}")
    st.write(f"Cause: {result_cause}")
    st.write(f"Pesticide: {result_pesticide}")

def main():
    st.title("Plant Disease Prediction")
    uploaded_file = st.file_uploader("Choose a plant image...", type="jpg")

    if uploaded_file is not None:
        # Save the file
        with open("uploaded_image.jpg", "wb") as f:
            f.write(uploaded_file.getvalue())

        # Make prediction
        model_predict("uploaded_image.jpg", model)

if __name__ == '__main__':
    main()