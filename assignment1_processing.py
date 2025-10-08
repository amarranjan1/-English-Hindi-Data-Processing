

import pandas as pd

def word_count(text: str) -> int:
    
    if pd.isna(text):
        return 0
    return len(str(text).split())

def main():
    
    df = pd.read_csv("English_Hindi_Dataset.csv", encoding="utf-8-sig")
    print(f"Loaded dataset with {len(df)} rows.")

  
    df["Word Count (English)"] = df["English"].apply(word_count)
    df["Word Count (Hindi)"] = df["Hindi"].apply(word_count)
    df["Difference (EN - HI)"] = df["Word Count (English)"] - df["Word Count (Hindi)"]

 
    mask = (
        df["Word Count (English)"].between(5, 50)
        & df["Word Count (Hindi)"].between(5, 50)
        & df["Difference (EN - HI)"].between(-10, 10)
    )
    filtered = df[mask].reset_index(drop=True)
    print(f"Filtered dataset: {len(filtered)} rows remaining after applying conditions.")

   
    filtered.to_excel("cleaned_dataset_assignment1.xlsx", index=False)


if __name__ == "__main__":
    main()
