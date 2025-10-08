
import pandas as pd


df = pd.read_excel("cleaned_dataset_assignment1.xlsx")


sample = df.sample(n=100, random_state=42).reset_index(drop=True)


sample_out = pd.DataFrame({
    "Original English sentence": sample["English"],
    "Model-generated Hindi translation": ["" for _ in range(len(sample))]
})


sample_out.to_excel("assignment2_sample_100.xlsx", index=False)

print("assignment2_sample_100.xlsx created successfully!")
