"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "31adf7682a475731a2b348b4d35f2b83"
GRADE_HASH = "3c5472c2b032a5464c76c1ed6e0d35a807b014d9c125577ac19fbacdfca0631d"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
