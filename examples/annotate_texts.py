import argparse
import logging
import spacy
import grammarticle

logging.basicConfig(
    format="%(asctime)s — %(levelname)s — %(message)s",
    level=logging.INFO
)


def main():
    parser = argparse.ArgumentParser(description="Detects article errors in texts from the input and saves annotations.")
    parser.add_argument("input", help="Input .txt file")
    parser.add_argument("output", help="Output .tsv or .txt file")
    args = parser.parse_args()

    logging.info("Loading pipeline...")
    nlp = grammarticle.load()

    logging.info(f"Reading input from {args.input}")
    with open(args.input, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    logging.info(f"Processing {len(lines)} lines")
    with open(args.output, "w", encoding="utf-8") as out:
        out.write("line\tlabel\ttext\tstart\tend\n")
        for i, line in enumerate(lines):
            doc = nlp(line)
            for span in doc.spans.get('sc', []):
                out.write(f"{i+1}\t{span.label_}\t{span.text}\t{span.start_char}\t{span.end_char}\n")

    logging.info(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
