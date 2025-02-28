# Predicția Riscului De Cancer Tiroidian

## Prezentare Generală

Aceasta este o aplicație de predicție a riscului de cancer tiroidian, dezvoltată cu ajutorul învățării automate pe baza unui set de date, care cuprinde 212.691 de statistici legate de factorii de risc pentru cancerul tiroidian. Include date demografice, istoricul clinic, stilul de viață și gradele cheie ale hormonilor tiroidieni. Utilizatorul poate folosi această aplicație prin intermediul unei interfațe interactive implementată cu Streamlit.

## Caracteristici

* Utilizează datele pacienților pentru a estima probabilitatea de risc.
* Antrenează și testează modele de învățare automată pentru predicția riscului de cancer tiroidian.
* Oferă o interfață web interactivă și ușor de utilizat cu ajutorul Streamlit.
* Rularea modelului în timp real pentru o evaluare rapidă.

## Tehnologii Utilizate

* Python - Limbajul principal de programare
* Scikit-learn - Modelul Machine Learning
* Streamlit - Crearea Interfeței Web
* Pandas, NumPy - Procesarea datelor
* Matplotlib, Seaborn - Vizualizarea datelor

## Interfața Web

<img src="interfetele Web/app.png" width="1000" height="550">

## Utilizare și Instalare

``` bash

git clone https://github.com/Lore10023/Thyroid_Cancer_Risk.git
cd "Thyroid Cancer Risk"

pip install -r biblioteci.txt

streamlit run app.py
