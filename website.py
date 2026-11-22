import streamlit as st

from storage import load_library, save_library

# Must be the first Streamlit command: browser tab title, icon and a wide layout
st.set_page_config(page_title="BookBox", page_icon="📚", layout="wide")

STATUSES = ["want to read", "currently reading", "read"]
RATINGS = ["No rating"] + [i / 2 for i in range(1, 11)]

# How each stored status is shown on the page
STATUS_LABELS = {
    "want to read": "Want to Read",
    "currently reading": "Currently Reading",
    "read": "Read",
}

CARDS_PER_ROW = 3


def stars(rating):
    """Turn a rating like 4.5 into '★★★★☆  4.5'."""
    full = int(rating)
    return "★" * full + "☆" * (5 - full) + f"  {rating:g}"


def show_book(book, library, key):
    with st.container(border=True):

        # --- What the card shows ---
        st.subheader(book.title)
        st.caption(f"{book.author} · {book.genre} · {STATUS_LABELS[book.status]}")

        if book.rating is not None:
            st.markdown(stars(book.rating))
        else:
            st.caption("Not rated yet")

        if book.review is not None:
            st.write(book.review)

        # --- The update form, tucked away until it's needed ---
        with st.expander("Update"):
            with st.form(key=f"form_{key}"):
                new_status = st.selectbox(
                    "Status",
                    STATUSES,
                    index=STATUSES.index(book.status),
                    format_func=lambda s: STATUS_LABELS[s],
                    key=f"status_{key}",
                )
                new_rating = "No rating"
                new_review = None

                if book.status != "want to read":
                    if book.rating is not None:
                        start = book.rating
                    else:
                        start = "No rating"
                    new_rating = st.select_slider("Rating", RATINGS, value=start, key=f"rating_{key}")

                    if book.review is not None:
                        start_review = book.review
                    else:
                        start_review = ""
                    new_review = st.text_area("Review", value=start_review, key=f"review_{key}")

                saved = st.form_submit_button("Save")

        if saved:
            book.update_status(new_status)
            if new_rating != "No rating":
                book.set_rating(new_rating)
            if new_review is not None:
                cleaned = new_review.strip()
                if cleaned == "":
                    book.write_review(None)
                else:
                    book.write_review(cleaned)

            save_library(library, "storage.json")
            st.rerun()


main_library = load_library("storage.json")

# --- Header ---
st.title("📚 BookBox")
st.caption("Your personal reading library")

tab_statuses = ["currently reading", "want to read", "read"]

# --- A count of books in each section ---
metric_cols = st.columns(3)
for col, status in zip(metric_cols, tab_statuses):
    col.metric(STATUS_LABELS[status], len(main_library.filter_by_status(status)))

st.divider()

# --- One tab per status ---
tabs = st.tabs([STATUS_LABELS[s] for s in tab_statuses])

for tab, status in zip(tabs, tab_statuses):
    with tab:
        books = main_library.filter_by_status(status)

        if not books:
            st.info("No books here yet.")
        else:
            tab_options = ["Recently added", "Title A-Z"]
            if status != "want to read":
                tab_options += ["Rating"]

            # A narrow column so the dropdown doesn't stretch across the whole page
            sort_col, _ = st.columns([1, 3])
            sort_choice = sort_col.selectbox("Sort by", tab_options, key=f"sort_{status}")

            if sort_choice == "Recently added":
                books = books[::-1]
            elif sort_choice == "Title A-Z":
                books = sorted(books, key=lambda b: b.title.lower())
            elif sort_choice == "Rating":
                books = sorted(books, reverse=True, key=lambda b: b.rating if b.rating is not None else 0)

            # Cards in a grid: book 0 goes in column 0, book 1 in column 1, book 3 back in column 0...
            cols = st.columns(CARDS_PER_ROW)
            for position, book in enumerate(books):
                with cols[position % CARDS_PER_ROW]:
                    show_book(book, main_library, main_library.books.index(book))
