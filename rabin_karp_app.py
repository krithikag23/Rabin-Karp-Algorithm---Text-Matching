import streamlit as st

# Rabin-Karp Algorithm
def rabin_karp(text, pattern, prime=101):
    n = len(text)
    m = len(pattern)
    d = 256
    h = pow(d, m - 1, prime)

    p_hash = 0
    t_hash = 0
    result = []

    if m > n:
        return []

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i + m] == pattern:
            result.append(i)
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0:
                t_hash += prime

    return result

# Streamlit UI Config
st.set_page_config(page_title="Rabin-Karp Text Matcher", page_icon="🔍")

# App Title
st.title("🔍 Rabin-Karp Text Matching App")

# Introduction Section
with st.expander("📘 About Rabin-Karp Algorithm"):
    st.markdown("""
    **Rabin-Karp** is a string-searching algorithm that uses **hashing** to find occurrences of a "pattern" string within a "text" string.

    🔧 **How it works**:
    - A hash is computed for the pattern.
    - Sliding over the text, a rolling hash is used to compare substrings.
    - If hashes match, then it checks character by character (to avoid false positives).

    ⏱ **Time Complexity**:
    - Best Case: **O(n + m)** — when hash values rarely match.
    - Average Case: **O(n + m)**
    - Worst Case: **O(nm)** — when all hash values match and comparison happens every time.

    📦 **Space Complexity**: O(1)

    ✅ **Applications**:
    - Plagiarism detection
    - Pattern recognition
    - Search engines
    - DNA sequencing

    👉 This app demonstrates how Rabin-Karp works on custom input files and patterns.
    """)

# File Upload
uploaded_file = st.file_uploader("📄 Upload a .txt file", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.text_area("📜 Uploaded Text", value=text, height=200, disabled=True)

    pattern = st.text_input("🔎 Enter the pattern to search for")

    if st.button("🚀 Find Matches"):
        if pattern and text:
            positions = rabin_karp(text, pattern)

            if positions:
                st.success(f"✅ Pattern found {len(positions)} time(s) at positions: {positions}")

                # Highlight Matches (Markdown)
                st.markdown("### 🔦 Highlighted Matches")
                highlighted = ""
                last = 0
                for pos in positions:
                    highlighted += text[last:pos]
                    highlighted += f"**:red[{text[pos:pos + len(pattern)]}]**"
                    last = pos + len(pattern)
                highlighted += text[last:]
                st.markdown(highlighted)

                # Stats
                st.markdown("### 📊 Match Statistics")
                col1, col2 = st.columns(2)
                col1.metric("Match Count", len(positions))
                col2.metric("Text Length", len(text))

                # Download Full Text with Highlighted Matches
                highlighted_txt = ""
                last = 0
                for pos in positions:
                    highlighted_txt += text[last:pos]
                    highlighted_txt += f"<<{text[pos:pos + len(pattern)]}>>"
                    last = pos + len(pattern)
                highlighted_txt += text[last:]

                st.download_button(
                    label="📥 Download Full Text with Highlights",
                    data=highlighted_txt,
                    file_name="highlighted_matches.txt",
                    mime="text/plain"
                )
            else:
                st.warning("⚠️ Pattern not found in the uploaded text.")
        else:
            st.error("❗ Please provide both text and a pattern.")
else:
    st.info("⬆️ Please upload a .txt file to get started.")
