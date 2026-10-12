QUESTIONS = [
    {"question": "When do housing lottery numbers come out?", "expects": "second week of March"},
    {"question": "How much does a wash cost at Morrow House laundry?", "expects": "$1.50"},
    {"question": "What happens to dining dollars that are left over in May?", "expects": "disappear"},
    {"question": "How much of the CS 210 grade are the labs worth?", "expects": "10%"},
    {"question": "If I drop a course in week four, what shows up on my transcript?", "expects": "W"},
]

OUT_OF_SCOPE = [
    "What is the capital of Mongolia?",
    "How do I change the oil in a diesel engine?",
    "Who won the 1994 World Cup?",
    "What is the recommended dosage of ibuprofen for a headache?",
    "How do I write a for loop in Rust?",
]


def answered() -> list[dict]:
    return [q for q in QUESTIONS if q.get("question", "").strip()]
