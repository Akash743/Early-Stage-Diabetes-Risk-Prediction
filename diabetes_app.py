import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image
from time import time
## Importing our Mini Apps
from diabetes_eda import *
from ml_app import *

st.set_page_config(page_title="Early Stage Diabetes Risk Prediction")


#<h4 style="color:white;text-align:center;">Diabetes </h4>
html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Early Stage Diabetes Risk Prediction </h1>
		
		</div>
		"""
desc_temp="""
			### Early Stage Diabetes Risk Predictor App
			
			The data for training this Machine Learning Model has been collected using direct questionnaires from the patients of Sylhet Diabetes
			Hospital in Sylhet, Bangladesh.
			
			As the data was donated just recently in July, 2020 for research and is from our neighbouring country with almost similar climate, topography, 
			standard of living and hence lifestyles, the model stands relevant in context of India also.
			
			This dataset contains the sign and symptoms of newly diabetic or would be diabetic patients. So, the model is relevant to caution you with an early 
			alarm based on the observable symptoms you have, if any, right now so that necessary actions could be taken in time to prevent diabetes.
			
			Kindly note, this may not be relevant for diabetic patients on medications having the major symptoms suppressed. 

			This is just a preliminary kind of test based on symptoms from a limited dataset and is in no way a substitute to much advanced and accurate tests
			available based on the blood sugar level, cholestrol, etc.
			
			Hence, I urge not to treat this as any kind of final report/declaration on your health condition/diabetes whatsoever and is recommended to consult a doctor in case
			you have these symptoms.

			#### App Content
				Click on the sidebar at top left corner to access following sections of the app: 
				- Data Exploration Section: Here you will find the description and analysis of the training dataset used to biuild the model.
				- Model Prediction Section: Here you will be able to select the symptoms, if any, to predict whether you are at risk or not.
				- Know more about diabetes: DO NOT SKIP THIS! Here you will find information about Diabetes and Health tips related to a healthy & diabetes free lifestyle.

			


			#### Datasource
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			

			

			"""

diabetes_description = """
            ### Diabetes
Diabetes is a metabolic disease that causes high blood sugar. The hormone insulin moves sugar from the 
blood into your cells to be stored or used for energy. With diabetes, your body either doesn’t make enough insulin or can’t effectively use 
the insulin it does make.

Untreated high blood sugar from diabetes can damage your nerves, eyes, kidneys, and other organs.

There are a few different types of diabetes:

- Type 1 diabetes is an autoimmune disease. The immune system attacks and destroys cells in the pancreas, where insulin is made. 
It’s unclear what causes this attack. About 10 percent of people with diabetes have this type.
One is more likely to get type 1 diabetes if you’re a child or teenager, you have a parent or sibling with the condition, 
or you carry certain genes that are linked to the disease.

- Type 2 diabetes occurs when your body becomes resistant to insulin, and sugar builds up in your blood.
Your risk for type 2 diabetes increases if you:

		* are overweight
		* are age 45 or older
		* have a parent or sibling with the condition
		* aren’t physically active
		* have had gestational diabetes
		* have prediabetes
		* have high blood pressure, high cholesterol, or high triglycerides

- Prediabetes occurs when your blood sugar is higher than normal, but it’s not high enough for a diagnosis of type 2 diabetes.

- Gestational diabetes is high blood sugar during pregnancy. Insulin-blocking hormones produced by the placenta cause this type of diabetes. 


As of 2019, an estimated 463 million people had diabetes worldwide (8.8% of the adult population), with type 2 diabetes making up about 90% 
 of the cases.Rates are similar in women and men.			

References: https://www.healthline.com/health/diabetes#complications
			https://en.wikipedia.org/wiki/Diabetes



			"""	

health_tips_for_diabetes = """
- Work Out regularly and lose weight if you're overweight or obese. Aim for 30. Try to be intentionally active by taking a walk, dancing, lifting weights or swimming for 30 minutes, five days per week. 

- Cut sugar and refined carbohydrates from your diet. Eating foods high in refined carbohydrates and sugar increases blood sugar and insulin levels, which may lead to diabetes over time.

- The body is water, so keep yourself hydrated. It may help control blood sugar and insulin levels, thereby reducing the risk of diabetes.

- Have adequate amount of fiber in your diet. Rich sources include vegetables such as broccoli, carrots, sweetcorn, peas, beans and pulses. Fruits(berries, pears, melon, oranges), nuts & seeds are also good sources.

- Consuming a good fiber source at each meal helps in weight management, prevents spikes in blood sugar and insulin levels, which may help reduce your risk of developing diabetes. 

- Eat good quality and quantity of protein

- Quit smoking, can't emphasize more. Smoking can contribute to insulin resistance, which can lead to type 2 diabetes. Quitting has been shown to reduce the risk of type 2 diabetes over time.  

References: https://www.gundersenhealth.org/health-wellness/be-well/6-natural-ways-to-prevent-diabetes-before-it-starts/
			https://www.indushealthplus.com/diet-tips-diabetes.html
						"""




def main():
	#st.title("Main App")
	



	menu = ['Home','Data Exploration','Model Prediction','Know more about Diabetes',]
	choice = st.sidebar.selectbox('Menu',menu)

	if choice == 'Home':
		
		stc.html(html_temp)
		st.subheader("Home")
		#st.write(desc_temp)
		st.markdown(desc_temp,unsafe_allow_html=True)
		
	elif choice=='Data Exploration':
		
		st.header("*Let's explore!*            ")
		img2 = Image.open("DA.jpg")
		st.image(img2,use_column_width=True)
		#st.subheader("*Let's get some insights from model training data!*")
		run_eda_app()
		
	elif choice == 'Model Prediction':
		st.subheader('*Predict your results here!*')
		st.write("       ")
		st.write("       ")
		img3 = Image.open("AI.jpg")
		st.image(img3,use_column_width=True)
		
		run_ml_app()

	elif choice == 'Know more about Diabetes':
		img = Image.open("diabetes.jpg")
		st.image(img,use_column_width=True)
		st.subheader('*A little knowledge is always helpful!*')
		st.markdown(diabetes_description,unsafe_allow_html=True)
		st.subheader('*Health Tips for Diabetes*')
		st.markdown(health_tips_for_diabetes,unsafe_allow_html=True)	








if __name__=='__main__':
	main()
