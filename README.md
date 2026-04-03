# LLM-Shield: Data Masking Pipeline for LLM Inputs

LLM-Shield is a high-performance, privacy-focused pipeline designed to sanitize user prompts before they reach Large Language Models (LLMs). It automatically detects and masks Personally Identifiable Information (PII) to prevent data leakage and ensure compliance with privacy regulations like GDPR and CCPA.

---

## 🚀 Features

- **Robust PII Detection**: Powered by [Microsoft Presidio](https://microsoft.github.io/presidio/) for state-of-the-art entity recognition.
- **Support for Multiple Entities**: Masks Names, Emails, Phone Numbers, Credit Cards, IP Addresses, and more.
- **RESTful API**: Built with **FastAPI** for seamless integration into existing AI workflows.
- **Customizable Masking**: Choose between standard placeholders (e.g., `<PERSON>`) or synthetic data.

---

## 🏗️ Architecture

1.  **Input**: Raw user prompt (e.g., "Hello, my name is John Doe and my email is john@example.com").
2.  **Analyzer**: Microsoft Presidio identifies sensitive entities using a combination of NLP models and rule-based detectors.
3.  **Anonymizer**: Replaces identified entities with descriptive placeholders.
4.  **Output**: Sanitized prompt ready for LLM consumption.

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- Python 3.10+
- `pip`

### 2. Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_lg
```

### 3. Run the API
```bash
uvicorn src.main:app --reload
```

---

## 📡 API Usage

### Mask Prompt
**POST** `/mask`
```json
{
  "text": "Call me at 555-0199 or email user@example.com"
}
```

**Response**
```json
{
  "masked_text": "Call me at <PHONE_NUMBER> or email <EMAIL_ADDRESS>",
  "entities_found": ["PHONE_NUMBER", "EMAIL_ADDRESS"]
}
```

