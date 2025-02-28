import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mp
from sklearn.preprocessing import LabelEncoder

st.title("Data Analysis")


st.caption("Welcome to the Data Analysis section! In this analysis, we aim to explore and understand various factors that contribute to thyroid cancer, focusing on a dataset that includes crucial medical and lifestyle information.")
st.caption("The dataset includes multiple variables related to age, gender, family history, radiation exposure, obesity, and several important thyroid hormone levels. By examining the relationships between these features, we can uncover patterns that could help in identifying potential risk factors for Thyroid Cancer and other related conditions.")
st.caption("Our goal is to provide actionable insights by identifying the most significant patterns and relationships within the data, which could potentially aid in risk assessment and early detection strategies for thyroid cancer.")


data=pd.read_csv("thyroid_cancer_risk_data.csv")

#-----------------------------------------------Correlation Heatmap--------------------------------------------------

st.header("Correlation Heatmap with Features")

object_column = data.select_dtypes(include=['object', 'category']).columns

le=LabelEncoder()

for col in object_column:
  data[col]= le.fit_transform(data[col])

correlation_matrix = data.corr()

mp.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap="Reds", fmt='.2f')

st.pyplot(mp)


#-------------------------------------------------Age and Country -> Thyroid Cancer Risk-------------------------------------

data2=pd.read_csv("thyroid_cancer_risk_data.csv")
risk_map = {"Low": 0, "Medium": 1, "High": 2}
data2['Risk_Numeric'] = data2['Thyroid_Cancer_Risk'].map(risk_map)

fig, ax = mp.subplots(figsize=(10,8))

scatter = ax.scatter(
  data2["Country"],
  data2["Age"],
  c=data2["Risk_Numeric"],
  cmap="coolwarm",
  alpha = 0.7
)

cbar = mp.colorbar(scatter, ax=ax)
cbar.set_label("Thyroid Cancer Risk(Low=0, Medium=1, High=2)")

ax.set_xlabel("Country")
ax.set_ylabel("Age")
ax.set_title("Country vs. Age")

st.pyplot(fig)

#-------------------------------------------------Histogram for all the data-------------------------------------

data3=pd.read_csv("thyroid_cancer_risk_data.csv")

if 'Patient_ID' in data3.columns:
        data3 = data3.drop('Patient_ID', axis=1)

numeric_colums = data3.select_dtypes(include=['number']).columns
obj_colums = data3.select_dtypes(include=['object', 'category']).columns

col1, col2 = st.columns(2)

with col1:
    st.write("### Histograms for Numeric Columns")

    for column in numeric_colums:
      fig, ax = mp.subplots(figsize=(10,8))
      ax.hist(data3[column].dropna(),bins=20, color='skyblue', edgecolor='black')
      ax.set_title(f"Histogram of {column}")
      ax.set_xlabel(column)
      ax.set_ylabel("Frequency")
      st.pyplot(fig)


with col2:
    st.write("### Bar Plots for Categorical Columns")
    for column in obj_colums:
      fig, ax = mp.subplots(figsize=(10,8))
      sns.countplot(x=data3[column], palette='Set2', ax=ax)
      ax.set_title(f"Bar Plot of {column}")
      ax.set_xlabel(column)
      ax.set_ylabel("Count")
      st.pyplot(fig)