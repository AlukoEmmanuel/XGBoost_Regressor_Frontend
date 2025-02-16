# import streamlit as st
# from dotenv import load_dotenv
# import requests
#
# # If you have environment variables (like base URL), load them here.
# load_dotenv()
#
# # Define the base URL for the API (adjust as needed)
# base_url =("BASE_URL", "http://localhost:8005")
#
# # Set page configuration
# st.set_page_config(
#     page_title="Insurance Charges Prediction",
#     page_icon="💰",
#     layout="centered",
#     initial_sidebar_state="expanded",
# )
#
# # Add a title and description with corrected HTML markup
# st.markdown(
#     """
#     <style>
#     .main {
#         background-color: #f9f9f9;
#         padding: 20px;
#         border-radius: 10px;
#     }
#     .title {
#         font-size: 30px;
#         font-weight: bold;
#         color: #4CAF50;
#         margin-bottom: 20px;
#     }
#     .footer {
#         text-align: center;
#         font-size: 14px;
#         color: #777;
#         margin-top: 50px;
#     }
#     </style>
#     <div class="main">
#       <h1 class="title">Insurance Charges Prediction</h1>
#       <p class="subtitle">Easily <b>predict insurance charges</b> based on filling out the form below!</p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )
#
# # Fetch metadata from FastAPI
# def fetch_entities(endpoint):
#     try:
#         result = requests.get(f"{base_url}/api/entities/{endpoint}")
#         if result.status_code == 200:
#             return result.json()
#         else:
#             st.error(f"Error: ❌ Could not fetch {endpoint} entities.Please check the API service" )
#             return None
#     except Exception as e:
#         st.error(f"Error: {e}")
#         return None
#
# sex_entities = fetch_entities("sex")
# smoker_entities = fetch_entities("smoker")
# region_entities = fetch_entities("region")
#
# # User input form
# with st.form("user_input_form"):
#     st.write("### User Details")
#     age = st.number_input("👩 Age:", min_value=0, max_value=120, value=30, step=1)
#
#     # Sex input
#     if sex_entities:
#         sex_options = [item["label"] for item in sex_entities["sex"]]
#     sex_input = st.radio("👩🏻‍🤝‍👨🏼 Sex:", sex_options, horizontal=True)
#     sex = next(item["value"] for item in sex_entities["sex"] if item["label"] == sex)
#
#     bmi = st.number_input("📇 BMI (Body Mass Index):", min_value=0.0, max_value=100.0, value=25.0, step=0.1)
#     children = st.slider("👶👦👧 Number of Children:", min_value=0, max_value=10, value=0, step=1)
#
#     # Smoker input
#     smoker_input = st.radio("🚬 Smoker:", ["No", "Yes"], horizontal=True)
#     smoker = 0 if smoker_input == "No" else 1
#
#     # Region select box with a complete list (adjust the regions to match your encoding)
#     region = st.selectbox("Region:", ["Northwest", "Southeast", "Southwest", "Northeast"])
#
#     # Encode region as binary flags
#     northwest, southeast, southwest = 0, 0, 0
#     if region == "Northwest":
#         northwest = 1
#     elif region == "Southeast":
#         southeast = 1
#     elif region == "Southwest":
#         southwest = 1
#     # For "Northeast" all flags remain 0
#
#     submitted = st.form_submit_button("Predict 🔮")
#
#     if submitted:
#         # Prepare payload for API request
#         api_url = f"{base_url}/api/predict"
#         data = {
#             "age": age,
#             "sex": sex,
#             "bmi": bmi,
#             "children": children,
#             "smoker": smoker,
#             "northwest": northwest,
#             "southeast": southeast,
#             "southwest": southwest
#         }
#         with st.spinner("Fetching prediction....🔮"):
#             response = requests.post(api_url, json=data)
#
#         if response.status_code == 200:
#             prediction = response.json()["predicted_charges"]
#             st.success(f"🔮 Predicted Insurance Charges: **${prediction:.2f}**")
#             st.balloons()
#         else:
#             st.error("❌ Error: Unable to parse JSON response.")
#
#         #Footer
#         st.markdown(
#             """
#
#             <div class="footer">
#                Made with 💖 using streamlit.
#             </div>
#
#             """,
#             unsafe_allow_html = True,
#         )
#
# #To run the application "streamlit run App.py"
#
#
#
#         # Make the API request to the FastAPI endpoint
#         #try:
#             #response = requests.post(f"{base_url}/predict", json=payload)
#             #response.raise_for_status()
#             #prediction = response.json().get("predicted_charges")
#             #st.success(f"Predicted Charges: {prediction}")
#         #except requests.exceptions.RequestException as e:
#             #st.error(f"An error occurred: {e}")
