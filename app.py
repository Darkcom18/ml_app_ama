import streamlit as st
# EDA Pkg
import pandas as pd
import os
import numpy as np
import joblib

# Storing Data
import sqlite3
import datetime


def get_value(val,my_dict):
	for key ,value in my_dict.items():
		if val == key:
			return value

# Find the Key From Dictionary
def get_key(val,my_dict):
	for key ,value in my_dict.items():
		if val == value:
			return key

# Load Models
def load_model_n_predict(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model


def main():
	""" ML App with Streamlit"""
	st.title("LeadTime Predictor")

	# Preview Dataset
	activity = ["prediction","about"]
	choice = st.sidebar.selectbox("Choose Activity",activity)

	# CHOICE FOR PREDICTION WITH ML
	if choice == 'prediction':
		st.text("Predict LeadTime")

		# Dictionary of Mapped Values
		d_source = {"J": 0, "W": 1}
		d_types= {"PTR":0, "CR":1,"Story":2, "Task":3, "Bug":4, "TR":5, "Sub-task":6, "Epic":7,"Initiative":8, "Risk":9, "IR":10, "WO":11, "CP":12, "Spike":13}

		# RECEIVE USER INPUT
		source = st.selectbox("Select Source",tuple(d_source.keys()))
		types = st.selectbox("Select Type",tuple(d_types.keys()))

	
		# USER INPUT ENDS HERE

		# GET VALUES FOR EACH INPUT
		k_source = get_value(source,d_source)
		k_types= get_value(types,d_types)


		# RESULT OF USER INPUT
		sample_data = np.array([source ,types]).reshape(-1, 1)
		st.info(sample_data)
		st.text("Using this encoding for prediction")
		st.success(sample_data)

		prettified_result = {"Source":source,
		"Types":types}
		
		st.subheader("Prettify JSON")
		st.json(prettified_result)

		# MAKING PREDICTION
		st.subheader("Prediction")

		if st.button("Predict"):
					model_predictor = load_model_n_predict("leadtime_model.pkl")
					prediction = model_predictor.predict(sample_data)
		st.success("Predicted Leadtime as :: {}".format(prediction))
	
	# ABOUT CHOICE
	if choice == 'about':
		st.subheader("About")
		st.markdown("""
			Work done by Trung
			""")



if __name__ == '__main__':
	main()
