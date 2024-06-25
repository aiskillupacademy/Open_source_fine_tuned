## Open Source Fine-tuned LLM (nous-hermes2) 🧠

**Description:**

This Streamlit app empowers you to fine-tune the open-source "nous-hermes2" large language model (LLM) using your own training data. You can upload a CSV file containing instruction-response pairs, train the model, and then interact with it using the provided query interface.

**Features:**

- Fine-tune the "nous-hermes2" LLM with custom CSV data
- Train the model for multiple epochs
- Generate text responses based on user queries
- Set the maximum output token limit for generated responses
- Display estimated training time

**Requirements:**

- `streamlit` library
- `pandas` library
- `gradientai` library (specific instructions for installation might be needed)
- `langchain_community` library (specific instructions for installation might be needed)
- A Gradientai account with a workspace and access token ([https://www.gradient.ai/](https://www.gradient.ai/))

**Installation:**

1. Install the required libraries using `pip install streamlit pandas gradientai langchain_community`.
2. Create a Gradientai account and obtain your workspace ID and access token ([https://www.gradient.ai/](https://www.gradient.ai/)).
3. Store these credentials securely (environment variables recommended) before running the application.

**Usage:**

1. Clone or download this repository.
2. Set your Gradientai workspace ID and access token as environment variables:

   ```bash
   export GRADIENT_WORKSPACE_ID=YOUR_GRADIENT_WORKSPACE_ID
   export GRADIENT_ACCESS_TOKEN=YOUR_GRADIENT_ACCESS_TOKEN
   ```

3. Run the app using `streamlit run app.py`.

**Interface:**

1. **Data Upload:**
   - Upload a CSV file containing two columns: "Input" and "Output".
   - Each row represents an instruction-response pair for training the LLM.

2. **Model Training:**
   - Enter a descriptive name for your fine-tuned model.
   - Click the "Train " button to initiate the fine-tuning process.
   - The app will display training progress for multiple epochs based on the specified number of iterations.

3. **Query Generation:**
   - Enter your query in the text input field.
   - Use the slider to adjust the maximum output token limit for the generated response.
   - Click the "Enter ➤" button to send the query to the trained model.

4. **Results:**
   - The app will display the model used (by name) and initiate response generation.
   - Once complete, the generated response will be presented.
   - An estimated training time will also be shown.

**Further Considerations:**

- Fine-tuning quality depends greatly on the quality and quantity of your training data.
- Experiment with different training parameters and data sets to optimize results.
- For more advanced usage, explore the full capabilities of the `gradientai` and `langchain_community` libraries.

