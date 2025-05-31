#  Multilingual Language Detection and Translation System using Multinomial Naive Bayes

This repository provides a lightweight and efficient **language detection and translation system** that uses the **Multinomial Naive Bayes** algorithm to classify the language of a given text and then translate it into a user-defined target language using external APIs.

---

## Key Features

-  Detects language of a given text from multiple supported languages.
-  Uses Multinomial Naive Bayes for fast and accurate text classification.
-  Translates detected text into the selected target language using `googletrans` or similar APIs.
-  Simple and extensible architecture for academic or lightweight production use.

---


---

##  Supported Languages

The current model supports detection of:

- English
- French
- Spanish
- German
- Hindi
- Arabic
- Chinese
- Russian
- Italian
- Portuguese

(You can extend this list by adding more training samples.)

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/language-detection-translation.git
cd language-detection-translation

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

Train the Model
python train_model.py

Detect and Translate (CLI)
python app/detect_translate.py --text "Bonjour tout le monde" --target_lang "en"

```

Output:
Detected Language: French
Translation: Hello everyone

Evaluation
-Accuracy: ~95% on short sentences.
-Tested with common phrases, greetings, and basic paragraphs.

Acknowledgments
-Scikit-learn
-Google Translate API (unofficial)
-Sample datasets from Tatoeba, Wikipedia



