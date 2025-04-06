import streamlit as st
import time

# Rabin-Karp Algorithm with execution time tracking
def rabin_karp(text, pattern, prime=101):
    start_time = time.time()

    n = len(text)
    m = len(pattern)
    d = 256  # Number of characters in the input alphabet
    h = pow(d, m-1, prime)  # The value of d^(m-1)

    p_hash = 0  # Hash value for pattern
    t_hash = 0  # Hash value for text
    result = []

    if m > n:
        exec_time = time.time() - start_time
        return [], exec_time, n, m

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i+m] == pattern:
            result.append(i)
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0:
                t_hash += prime

    exec_time = time.time() - start_time
    return result, exec_time, n, m

# Streamlit UI
st.set_page_config(page_title="Rabin-Karp Matcher", page_icon="🔍", layout="wide")
st.title("🔍 Rabin-Karp Text Matching App")
st.markdown("Search for a pattern in your input text using the Rabin-Karp algorithm. Upload your text file or enter manually below.")

# Upload or text area
uploaded_file = st.file_uploader("📄 Upload a .txt file", type=["txt"])
if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
else:
    text = st.text_area("Or enter your text manually here:", height=200)

pattern = st.text_input("🔡 Enter the pattern to search")

# Find Matches
if st.button("Find Matches"):
    if not pattern or not text:
        st.error("❗ Please provide both text and pattern.")
    else:
        positions, exec_time, n, m = rabin_karp(text, pattern)

        # Output
        if positions:
            st.success(f"✅ Pattern found {len(positions)} time(s) at positions: {positions}")
        else:
            st.warning("⚠️ Pattern not found.")

        # Time & complexity analysis
        st.markdown("### 🧠 Time & Complexity Analysis")
        st.markdown(f"- Input Text Length (n): `{n}`")
        st.markdown(f"- Pattern Length (m): `{m}`")
        st.markdown(f"- Execution Time: `{exec_time:.6f} seconds`")
        st.markdown(f"- **Time Complexity**: `O(n + m)` on average, `O(n*m)` worst-case (when many hash collisions occur)")

        # Highlight matches
        st.markdown("### 🔦 Highlighted Text with Matches")
        highlighted = ""
        last = 0
        for pos in positions:
            highlighted += text[last:pos]
            highlighted += f"**:red[{text[pos:pos+len(pattern)]}]**"
            last = pos + len(pattern)
        highlighted += text[last:]
        st.markdown(highlighted)

        # Prepare file for download
        download_text = ""
        last = 0
        for pos in positions:
            download_text += text[last:pos]
            download_text += f"<<{text[pos:pos+len(pattern)]}>>"
            last = pos + len(pattern)
        download_text += text[last:]

        st.download_button(
            label="⬇️ Download Highlighted File",
            data=download_text,
            file_name="highlighted_output.txt",
            mime="text/plain"
        )
