import os
import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(
    page_title="VGN Homes Assistant",
    page_icon="🏡",
    layout="centered"
)

# Title and introduction
st.title("VGN Homes AI Assistant")
st.write("Ask questions about VGN Homes real estate services")

# Initialize session state variables if they don't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# About Us section
with st.expander("About VGN Homes"):
    st.markdown("""
    **Founded in 1942, VGN is a leader, visionary and a pioneer in the real estate business and stands out distinctly among its competitors. Headquartered in Chennai, we are one of the oldest and most trusted real estate companies, certified by ISO 14001:2004. Years of experience helped us create our own path by understanding our customer's desires and helped us improve their quality of life by providing them with the best projects. And this has helped us become a brand that customers deeply trust.**
    
    **We always believed in going the extra mile for our customers. That's why just ordinary plotted developments weren't enough. Every idea, every unique feature, and our passion reflected in our projects, and our customer family grew rapidly, making us a trustworthy brand.**
    
    **Our projects are spread across the city with plenty of happy families and investors reaping from their investments. Residential, commercial, retail and plots, we develop and transform land of every kind. With our expertise in consumer behavior, we have offered plots with unmatched quality, right from affordable to ultra-luxury.**
    
    **As much as we take pride in our range of offering, we are also proud of our industry-best practices, transparency and customer service. And this inspires us to do more and venture into many more challenges with confidence.**
    """)

# Function to get AI response
def get_ai_response(user_query):
    # Hard-coded API key (in practice, use environment variables)
    api_key = "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"
    model = "llama3-70b-8192"
    
    try:
        # Initialize the Groq client
        client = Groq(api_key=api_key)
        
        prompt = (
            f"You are a customer support assistant for VGN Homes, a real estate company. "
            f"Answer the customer's question concisely (max 30 words), using only facts. "
            f"VGN HOMES PRIVATE LIMITED is located at No.333, Poonamallee High Road, Amaindakarai, Chennai – 600 030. "
            f"Email: info@vgngroup.org, Phone: +91 44 4393 7979. "
            f"Founded in 1942, VGN is a leader in real estate, certified by ISO 14001:2004. "
            f"They develop residential, commercial, retail properties and plots across Chennai ranging from affordable to ultra-luxury."
            f"\n\nQuestion: {user_query}"
        )
        
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Error: {str(e)}"

# User input
user_query = st.chat_input("Ask about VGN Homes...")

if user_query:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_query)
    
    # Display assistant response with a loading spinner
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_ai_response(user_query)
            st.write(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Add instructions at the bottom
st.markdown("---")
st.caption("Ask questions about properties, amenities, pricing, or contact information.")