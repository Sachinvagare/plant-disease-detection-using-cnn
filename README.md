# plant-disease-detection-using-cnn
1. Train the Model in Google Colab:
   Upload your dataset to Google Colab or mount Google Drive if your data is stored there.
   Write and execute the code in the Colab notebook to train your CNN model.
   
2. Save the Model:
After training your model, save it so that you can load it later for deployment.

  python code:
  model.save("plant_disease_model.h5")  

 3. Create the Streamlit App in Google Colab:
 Create a new Colab notebook and write the Streamlit app code in a code cell. Make sure to install Streamlit in the Colab 
 environment using the following command:

  python code:
  !pip install streamlit 

 Write the Streamlit app code in a cell in your Colab notebook, and use the !streamlit run command to run the app directly 
 from Colab. However, keep in mind that Streamlit is primarily designed for local development and may not work seamlessly 
 within a Colab notebook.

 4.# Streamlit app code

  !streamlit run app.py

5. Download and Run Locally:
 Colab might not be the ideal platform for running Streamlit apps due to its architecture, and the interactive nature of 
 Streamlit might not work as expected within Colab. Therefore, it's often recommended to download the Streamlit app file 
 (app.py) and run it locally on your machine.

6. Deployment to a Web Server:
 For a more scalable deployment, consider deploying your Streamlit app to a web server. You can use platforms like Heroku, 
 AWS, or Google Cloud Platform for this purpose. Streamlit Sharing is another option provided by Streamlit for deploying 
 apps easily.

 
