# 📚 EduKeySearch – DFA-Optimized Keyword Search Engine for ITS

EduKeySearch is a mini project that showcases an **efficient keyword-based content search system** using **Deterministic Finite Automaton (DFA)**. It is tailored for **Intelligent Tutoring Systems (ITS)** to help learners quickly find educational resources by entering simple search terms.

**Live Demo**: [Click to open the app](https://dfa-optimised-search.streamlit.app/)

---

## About the Project

In modern digital education platforms, learners often struggle to find the exact content due to poor search mechanisms. EduKeySearch addresses this issue with a DFA-based search engine that ensures **fast**, **precise**, and **case-insensitive** keyword matching.

---

## Key Features

- DFA-based pattern matcher for efficient keyword search  
- Beautiful course cards with images and titles  
- Real-time filtering of educational content  
- Sidebar navigation between **Home** and **Search**  
- Responsive layout built using **Streamlit**

---

## How DFA Works in This Project

- A **Deterministic Finite Automaton (DFA)** is constructed for every keyword entered by the user.
- This DFA is used to **match substrings** inside course titles quickly.
- Unlike regular Python `in` or regex, DFA matching is optimized to process text in **O(n)** time with **constant-time transitions**, ideal for real-time filtering.

---

## Developer Info

- **Name**: Shyam Raj D  
- **Department**: IT  
- **Student ID**: 7376222IT254

---

## Tech Stack

- Python 3  
- Streamlit  
- PIL & Requests for image handling  
- DFA logic implemented from scratch  

