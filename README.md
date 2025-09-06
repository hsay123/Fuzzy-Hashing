# 🔑 Fuzzy Hashing Tool

A simple Python-based **fuzzy hashing tool** that uses [ssdeep](https://ssdeep-project.github.io/ssdeep/) to detect **similarities between files**.  
Unlike normal hashing (MD5/SHA256) that only detects identical files, fuzzy hashing can tell if two files are **partially similar**, which is useful in **malware analysis, forensics, and duplicate detection**.

---

## ⚙️ Features
- Generate **fuzzy hashes** for files
- Compare **two files** and output similarity score (0–100%)
- Scan a **directory** and print fuzzy hashes for all files
- Works on **Linux (Kali, Ubuntu, etc.)** and **Windows**

---

## 📦 Dependencies

### Linux (Debian/Kali/Ubuntu)
```bash
sudo apt update
sudo apt install ssdeep python3-ssdeep python3-pip -y
pip install ssdeep


Windows

Install Python 3
.

Open Command Prompt (cmd) or PowerShell and run:
pip install ssdeep




🚀 Usage

Clone or copy the script into a file named fuzzy.py.

1. Compare two files
python3 fuzzy.py -c file1.txt file2.txt


✅ Outputs fuzzy hashes of both files and a similarity score.

2. Scan all files in a directory
python3 fuzzy.py -d ./samples


✅ Prints fuzzy hashes for every file in the folder.



🛠️ Example
echo "The quick brown fox jumps over the lazy dog." > file1.txt
echo "The quick brown fox jumps over the smart dog." > file2.txt

python3 fuzzy.py -c file1.txt file2.txt


Output:

🔹 File 1: file1.txt
   Hash: 3:kU4h8:foxdog
🔹 File 2: file2.txt
   Hash: 3:kU4h9:foxdog

✅ Similarity Score: 86%


🔍 How It Works

Input → User provides files or directory.

Chunking → Files are split into blocks instead of hashing whole file.

Rolling Hash → Each chunk is hashed with a rolling algorithm.

Signature Generation → The sequence of chunk-hashes forms a fuzzy hash signature.

Comparison → Fuzzy hashes are compared using an edit distance algorithm.

Output → Tool prints fuzzy hashes and a similarity score (0–100%).

🎯 Use Cases

Malware variant detection

Digital forensics

Detecting modified or tampered files

Finding near-duplicate documents
