import streamlit as st

# Set page configuration
st.set_page_config(page_title="Naam Jaap Counter 🙏", page_icon="🕉️")

# Initialize counter in session state
if 'count' not in st.session_state:
    st.session_state.count = 0

# Title and subtitle
st.title("Naam Jaap Counter 🙏")
st.markdown("### Keep chanting and counting with devotion! 🧘")

# Display current count in a larger, highlighted format
st.markdown(f"""
    <h2 style='text-align: center; color: #4CAF50; font-size: 36px;'>
        Current Count: {st.session_state.count}
    </h2>
""", unsafe_allow_html=True)

# Buttons for incrementing and resetting count
col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Increment Count", help="Click to increase count"):
        st.session_state.count += 1

with col2:
    if st.button("🔄 Reset Counter", help="Click to reset count to zero"):
        st.session_state.count = 0

# Encouraging message
st.markdown("**Stay dedicated and continue your Jaap! 🙏✨**")
