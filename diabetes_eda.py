import streamlit as st
import pandas as pd

#Load Data viz pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px



## Load dataset
@st.cache
def load_data(data):
	df = pd.read_csv(data)
	return df

def run_eda_app():
	st.subheader("Exploratory Data Analysis")
	st.write("Here you can gain more insights on the data used for training the model")
	#df = pd.read_csv('data/diabetes_data_upload.csv')
	df = load_data("data/diabetes_data_upload.csv")
	df_clean = load_data("data/diabetes_clean_data.csv")
	 

	submenu = st.sidebar.selectbox("Submenu",['Descriptive','Plots'])
	if submenu == 'Descriptive':
		st.dataframe(df)

		with st.beta_expander("Data Types"):
			st.dataframe(df.dtypes)

		with st.beta_expander("Descriptive Summary"):
			st.dataframe(df.describe())
			
		with st.beta_expander("Class Distribution"):
			st.dataframe(df['class'].value_counts())

		with st.beta_expander("Gender Distribution"):
			st.dataframe(df['Gender'].value_counts())

	
	

	else:
		st.subheader("Plots")

		# Layouts
		col1,col2 = st.beta_columns([1,1])
		with col1:
			with st.beta_expander("Distribution Plot of Gender"):
				st.write("Out of the total Females, 90% were found to be Positive class ")
				#fig = plt.figure()
        		#sns.countplot(data=df_clean["Gender"],x='class',hue='Gender')
				#st.pyplot(fig)
				# fig = plt.figure()
				# sns.countplot(df['Gender'])
				# st.pyplot(fig)

				gen_df = df['Gender'].value_counts().to_frame()
				gen_df = gen_df.reset_index()
				gen_df.columns = ['Gender Type','Counts']
				# st.dataframe(gen_df)
				p01 = px.pie(gen_df,names='Gender Type',values='Counts')
				st.plotly_chart(p01,use_container_width=True)

			with st.beta_expander("Dist Plot of Class"):
				fig = plt.figure()
				sns.countplot(df['class'])
				st.pyplot(fig)





		with col2:
			pass
			#with st.beta_expander("Gender Distribution"):
				#st.dataframe(df['Gender'].value_counts())

		#	with st.beta_expander("Class Distribution"):
		#		st.dataframe(df['class'].value_counts())

		#	with st.beta_expander("Polyuria vs Class"):
		#		cat_feat = ['Polyuria','Polydipsia','Polyphagia','sudden weight loss','Alopecia','Obesity','class']	
				
		#
		#		sns.countplot(df_clean['Polyuria'])
		#		st.pyplot(fig)
			
		#	with st.beta_expander("Polydipsia vs Class"):	
		#		fig = plt.figure()
		#		sns.countplot(df_clean['Polydipsia'])
		#		st.pyplot(fig)
		#		
 		#	with st.beta_expander("Polyphagia vs Class"):	
		#		fig = plt.figure()
		#		sns.countplot(df_clean['Polyphagia'])
		#		st.pyplot(fig)
			
		#	with st.beta_expander("Alopecia vs Class"):				
 		#		fig = plt.figure()
		#		sns.countplot(df_clean['Alopecia'])
		#		st.pyplot(fig)
				

 


				
 			

		with st.beta_expander("Frequency Dist Plot of Age"):
			# fig,ax = plt.subplots()
			# ax.bar(freq_df['Age'],freq_df['count'])
			# plt.ylabel('Counts')
			# plt.title('Frequency Count of Age')
			# plt.xticks(rotation=45)
			# st.pyplot(fig)
			fig = plt.figure()
			sns.histplot(data=df['Age'])
			st.pyplot(fig)
			#p = px.bar(freq_df,x='Age',y='count')
			#st.plotly_chart(p)

			#p2 = px.line(freq_df,x='Age',y='count')
			#st.plotly_chart(p2)

			####OUTLIER DETECTION PLOT REMOVED

		#with st.beta_expander("Outlier Detection Plot"):
			# outlier_df = 
			#fig = plt.figure()
			#sns.boxplot(df['Age'])
			#st.pyplot(fig)

			#p3 = px.box(df,x='Age',color='Gender')
			#st.plotly_chart(p3)

		with st.beta_expander("Correlation Plot"):
			corr_matrix = df_clean.corr()
			fig = plt.figure(figsize=(20,10))
			sns.heatmap(corr_matrix,annot=True)
			st.pyplot(fig)

			p3 = px.imshow(corr_matrix)
			st.plotly_chart(p3)
			plt.figure(figsize=(20,10))
			sns.heatmap(df_clean.corr(),annot=True)
			plt.show()

		
