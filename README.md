# Book Web Library Application (BookBox)

A Python and Streamlit project for organising a personal reading library. Books are represented as objects and saved locally in JSON so changes persist between sessions.

## Current features

- Separate views for books you want to read, are currently reading, and have read.
- Update reading status, add reviews, and rate started or completed books in half-star steps.
- Sort by title, recently added, or rating, depending on the view.
- Search by title and filter by genre, status, or minimum rating through the Python `Library` class.
- Recover from missing data files and preserve malformed JSON as a backup.

## Run locally

Use Python 3.10 or newer. From the project folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run website.py
```

On Windows, activate the environment with `.venv\Scripts\activate` instead.

The app starts with an empty library if `storage.json` is missing. To try it with the original sample books, run `python -m examples.library_demo` from the project folder before launching Streamlit. Only run the demo if you are happy to replace any existing `storage.json`.

The current interface edits existing books. Adding and removing books is available through the Python classes, with an interface planned as future work.

## Project layout

| File | Purpose |
| --- | --- |
| `library.py` | Book and Library classes, rating rules, search, and filtering |
| `storage.py` | JSON saving, loading, and malformed-file recovery |
| `website.py` | Streamlit interface |
| `examples/library_demo.py` | Original sample library and JSON round trip |
| `.streamlit/config.toml` | Interface theme |

## Development notes

This is an ongoing learning project covering Python classes, JSON persistence, error handling, and web interfaces. AI assistance was used for parts of the Streamlit layout and presentation.

Data is stored in `storage.json` in the folder you launch Streamlit from. The file is excluded from Git. This is a local, single-library prototype: there are no accounts, per-user storage, or concurrent-write protection. AI recommendations are a future idea and are not implemented.
