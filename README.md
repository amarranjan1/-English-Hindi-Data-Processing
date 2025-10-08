English Hindi Translation Assessment

Assignment 1
This script processes a bilingual dataset of English and Hindi sentences
It calculates word counts for both languages and filters sentences that have
between 5 and 50 words in each language and where the difference in word count
is between -10 and +10
Output file cleaned_dataset_assignment1.xlsx contains the filtered data

To run
python assignment1_processing.py

Input file required
English_Hindi_Dataset.csv

Output file
cleaned_dataset_assignment1.xlsx

Assignment 2
This script translates 100 English sentences into Hindi using a Hugging Face model
It uses the Helsinki NLP opus mt en hi model and saves the model generated translations

To run
python assignment2_translation.py

Input file required
assignment2_sample_100.xlsx

Output files
translations_assignment2.xlsx
translations.txt

If a column named Reference Hindi is added to the input Excel file
the script also calculates BLEU CHRF and TER metrics and saves them in scores.txt

Dependencies
pandas
openpyxl
torch
transformers
sentencepiece
sacrebleu

Install dependencies
pip install transformers[sentencepiece] torch sacrebleu pandas openpyxl

<img width="727" height="89" alt="image" src="https://github.com/user-attachments/assets/7b2280e5-bd69-4f6b-b5bf-cd340c403813" />

<img width="751" height="239" alt="image" src="https://github.com/user-attachments/assets/4863af5c-063b-4387-89c1-f073c2df0a3f" />
