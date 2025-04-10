# RNA Translation Counter

This repository contains a simple Python script that calculates the total number of possible RNA strings that can translate into a given protein string, accounting for the redundancy in the genetic code and including the stop codons.

## 🧬 Problem Description
Given a protein string of length at most 1000 amino acids, the goal is to compute the total number of different RNA strings that could have translated into that protein. The result is returned modulo 1,000,000.

## 📝 Input Format
- A text file named `protein.txt` containing a single line with the protein string (e.g., `MA`).

## 📤 Output Format
- A text file named `output.txt` containing a single integer representing the number of RNA strings modulo 1,000,000.

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/Shouryanpatil/rna-translation-counter.git
cd rna-translation-counter
```

2. Add your protein string to `protein.txt`.

3. Run the script:
```bash
python rna_translation_counter.py
```

4. Check `output.txt` for the result.

## 🐍 Script Overview
- **rna_translation_counter.py**: Reads a protein string from `protein.txt`, computes the total number of possible RNA strings using a codon table, and writes the result to `output.txt`.

## 📚 Example
### Input (`protein.txt`)
```
MA
```
### Output (`output.txt`)
```
12
```

## 🧠 Key Concepts
- **Codon Redundancy**: Most amino acids are coded by more than one codon.
- **Stop Codons**: There are 3 codons that signal the end of translation, which must be included in the final count.

## 🛠️ Requirements
- Python 3.x

No external libraries are required.

## 📄 License
This project is open source and available under the [MIT License](LICENSE).

---
