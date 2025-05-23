# Grammarticle

<img src="https://raw.githubusercontent.com/upunaprosk/grammarticle/master/logo.png" alt="GrammArticle Logo" width="150" align="right" />

GrammArticle is a RoBERTa-based grammar checker for English article usage. It detects three types of article errors:

1) Missing – when an article is absent but required
2) Wrong – when an incorrect article is used (e.g., "a apple" instead of "an apple", or "the" instead of "a/an")
3) Redundant – when an article is unnecessary (e.g., "the furniture")



## Installation

GrammArticle is trained on publicly available GEC datasets with synthetic augmentation and is available as a SpaCy pipeline.

`pip install grammarticle`

or

```bash
pip install spacy-transformers
python -m spacy download en_core_web_trf
pip install https://huggingface.co/iproskurina/en_grammarticle/resolve/main/en_grammarticle-1-py3-none-any.whl

```

## Usage

```
import grammarticle
nlp = grammarticle.load()
text = "This is sentence"
doc = nlp(text)
for span in doc.spans.get("sc", []): 
    print(f"[{span.label_}] {span.text}")
```

Outputs:
```
[Missing] sentence
```
___

Easy-to-use examples can be found in the `/examples` folder:  
`annotate_texts.py` for text annotation and `html_render.py` for HTML highlighting (see example below).

![Example Output](https://raw.githubusercontent.com/upunaprosk/grammarticle/master/example.png)

___
