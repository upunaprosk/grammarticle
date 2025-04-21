import argparse
import logging
import spacy
import grammarticle

logging.basicConfig(
    format="%(asctime)s — %(levelname)s — %(message)s",
    level=logging.INFO
)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <style>
    body {
      font-family: "Segoe UI", Helvetica, sans-serif;
      line-height: 1.6;
      max-width: 900px;
      margin: 20px auto;
      background: #fafafa;
      color: #333;
    }
    mark {
      padding: 0.15em 0.35em;
      border-radius: 4px;
      font-weight: bold;
    }
    .redundant { background-color: #fff3cd; }
    .wrong { background-color: #f8d7da; }
    .missing { background-color: #cce5ff; }
    .label {
      font-size: 0.75em;
      font-weight: bold;
      margin-left: 4px;
      vertical-align: super;
      color: #666;
    }
  </style>
</head>
<body>
  {{BODY}}
</body>
</html>
"""


def render_html_body(doc, span_key="sc"):
    span_map = {span.start: span for span in doc.spans.get(span_key, [])}
    output = []
    for i, token in enumerate(doc):
        if i in span_map:
            span = span_map[i]
            label = span.label_.lower()
            span_text = " ".join(tok.text_with_ws for tok in span)
            html = f'<mark class="{label}">{span_text.strip()}</mark><span class="label">{span.label_}</span>'
            output.append(html)
            for j in range(span.start + 1, span.end):
                output.append("")
        elif not any(s.start < i < s.end for s in doc.spans.get(span_key, [])):
            output.append(token.text_with_ws)
    return "<p>" + "".join(output).strip() + "</p>"


def main():
    parser = argparse.ArgumentParser(description="Render a text with article error annotations to HTML.")
    parser.add_argument("input", help="Input .txt file")
    parser.add_argument("output", help="Output .html file")
    args = parser.parse_args()

    logging.info("Loading grammarticle pipeline...")
    nlp = grammarticle.load()

    logging.info(f"Reading input from {args.input}")
    with open(args.input, "r", encoding="utf-8") as f:
        text = f.read()

    doc = nlp(text)

    logging.info("Rendering HTML...")
    body_html = render_html_body(doc, span_key='sc')
    full_html = HTML_TEMPLATE.replace("{{BODY}}", body_html)

    logging.info(f"Saving to {args.output}")
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(full_html)


if __name__ == "__main__":
    main()
