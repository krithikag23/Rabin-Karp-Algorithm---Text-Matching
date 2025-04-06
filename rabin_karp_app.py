import streamlit as st
import time

# Page Config
st.set_page_config(page_title="Rabin-Karp Matcher", page_icon="🔍", layout="wide")
st.title("🔍 Rabin-Karp Text Matching App")

# --------------------------------------
# 📘 Rabin-Karp Theory (Non-Collapsible)
# --------------------------------------
st.markdown("""
### 📘 What is Rabin-Karp?

**Rabin-Karp** is a string-searching algorithm that uses hashing to detect the presence of a pattern in a text.

- It computes a hash for the pattern and then uses a **rolling hash** on the text.
- When the hash of a substring matches the pattern’s hash, it performs an exact comparison.
- This reduces unnecessary comparisons and makes it efficient when searching for multiple patterns.

#### 🔧 How it Works:
- Uses a prime number to reduce collisions.
- Rolling hash: efficient rehashing of the text window.

#### ⏱ Time Complexity:
- **Best & Average Case**: O(n + m)
- **Worst Case**: O(n * m), due to hash collisions

#### 📦 Space Complexity: O(1)

#### ✅ Applications:
- Plagiarism detection
- DNA sequence searching
- Search engines
- Spam filtering

---
""")

# --------------------------------------
# 📂 Upload Section
# --------------------------------------
uploaded_file = st.file_uploader("📄 Upload a .txt file", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
else:
    text = st.text_area("✍️ Or enter your text manually here:", height=200)

pattern = st.text_input("🔡 Enter the pattern to search")

case_sensitive = st.toggle("🔠 Case Sensitive?", value=True)

# --------------------------------------
# 🔍 Rabin-Karp Algorithm
# --------------------------------------
def rabin_karp(text, pattern, prime=101):
    start_time = time.time()

    n = len(text)
    m = len(pattern)
    d = 256
    h = pow(d, m - 1, prime)

    p_hash = 0
    t_hash = 0
    result = []

    if m > n:
        exec_time = time.time() - start_time
        return [], exec_time, n, m

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

    exec_time = time.time() - start_time
    return result, exec_time, n, m

# --------------------------------------
# 🚀 Execution Section
# --------------------------------------
if st.button("🚀 Find Matches"):
    if not text or not pattern:
        st.error("❗ Please provide both text and pattern.")
    else:
        search_text = text if case_sensitive else text.lower()
        search_pattern = pattern if case_sensitive else pattern.lower()

        positions, exec_time, n, m = rabin_karp(search_text, search_pattern)
        k = len(positions)

        # ✅ Match Result
        if positions:
            st.success(f"✅ Pattern found {k} time(s) at positions: {positions}")
        else:
            st.warning("⚠️ Pattern not found.")

        # 📊 Time & Complexity
        st.markdown("### 🧠 Time & Complexity Analysis")
        st.markdown(f"- Input Text Length (n): `{n}`")
        st.markdown(f"- Pattern Length (m): `{m}`")
        st.markdown(f"- Execution Time: `{exec_time:.6f} seconds`")

        total_operations = n + m + (k * m)
        st.markdown(f"- Number of Hash Comparisons: `{n - m + 1}`")
        st.markdown(f"- Number of Character Comparisons (k * m): `{k} * {m} = {k * m}`")

        st.markdown("### 📈 Estimated Time Complexity: `O(n + m + k*m)`")
        st.code(f"O({n} + {m} + {k}*{m}) = O({total_operations})", language="python")

        # 🔦 Highlighted Result
        st.markdown("### 🔦 Highlighted Matches in Text")
        highlighted = ""
        last = 0
        for pos in positions:
            highlighted += text[last:pos]
            highlighted += f"**:red[{text[pos:pos + len(pattern)]}]**"
            last = pos + len(pattern)
        highlighted += text[last:]
        st.markdown(highlighted)

        # 📥 Download Output
        download_text = ""
        last = 0
        for pos in positions:
            download_text += text[last:pos]
            download_text += f"<<{text[pos:pos + len(pattern)]}>>"
            last = pos + len(pattern)
        download_text += text[last:]

        st.download_button(
            label="⬇️ Download Highlighted Output",
            data=download_text,
            file_name="highlighted_output.txt",
            mime="text/plain"
        )
