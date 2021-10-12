import streamlit as st
import pandas as pd
import joblib
import os
import numpy as np

attrib_info = """
### Attribute Information:
	Age: 20-65
	Sex: 1. Male, 2.Female
	Polyuria: 1.Yes, 2.No.
	Polydipsia: 1.Yes, 2.No.
	Sudden weight loss: 1.Yes, 2.No.
	Weakness: 1.Yes, 2.No.
	Polyphagia: 1.Yes, 2.No.
	Genital thrush: 1.Yes, 2.No.
	visual blurring: 1.Yes, 2.No.
	Itching: 1.Yes, 2.No.
	Irritability: 1.Yes, 2.No.
	Delayed healing: 1.Yes, 2.No.
	Partial paresis: 1.Yes, 2.No.
	Muscle stiffness: 1.Yes, 2.No.
	Alopecia: 1.Yes, 2.No.
	Obesity: 1.Yes, 2.No.
	Class: 1.Positive, 2.Negative.
				
	"""


		##Load ML Models
@st.cache(allow_output_mutation=True)
def load_model(model_file):
	loaded_model = joblib.load(os.path.join(model_file),'rb',allow_pickle=True)
	return loaded_model		

label_dict = {'No':0,"Yes":1}
gender_map = {'Female':0,'Male':1}
target_label_map ={'Negative':0,'Positive':1}

def get_fvalue(val):
	feature_dict = {'No':0,'Yes':1}
	for key,value in feature_dict.items():
		if val == key:
			return value  ## value and val, both are different 
		
def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value

		

##Load ML Pkgs
def run_ml_app():
	st.subheader("Model Prediction")
	

	df = pd.read_csv('data/diabetes_data_upload.csv')		
	#st.dataframe(df)

	#with st.beta_expander("Attributes Info"):
	#	st.markdown(attrib_info)

	## Layout
	col1, col2 = st.beta_columns(2)

	with col1:
		age = st.number_input("Age",10,100)
		#gender = st.radio("Gender",["Female","Male"])
		polyuria = st.radio("Polyuria",["No","Yes"])
		st.write("An abnormally large production  of urine (greater than 2.5L - 3L over 24 hours in adults)")
		sudden_weight_loss = st.radio("Sudden weight loss",["No","Yes"])
		visual_blurring = st.radio("Visual Blurring",["No","Yes"])
		itching = st.radio("Itching",["No","Yes"]) 
		irritability = st.radio("Irritability",["No","Yes"]) 
		delayed_healing = st.radio("Delayed healing",["No","Yes"]) 
		polyphagia = st.radio("Polyphagia",["No","Yes"]) 
		st.write("Condition of excessive hunger")
		st.write("                           ")
		st.write("                           ")
		st.write("                           ")
		st.write("                           ")
		st.write("                           ")

	with col2:
		polydipsia = st.radio("Polydipsia",["No","Yes"]) 
		st.write("Feeling of extreme thirstiness") 
		weakness = st.radio("Weakness",["No","Yes"]) 
		genital_thrush = st.radio("Genital thrush",["No","Yes"])
		st.write("A kind of yeast infection causing itching, soreness in genital area and genital discharge")
		partial_paresis = st.radio("Partial paresis",["No","Yes"])
		st.write("Weakening of muscles with reduced ability to move")
		muscle_stiffness = st.radio("Muscle stiffness",["No","Yes"]) 
		alopecia = st.radio("Alopecia",["No","Yes"]) 
		st.write("An autoimmune disorder leading to unpredictable hairloss")
		obesity = st.radio("Obesity",["No","Yes"])
			
	


	if st.button('Submit your choices'):		
		st.write("")
		st.write("")
		with st.beta_expander("Your Selected Options"):
			result = {'age':age,
			#'gender':gender,
			'polyuria':polyuria,
			'polydipsia':polydipsia,
			'sudden_weight_loss':sudden_weight_loss,
			'weakness':weakness,
			'polyphagia':polyphagia,
			'genital_thrush':genital_thrush,
			'visual_blurring':visual_blurring,
			'itching':itching,
			'irritability':irritability,
			'delayed_healing':delayed_healing,
			'partial_paresis':partial_paresis,
			'muscle_stiffness':muscle_stiffness,
			'alopecia':alopecia,
			'obesity':obesity
			}

			st.write(result)
			st.write("                           ")
			st.write("                           ")

			encoded_result = []			

			for i in result.values():
				if type(i) == int:
					encoded_result.append(i)
				elif i in ["Female","Male"]:
					res = get_value(i,gender_map)
					encoded_result.append(res)
				else:
					encoded_result.append(get_fvalue(i))	


			#st.write(encoded_result)


		with st.beta_expander("Prediction Result"):
			single_sample = np.array(encoded_result).reshape(1,-1)
			#st.write(single_sample)

			model = load_model("models/Diabetes_Prediction_LGBM.pkl")

			prediction = model.predict(single_sample)
			pred_prob = model.predict_proba(single_sample)
			#st.write(prediction)

			if prediction == 1:
				st.error("Model Prediction: You are at Risk!!")
				st.warning("Model has categorized you as Positive Class with {}% confidence ".format(round(pred_prob[0][1]*100,2)))
				#st.write("Note: Probability score is the confidence with which the model has categorized you as Positive class.")
			
			elif prediction == 0:
				st.success("Model Prediction: You are safe!!")
				st.info("Model has categorized you as a Negative Class with {}% confidence".format(round(pred_prob[0][0]*100,2)))
				#st.write("Note: Probability score is the confidence with which the model has categorized you as Negative class.") 	

				

