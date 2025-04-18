<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="readmeai/assets/logos/purple.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# SMARTER_SPELLING_PRACTICE

<em>Master spelling.  Effortlessly.  Intelligently.</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/dev-ansh-r/Smarter_spelling_practice?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/dev-ansh-r/Smarter_spelling_practice?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/dev-ansh-r/Smarter_spelling_practice?style=default&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/dev-ansh-r/Smarter_spelling_practice?style=default&color=0080ff" alt="repo-language-count">

<!-- default option, no dependency badges. -->


<!-- default option, no dependency badges. -->

</div>
<br>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

Smarter_spelling_practice is a Python application designed for building efficient and engaging spelling practice tools. It combines optical character recognition, an AI-powered feedback mechanism, and a spaced repetition system for optimal learning.

**Why Smarter_spelling_practice?**

This project streamlines the development of robust spelling practice applications. The core features include:

- **🟨 OCR Integration:**  Automatically extracts words from images using EasyOCR and OpenCV, eliminating manual data entry.
- **🟩 AI-Powered Feedback:** Leverages Google's Gemini API for accurate spell-checking and insightful corrections.
- **🟦 Spaced Repetition System (SRS):** Optimizes learning through intelligent scheduling, maximizing retention.
- **🟪 Streamlit Dashboard:** Provides a user-friendly interface for progress tracking and interactive exercises.
- **🟥 SQLite Database:**  Ensures persistent data storage and management for seamless application functionality.
- **💜 Modular Design:**  Cleanly separated modules for OCR, AI, SRS, and database interaction promote maintainability and extensibility.

---

## Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Streamlit web app</li><li>Uses image processing (OpenCV) for handwritten word capture</li><li>OCR (EasyOCR) for text extraction</li><li>Simple UI for word input and feedback</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Code is relatively concise</li><li>Room for improvement in terms of error handling and modularity</li><li>Some functions could be better documented</li></ul> |
| 📄 | **Documentation** | <ul><li>Minimal documentation</li><li>README provides basic instructions</li><li>Lack of in-code comments in several places</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates EasyOCR for Optical Character Recognition</li><li>Integrates OpenCV for image processing</li><li>Uses Streamlit for the web application interface</li><li>Uses Pandas (likely for data handling, though not extensively shown)</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Could benefit from better separation of concerns</li><li>Some functions handle multiple tasks</li><li>Improved modularity would enhance testability and maintainability</li></ul> |
| 🧪 | **Testing**       | <ul><li>No dedicated test suite observed</li><li>Testing would improve code reliability</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Performance depends heavily on OCR and image processing speed</li><li>Potential for optimization, especially with larger images or datasets</li></ul> |
| 🛡️ | **Security**      | <ul><li>No apparent security vulnerabilities in this simple application</li><li>Security considerations would be more relevant with user data storage</li></ul> |
| 📦 | **Dependencies**  | <ul><li>EasyOCR</li><li>OpenCV-Python</li><li>Streamlit</li><li>Pandas</li></ul> |
| 🚀 | **Scalability**   | <ul><li>Currently not designed for scalability</li><li>Would require significant changes for handling a large number of users or data</li></ul> |

---

## Project Structure

```sh
└── Smarter_spelling_practice/
    ├── README.md
    ├── ai_helper
    │   └── gemma_wrapper.py
    ├── dashboard
    │   └── app.py
    ├── data
    │   └── user_db.sqlite
    ├── main.py
    ├── ocr_module
    │   └── reader.py
    ├── requirements.txt
    ├── sample_input.png
    ├── sample_input1.png
    ├── scripts
    │   ├── db_creator.py
    │   └── seed_dictionary.py
    ├── srs_engine
    │   └── sm2.py
    └── system_architecture.png
```

### Project Index

<details open>
    <summary><b><code>SMARTER_SPELLING_PRACTICE/</code></b></summary>
    <!-- __root__ Submodule -->
    <details>
        <summary><b>__root__</b></summary>
        <blockquote>
            <div class='directory-path' style='padding: 8px 0; color: #666;'>
                <code><b>⦿ __root__</b></code>
            <table style='width: 100%; border-collapse: collapse;'>
            <thead>
                <tr style='background-color: #f8f9fa;'>
                    <th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
                    <th style='text-align: left; padding: 8px;'>Summary</th>
                </tr>
            </thead>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='https://github.com/dev-ansh-r/Smarter_spelling_practice/blob/master/requirements.txt'>requirements.txt</a></b></td>
                    <td style='padding: 8px;'>- Streamlit for the user interface, Pandas for data manipulation, EasyOCR for optical character recognition, and OpenCV for image processing<br>- These libraries collectively support the applications core functionality.</td>
                </tr>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='https://github.com/dev-ansh-r/Smarter_spelling_practice/blob/master/main.py'>main.py</a></b></td>
                    <td style='padding: 8px;'>- Main.py` orchestrates the Smarter Spelling Practice application<br>- It integrates optical character recognition (OCR), a spaced repetition system (SRS) for vocabulary learning, an AI-powered feedback mechanism, and a user dashboard<br>- The script initializes the application and launches the dashboard, providing a user interface for interacting with the integrated components<br>- The commented-out code suggests functionalities for word validation, scheduling, and AI-assisted learning.</td>
                </tr>
            </table>
        </blockquote>
    </details>
    <!-- dashboard Submodule -->
    <details>
        <summary><b>dashboard</b></summary>
        <blockquote>
            <div class='directory-path' style='padding: 8px 0; color: #666;'>
                <code><b>⦿ dashboard</b></code>
            <table style='width: 100%; border-collapse: collapse;'>
            <thead>
                <tr style='background-color: #f8f9fa;'>
                    <th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
                    <th style='text-align: left; padding: 8px;'>Summary</th>
                </tr>
            </thead>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='https://github.com/dev-ansh-r/Smarter_spelling_practice/blob/master/dashboard/app.py'>app.py</a></b></td>
                    <td style='padding: 8px;'>- The <code>dashboard/app.py</code> script implements a Streamlit-based spelling practice application<br>- It provides a user interface with progress tracking and interactive spelling exercises<br>- The application uses OCR to extract words from uploaded images, leverages a spaced repetition system for scheduling practice, and integrates with an AI for feedback on misspelled words, storing progress in a local SQLite database.</td>
                </tr>
            </table>
        </blockquote>
    </details>
    <!-- scripts Submodule -->
    <details>
        <summary><b>scripts</b></summary>
        <blockquote>
            <div class='directory-path' style='padding: 8px 0; color: #666;'>
                <code><b>⦿ scripts</b></code>
            <table style='width: 100%; border-collapse: collapse;'>
            <thead>
                <tr style='background-color: #f8f9fa;'>
                    <th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
                    <th style='text-align: left; padding: 8px;'>Summary</th>
                </tr>
            </thead>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='https://github.com/dev-ansh-r/Smarter_spelling_practice/blob/master/scripts/seed_dictionary.py'>seed_dictionary.py</a></b></td>
                    <td style='padding: 8px;'>- The script populates a SQLite database with a word list downloaded from a specified URL<br>- It establishes a connection to the <code>user_db.sqlite</code> database within the <code>data</code> directory, creating a <code>dictionary</code> table if it doesnt exist<br>- The script then inserts each word, ensuring uniqueness and handling potential insertion errors<br>- Finally, it reports the number of words successfully added.</td>
                </tr>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='https://github.com/dev-ansh-r/Smarter_spelling_practice/blob/master/scripts/db_creator.py'>db_creator.py</a></b></td>
                    <td style='padding: 8px;'>- Db_creator.py<code> establishes the database schema for the application<br>- It creates an SQLite database named </code>user_db.sqlite` containing a table to log word learning progress, tracking repetitions, review intervals, easiness factors, and due dates<br>- This script ensures the database is ready for use by other parts of the application, facilitating data persistence and management within the projects data directory.</td>
                </tr>
            </table>
        </blockquote>
    </details>
    <!-- ocr_module Submodule -->
    <details>
        <summary><b>ocr_module</b></summary>
        <blockquote>
            <div class='directory-path' style='padding: 8px 0; color: #666;'>
                <code><b>⦿ ocr_module</b></code>
            <table style='width: 100%; border-collapse: collapse;'>
            <thead>
                <tr style='background-color: #f8f9fa;'>
                    <th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
                    <th style='text-align: left; padding: 8px;'>Summary</th>
                </tr>
            </thead>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='https://github.com/dev-ansh-r/Smarter_spelling_practice/blob/master/ocr_module/reader.py'>reader.py</a></b></td>
                    <td style='padding: 8px;'>- Reader.py` provides optical character recognition (OCR) functionality within the larger project<br>- It extracts the first word from an image using the pytesseract library<br>- This module likely serves as a component in a larger system that processes images, potentially for data extraction or indexing, contributing to the overall image processing pipeline.</td>
                </tr>
            </table>
        </blockquote>
    </details>
    <!-- ai_helper Submodule -->
    <details>
        <summary><b>ai_helper</b></summary>
        <blockquote>
            <div class='directory-path' style='padding: 8px 0; color: #666;'>
                <code><b>⦿ ai_helper</b></code>
            <table style='width: 100%; border-collapse: collapse;'>
            <thead>
                <tr style='background-color: #f8f9fa;'>
                    <th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
                    <th style='text-align: left; padding: 8px;'>Summary</th>
                </tr>
            </thead>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='https://github.com/dev-ansh-r/Smarter_spelling_practice/blob/master/ai_helper/gemma_wrapper.py'>gemma_wrapper.py</a></b></td>
                    <td style='padding: 8px;'>- Gemma_wrapper.py` facilitates interaction with Googles Gemini API<br>- It securely loads an API key from environment variables, then uses the Gemini API to check the spelling of a given word<br>- If misspelled, the API provides a correction and example sentence<br>- This module integrates Geminis capabilities into the broader application, providing spell-checking functionality.</td>
                </tr>
            </table>
        </blockquote>
    </details>
    <!-- srs_engine Submodule -->
    <details>
        <summary><b>srs_engine</b></summary>
        <blockquote>
            <div class='directory-path' style='padding: 8px 0; color: #666;'>
                <code><b>⦿ srs_engine</b></code>
            <table style='width: 100%; border-collapse: collapse;'>
            <thead>
                <tr style='background-color: #f8f9fa;'>
                    <th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
                    <th style='text-align: left; padding: 8px;'>Summary</th>
                </tr>
            </thead>
                <tr style='border-bottom: 1px solid #eee;'>
                    <td style='padding: 8px;'><b><a href='https://github.com/dev-ansh-r/Smarter_spelling_practice/blob/master/srs_engine/sm2.py'>sm2.py</a></b></td>
                    <td style='padding: 8px;'>- Sm2.py<code> manages a spaced repetition system (SRS) for vocabulary learning<br>- It updates word learning schedules based on user responses, adjusting repetition intervals and easiness factors<br>- The module interacts with a SQLite database (</code>data/user_db.sqlite`) storing word data, determining words due for review and validating word existence against a dictionary<br>- It provides functions for schedule updates and retrieval of due words.</td>
                </tr>
            </table>
        </blockquote>
    </details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip

### Installation

Build Smarter_spelling_practice from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/dev-ansh-r/Smarter_spelling_practice
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd Smarter_spelling_practice
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->

<!-- [![pip][pip-shield]][pip-link] -->
<!-- REFERENCE LINKS -->
<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
<!-- [pip-link]: https://pypi.org/project/pip/ -->

**Using [pip](https://pypi.org/project/pip/):**

```sh
❯ pip install -r requirements.txt
```

### Usage

Run the project with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
python {entrypoint}
```

### Testing

Smarter_spelling_practice uses the {__test_framework__} test framework. Run the test suite with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
pytest
```

---

## Contributing

- **💬 [Join the Discussions](https://github.com/dev-ansh-r/Smarter_spelling_practice/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/dev-ansh-r/Smarter_spelling_practice/issues)**: Submit bugs found or log feature requests for the `Smarter_spelling_practice` project.
- **💡 [Submit Pull Requests](https://github.com/dev-ansh-r/Smarter_spelling_practice/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/dev-ansh-r/Smarter_spelling_practice
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/dev-ansh-r/Smarter_spelling_practice/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=dev-ansh-r/Smarter_spelling_practice">
   </a>
</p>
</details>

---

## License

Smarter_spelling_practice is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
