from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="grammarticle",
    version="1.0.0",
    description="Grammarticle spaCy pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="upunaprosk",
    author_email="",
    url="https://github.com/upunaprosk/grammarticle",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=False,
    install_requires=[
        "spacy>=3.8.5,<3.9.0",
        "spacy-transformers>=1.3.8,<1.4.0",
        "spacy-huggingface-hub==0.0.10"
    ],
    entry_points={
        "spacy_pipelines": [
            "grammarticle = grammarticle.loader:load_model"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.7",
)