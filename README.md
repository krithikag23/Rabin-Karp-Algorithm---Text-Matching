# 🔍 Rabin-Karp Text Matching App

A simple and interactive Streamlit web application that demonstrates the **Rabin-Karp string matching algorithm**. Upload a `.txt` file, enter a pattern to search, and visualize matched positions with highlighting. Ideal for learners, educators, and algorithm enthusiasts.

---


## 📌 Features


- ✅ Upload any `.txt` file as input
- ✅ Search for any pattern using Rabin-Karp algorithm
- ✅ Highlight matched patterns in the text
- ✅ Download the annotated result file
- ✅ User-friendly interface with Streamlit
- ✅ Displays matched positions and match count
- ✅ Real-time performance with hash-based efficiency

---

## 🧠 About the Rabin-Karp Algorithm

Rabin-Karp is a pattern matching algorithm that uses **hashing** to find any one of a set of pattern strings in a text. It is particularly efficient when searching for multiple patterns or when the pattern occurs frequently in the text.

- **Time Complexity**:  
  - Average case: O(n + m)  
  - Worst case (with many hash collisions): O(nm)

- **Use Cases**:  
  - Plagiarism detection  
  - DNA sequence analysis  
  - Intrusion detection systems  
  - Pattern matching in large text corpora

---

## 🚀 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/krithikag23/rabin-karp-streamlit-app.git
   cd rabin-karp-streamlit-app
