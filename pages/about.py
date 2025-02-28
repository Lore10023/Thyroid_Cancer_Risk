import streamlit as st

st.title("About Thyroid Cancer and AI model")

st.header("What Is Thyroid Cancer?")


col1, col2 = st.columns([1, 1.2])  # Adjust width ratio as needed

with col1:
    st.image("images/thyroid_cancer.png", width=300)

with col2:
    st.write("**Thyroid cancer** is a growth of cells that starts in the **thyroid gland**. The thyroid is a butterfly-shaped gland located at the base of the neck, just below the Adam's apple. The thyroid produces hormones that regulate heart rate, blood pressure, body temperature and weight. The amount of thyroid hormone released by the thyroid is regulated by the pituitary gland at the base of your brain. This gland makes a substance called **thyroid-stimulating hormone (TSH)**.")

st.write("    Thyroid cancer might not cause any symptoms at first. But as it grows, it can cause signs and symptoms, such as swelling in your neck, voice changes and difficulty swallowing. Several types of thyroid cancer exist. Many types of growths and tumors can develop in the thyroid gland. Most of these are benign (non-cancerous), but others are malignant (cancerous), which means they can spread into nearby tissues and to other parts of the body.")

st.write("    **Most thyroid cancers are highly curable**. Treatments include surgery, chemotherapy, radiation, hormone therapy and radioiodine therapy.")

#st.image("images/thyroid_cancer.png",width=500)

st.header("Purpose of AI in Thyroid Cancer")

st.write("   AI models in thyroid cancer research and diagnosis serve multiple purposes, helping doctors, researchers, and patients by improving accuracy, speed, and efficiency.")

st.write("   The datasets that I use incorporates 212,691 statistics related to **thyroid cancer risk factors**. It includes demographic facts, clinical history, lifestyle factors, and key thyroid hormone degrees to assess the probability of thyroid most cancers.")