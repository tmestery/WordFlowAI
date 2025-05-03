# WordFlowAI

An AI app for next-word prediction using Markov Chains.

## 1. Set up a Virtual Environment

To avoid any dependency issues, it's recommended to create a virtual environment for your project.

* **Create a virtual environment**:

  ```
  python -m venv venv
  ```

* **Activate the virtual environment**:

  * On Windows:

    ```
    .\venv\Scripts\activate
    ```
  * On Mac/Linux:

    ```
    source venv/bin/activate
    ```

* **Deactivate the virtual environment** when you're done:

  ```
  deactivate
  ```

## 2. Install Python libraries:

* `nltk` and `spaCy` to help split text into words and clean it.
* `collections.Counter` to count how often word pairs appear.
