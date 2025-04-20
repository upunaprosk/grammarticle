import spacy
from huggingface_hub import snapshot_download

def load_model():
    model_dir = snapshot_download("iproskurina/en_grammarticle")
    return spacy.load(model_dir)