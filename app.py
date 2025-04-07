import streamlit as st
from collections import deque
from PIL import Image
import requests
from io import BytesIO


content_repository = [
    {"title": "Binary Search in Data Structures", "image": "https://miro.medium.com/v2/resize:fit:1200/1*QBsOC7m5XSiMFKgPc7hG2A.gif"},
    {"title": "Bubble Sort Algorithm Explained", "image": "https://miro.medium.com/v2/resize:fit:802/1*7seGXJi3te9beNfpAvFXEQ.gif"},
    {"title": "Understanding Stack vs Queue", "image": "https://miro.medium.com/v2/resize:fit:1400/1*pWZt8c1M3nK5KIAkHNut9A.gif"},
    {"title": "Depth First Search (DFS) and Breadth First Search (BFS)", "image": "https://miro.medium.com/v2/resize:fit:1280/1*GT9oSo0agIeIj6nTg3jFEA.gif"},
    {"title": "HashMap Implementation in Java", "image": "https://miro.medium.com/v2/resize:fit:800/1*5n4jECfFKDqv_3Eb7yQUoA.gif"},
    {"title": "Recursion and the Function Call Stack", "image": "https://content.codecademy.com/practice/art-for-practice/stackcall.gif"},
    {"title": "How Stack Overflow Happens in Recursion", "image": "https://media.lordicon.com/icons/wired/lineal/2567-logo-stack-overflow.gif"},
    {"title": "Greedy Algorithms vs Dynamic Programming", "image": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Greedy-search-path-example.gif"},
    {"title": "Basics of Object-Oriented Programming", "image": "https://www.shutterstock.com/image-vector/oop-object-oriented-programming-acronym-260nw-2029215269.jpg"}
]


def build_dfa(pattern):
    pattern = pattern.lower()
    dfa = [{} for _ in range(len(pattern)+1)]
    dfa[0][pattern[0]] = 1
    X = 0
    for i in range(1, len(pattern)):
        for c in set(pattern):
            dfa[i][c] = dfa[X].get(c, 0)
        dfa[i][pattern[i]] = i + 1
        X = dfa[X].get(pattern[i], 0)
    return dfa

def match_dfa(text, pattern):
    dfa = build_dfa(pattern)
    state = 0
    for char in text.lower():
        state = dfa[state].get(char, 0)
        if state == len(pattern):
            return True
    return False


st.sidebar.title("🔍 Navigation")
nav_home = st.sidebar.button("🏠 Home")
nav_search = st.sidebar.button("🔎 Search Courses")


if 'page' not in st.session_state:
    st.session_state.page = "Home"
if nav_home:
    st.session_state.page = "Home"
if nav_search:
    st.session_state.page = "Search"


if st.session_state.page == "Home":
    st.title("📚 EduKeySearch")
    st.subheader("DFA-based Keyword Search Engine for Intelligent Tutoring Systems")

    
    banner_url = "https://t4.ftcdn.net/jpg/02/36/21/57/360_F_236215734_DtGW6nWViuE5ccmbv88ITDIvKKQvVoqZ.jpg"
    response = requests.get(banner_url)
    img = Image.open(BytesIO(response.content))
    st.image(img, use_column_width=True)

    st.markdown("""
    ### About This Project
    This project demonstrates the use of **Deterministic Finite Automaton (DFA)** for fast and efficient keyword-based content search within an **Intelligent Tutoring System (ITS)**.

    🔍 **Key Features**:
    - DFA-based optimized keyword matching
    - Educational content browsing
    - Real-time course filtering

    👨‍💻 **Developer**: Shyam Raj D  
    🎓 **Department**: IT  
    🆔 **ID**: 7376222IT254
    """)


elif st.session_state.page == "Search":
    st.title("🔍 Course Search")
    st.markdown("Use DFA-based keyword matching to search relevant topics.")

    keyword = st.text_input("Enter keywords (e.g., recursion stack):")

    def display_courses(course_list):
        cols = st.columns(2)
        for idx, course in enumerate(course_list):
            with cols[idx % 2]:
                with st.container():
                    st.image(course["image"], width=250)
                    st.markdown(f"**{course['title']}**")
                    st.markdown("---")

    if keyword:
        matched_courses = []
        keywords = keyword.strip().split()

        for course in content_repository:
            if all(match_dfa(course["title"], key) for key in keywords):
                matched_courses.append(course)

        if matched_courses:
            st.subheader("📘 Matched Courses")
            display_courses(matched_courses)
        else:
            st.warning("No matching content found.")
    else:
        st.subheader("📘 All Courses")
        display_courses(content_repository)
