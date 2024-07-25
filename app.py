import streamlit as st
import cohere

# Initialize the Cohere client with your API key
co = cohere.Client('XnjuHlhs02hrg1UYZYtx51Oi4XGRm8T2D2JYbV5N')

def generate_content(prompt, max_tokens=150):
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.7,
        stop_sequences=["."]
    )
    return response.generations[0].text.strip()

# Streamlit interface
st.title('Content Creation Assistant')

st.write("""
    Welcome to the Content Creation Assistant! This tool helps bloggers, marketers, and writers generate ideas and social media posts, and marketing campaigns.
""")

# Input for content type
content_type = st.selectbox(
    "Choose the type of content you want to generate:",
    ("Social Media Post", "Marketing Campaign")
)

# Input for content topic
user_input = st.text_area("Enter the topic or keywords:", "E.g., AI in healthcare")

if st.button('Generate Content'):
    if content_type == "Article Idea":
        prompt = f"Generate a list of article ideas based on the topic: {user_input}"
    elif content_type == "Social Media Post":
        prompt = f"Create a social media post about: {user_input}"
    else:
        prompt = f"Draft a marketing campaign focused on: {user_input}"

    content = generate_content(prompt)
    st.write(content)  # Display the generated content

   