# WordFlowAI

An AI app for next-word prediction using Markov Chains.

---

## 1. Set up a Virtual Environment

* **Create a virtual environment**:

  ```bash
  python -m venv venv
  ```

* **Activate the virtual environment**:

  * On **Windows**:

    ```bash
    .\venv\Scripts\activate
    ```
  * On **Mac/Linux**:

    ```bash
    source venv/bin/activate
    ```

* **Deactivate the virtual environment** when you're done:

  ```bash
  deactivate
  ```

---

## 2. Install Python libraries

* Install all dependencies listed in `requirements.txt`:

  ```bash
  pip install -r requirements.txt
  ```

* Libraries used include:

  * `nltk` and `spaCy` — for tokenization and text cleaning
  * `collections.Counter` — for counting word pair frequencies

---

## 3. Notes

Make sure to download necessary data for `nltk` or `spaCy` after installation if needed:

```python
import nltk
nltk.download('punkt')
```

For `spaCy`, you might also need to run:

```bash
python -m spacy download en_core_web_sm
```
