# import os
# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as genai
# import shelve

# st.markdown(
#     """
#     <style>
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     button[title="View fullscreen"]{
#     visibility: hidden;}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Load environment variables
# load_dotenv()
# os.environ['GRPC_VERBOSITY'] = 'ERROR'

# # Configure Gemini model
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# generation_config = {
#     "temperature": 1,
#     "top_p": 0.95,
#     "top_k": 64,
#     "max_output_tokens": 8192,
#     "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#     model_name="gemini-1.5-flash",
#     generation_config=generation_config,
#     system_instruction="You are Prakriti AI🍃, created by SHIVAN ANAND. Your role is to assist users with their sustainability-related queries. Here are the details about Shivan Anand that you should know:\n\nShivan is a Btech student at Guru Gobind Singh Indraprastha University East Delhi Campus in the field of Artificial Intelligence and Data Science. he is a cat lover and passionate about AI, ML, and web3. He is constantly learning and exploring new technologies to broaden my skill set. However to know more about Shivan, his portfolio website is (https://shivan.up.railway.app/), his GitHub profile is (https://github.com/SHIVANANAND), his twitter account is (https://x.com/SHIVAN_ANAND_), and his LinkedIn account is (https://www.linkedin.com/in/shivan-anand-/)\n\n As you are a sustainability relatedd chatbot you should know about the SDGs. Here are the 17 Sustainable Development Goals (SDGs):\nNo Poverty: Ending extreme poverty in all its forms everywhere.\nZero Hunger: Ending hunger, achieving food security and improved nutrition, and promoting sustainable agriculture.\nGood Health and Well-being: Ensuring healthy lives and promoting well-being for all at all ages.\nQuality Education: Ensuring inclusive and equitable quality education and promoting lifelong learning opportunities for all.\nGender Equality: Achieving gender equality and empowering all women and girls.\nClean Water and Sanitation: Ensuring availability and sustainable management of water and sanitation for all.\nAffordable and Clean Energy: Ensuring access to affordable, reliable, sustainable, and modern energy for all.\nDecent Work and Economic Growth: Promoting sustained, inclusive, and sustainable economic growth, full and productive employment, and decent work for all.\nIndustry, Innovation and Infrastructure: Building resilient infrastructure, promoting inclusive and sustainable industrialization, and fostering innovation.\nReduced Inequalities: Reducing inequality within and among countries.\nSustainable Cities and Communities: Making cities and human settlements inclusive, safe, resilient, and sustainable.\nResponsible Consumption and Production: Ensuring sustainable consumption and production patterns.\nClimate Action: Taking urgent action to combat climate change and its impacts.\nLife Below Water: Conserving and sustainably using the oceans, seas and marine resources for sustainable development.\nLife on Land: Protecting, restoring, and promoting sustainable use of terrestrial ecosystems, sustainably managing forests, combating desertification, and halting and reversing land degradation and halting biodiversity loss.\nPeace, Justice, and Strong Institutions: Promoting peaceful and inclusive societies for sustainable development, providing access to justice for all, and building effective, accountable, and inclusive institutions at all levels.\nPartnerships for the Goals: Strengthening the means of implementation and revitalizing the global partnership for sustainable development.\n\nYou do not answer questions that are not directly related to sustainability. For example if user ask questions like, who is any person, or who is the prime minister of any nation then you must reject to answer those queries. But you can answer the questions related to Shivan Anand",
# )

# st.markdown("""
# <style>
#     .prakritiailogo {
#         font-size: 70px !important;        
#     }
# </style>
# <h1 class='prakritiailogo'>Prakriti AI🍃</h1>
# """, unsafe_allow_html=True)

# USER_AVATAR = "👤"
# BOT_AVATAR = "🍃"

# # Load chat history from shelve file
# def load_chat_history():
#     with shelve.open("chat_history") as db:
#         return db.get("messages", [])

# # Save chat history to shelve file
# def save_chat_history(messages):
#     with shelve.open("chat_history") as db:
#         db["messages"] = messages

# # Convert messages to Gemini model's expected format
# def format_history(messages):
#     formatted_history = []
#     for message in messages:
#         formatted_message = {
#             "role": "user" if message["role"] == "user" else "model",
#             "parts": [message["content"]]
#         }
#         formatted_history.append(formatted_message)
#     return formatted_history

# # Initialize or load chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = load_chat_history()

# # Sidebar with a button to delete chat history
# with st.sidebar:
#     st.markdown('# Prakriti AI🍃')
#     st.markdown('## By SHIVAN ANAND')
#     st.markdown("""
#     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
#     <style>
#         a {
#             color: white !important;
#             text-decoration: none;
#             margin-right: 10px;
#         }
#         a:hover {
#             text-decoration: none;
#         }
#         i {
#             font-size: 24px;
#             color: white;
#         }
#         i:hover {
#            color: #e95268;     
#         }
#     </style>
    
#     <a href="https://shivan.up.railway.app/" target="_blank">
#         <i class="fa fa-briefcase" aria-hidden="true"></i>
#     </a>
#     <a href="https://www.linkedin.com/in/shivan-anand-" target="_blank">
#         <i class="fab fa-linkedin" aria-hidden="true"></i>
#     </a>
#     <a href="https://x.com/SHIVAN_ANAND_" target="_blank">
#         <i class="fab fa-twitter" aria-hidden="true"></i>
#     </a>
#     <a href="https://github.com/SHIVANANAND" target="_blank">
#         <i class="fab fa-github" aria-hidden="true"></i>
#     </a>
#     """, unsafe_allow_html=True)

#     st.write("")
    
#     if st.button("Delete Chat History"):
#         st.session_state.messages = []
#         save_chat_history([])
    

# # Display chat messages
# for message in st.session_state.messages:
#     avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
#     with st.chat_message(message["role"], avatar=avatar):
#         st.markdown(message["content"])

# # Main chat interface
# if prompt := st.chat_input("How can I help?"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user", avatar=USER_AVATAR):
#         st.markdown(prompt)

#     # Format chat history and generate response from Gemini model
#     formatted_history = format_history(st.session_state.messages)
#     chat_session = model.start_chat(history=formatted_history)

#     # Send the user input to the chat session
#     response = chat_session.send_message(prompt)
#     model_response = response.text

#     with st.chat_message("model", avatar=BOT_AVATAR):
#         st.markdown(model_response)

#     st.session_state.messages.append({"role": "model", "content": model_response})

# # Save chat history after each interaction
# save_chat_history(st.session_state.messages)
import streamlit as st
import fitz  # PyMuPDF
import google.generativeai as genai

st.title("PDF Q&A with Gemini (PyMuPDF)")

# Gemini API Key
api_key = "AIzaSyD-_mIjZcRBYJQayHTStDw8Xoiy0yIh1-k"

if not api_key:
    st.warning("Please enter your Gemini API key.")
    st.stop()

genai.configure(api_key=api_key)

# List available models
try:
    models = genai.list_models()
    available_models = [model.name for model in models if "generateContent" in model.supported_generation_methods]

    if not available_models:
        st.error("No compatible models found. Please check your API key and permissions.")
        st.stop()

    model_name = st.selectbox("Select a Gemini model:", available_models, index=0) # select the first available model.

    model = genai.GenerativeModel(model_name)

except Exception as model_error:
    st.error(f"Error listing models: {model_error}")
    st.stop()

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    try:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as pdf_document:
            extracted_text = ""
            for page_number in range(pdf_document.page_count):
                page = pdf_document[page_number]
                extracted_text += page.get_text() + "\n\n"

        st.subheader("Extracted PDF Text (Context):")
        st.text_area("PDF Content", value=extracted_text, height=300)

        question = st.text_input("Enter your question about the PDF:")

        if st.button("Get Answer from Gemini"):
            if not question:
                st.warning("Please enter a question.")
            else:
                prompt = f"Context: {extracted_text}\n\nQuestion: {question}\n\nAnswer:"
                try:
                    response = model.generate_content(prompt)
                    st.write("Gemini's Answer:", response.text)
                except Exception as e:
                    st.error(f"Gemini API Error: {e}")

    except Exception as e:
        st.error(f"PDF Processing Error: {e}")