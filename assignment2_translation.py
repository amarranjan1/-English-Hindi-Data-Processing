
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import sacrebleu
import torch

def translate_batch(sentences, tokenizer, model, device="cpu", max_length=256):
    """Translate a batch of sentences using a Seq2Seq model."""
    inputs = tokenizer(sentences, return_tensors="pt", padding=True, truncation=True).to(device)
    outputs = model.generate(**inputs, max_length=max_length, num_beams=4)
    decoded = [tokenizer.decode(t, skip_special_tokens=True) for t in outputs]
    return decoded

def main():
   
    input_file = "assignment2_sample_100.xlsx"
    df = pd.read_excel(input_file)
    sentences = df["Original English sentence"].astype(str).tolist()

    
    model_name = "Helsinki-NLP/opus-mt-en-hi"
    print(f"Loading translation model: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    
    batch_size = 16
    translations = []
    for i in range(0, len(sentences), batch_size):
        batch = sentences[i:i+batch_size]
        trans = translate_batch(batch, tokenizer, model, device)
        translations.extend(trans)
        print(f"Translated {min(i+batch_size, len(sentences))}/{len(sentences)} sentences...")

   
    df["Model-generated Hindi translation"] = translations
    df.to_excel("translations_assignment2.xlsx", index=False)
    pd.Series(translations).to_csv("translations.txt", index=False, header=False)
    print(" Translations saved to 'translations_assignment2.xlsx' and 'translations.txt'.")

    
    if "Reference Hindi" in df.columns:
        refs = df["Reference Hindi"].astype(str).tolist()
        hyps = translations
        bleu = sacrebleu.corpus_bleu(hyps, [refs])
        chrf = sacrebleu.corpus_chrf(hyps, [refs])
        ter = sacrebleu.corpus_ter(hyps, [refs])

        with open("scores.txt", "w", encoding="utf-8") as f:
            f.write(f"BLEU: {bleu.score:.2f}\n")
            f.write(f"CHRF: {chrf.score:.2f}\n")
            f.write(f"TER: {ter.score:.2f}\n")

        print(f"Evaluation metrics saved to 'scores.txt'")
    else:
        print(" No 'Reference Hindi' column found — skipped metric evaluation.")

if __name__ == "__main__":
    main()
