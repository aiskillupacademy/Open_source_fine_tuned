import streamlit as st
import pandas as pd
import os
from gradientai import Gradient
from langchain_community.llms import GradientLLM
import time

os.environ["GRADIENT_WORKSPACE_ID"] = st.secrets["GRADIENT_WORKSPACE_ID"]
os.environ["GRADIENT_ACCESS_TOKEN"] = st.secrets["GRADIENT_ACCESS_TOKEN"]
st.set_page_config(
    page_title="Open source fine tuned LLM",
    page_icon="🧠"
)

st.title("Fine tuned LLM (nous-hermes2)")
model_id = "76efe711-7081-4a49-8f62-961d63bd0ba3_model_adapter"
model_name=""
with st.form(key='my_form'):
    # File upload widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # Process uploaded file
    if uploaded_file is not None:
    # Read the CSV file as a DataFrame
        df = pd.read_csv(uploaded_file, encoding="utf-8")

    mname = st.text_input("Model name:", placeholder="Give model name", key='name')
    model_name = mname
    submit_button = st.form_submit_button(label='Train 💻')
    #submit_button = st.form_submit_button(label='Enter ➤')
if submit_button:
    with st.spinner('Training LLM...'):
        gradient = Gradient()

        base_model = gradient.get_base_model(base_model_slug="nous-hermes2")

        new_model_adapter = base_model.create_model_adapter(
            name=mname
        )
        model_id = new_model_adapter.id
        samples=[]
        for index, row in df.iterrows():
            instruct = row['Input']
            response = row['Output']
            x = {"inputs": f"Instruction: {instruct} \n\nResponse: {response}"}
            samples.append(x)

        ## Lets define parameters for finetuning
        num_epochs=3
        count=0
        while count<num_epochs:
            st.info(f"Fine tuning the model with iteration {count + 1}")
            new_model_adapter.fine_tune(samples=samples)
            count=count+1
        st.success(f"Model with id {model_id} trained!")

with st.form(key='my_form2'):
    query = st.text_input("Query:", placeholder="Describe your query", key='comp')
    num_out = st.slider("Output token limit:", min_value=100, max_value=512, value=400)
    submit_button2 = st.form_submit_button(label='Enter ➤')
if submit_button2:
    st.info(f"Model to be used: {model_name}")
    llm = GradientLLM(
        model=model_id,
        model_kwargs=dict(max_generated_token_count=num_out)
        )
    with st.spinner("Generating response..."):
        start_time = time.time()
        st.write(llm.invoke(query))
        end_time = time.time()
        st.info(f"Time taken: {round(end_time-start_time)} seconds")