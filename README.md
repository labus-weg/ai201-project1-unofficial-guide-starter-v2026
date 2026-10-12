# The Unofficial Guide

Nafisa Nawrin Labonno — campus_life corpus

The Unofficial Guide answers plain questions about student life from a corpus of 88 short posts: housing, dining, courses, campus services, and administrative rules. It retrieves the closest chunks from a local vector store and has the model answer using only those, naming the source file. A relevance gate refuses questions that are too far from anything in the documents, instead of letting the model guess.

---

# Unit 1

## What This Does

<!-- Fill in: 3-4 sentences on your corpus and the kinds of questions your
     system answers, written for someone who's never seen this repo. -->

## Chunking Strategy

**Chunk size:** no fixed size — split on paragraph breaks
**Overlap:** none

Most documents in campus_life are short (~317 chars avg) and read like two
ideas glued together: a one-line title, then one or two paragraphs each
covering a separate fact. The starter's 800-char window never even triggered
on these, so I switched to splitting on blank lines instead.

One problem with a pure paragraph split: some documents have a short title
line or a short trailing paragraph, and either would become its own
near-empty chunk. So I set a 60-character floor — anything under that gets
merged into the next paragraph (or the previous one, if it's the last piece
in the doc).

Result: 88 docs -> 177 chunks, avg 156 chars (shortest 61, longest 397).

## Sample Chunks

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a
longer window — through the end of week six — but a drop after week two
shows as a W on your transcript. Nothing anywhere on the registrar's site
says this plainly, and students find out from each other.
```

Stands on its own fine.

**Chunk 2** — source: `course_cs_340_exams.txt#1` — produced by: `chunker.py::split_documents`

```
Start the term project in week three, not week eight; everyone learns this
the hard way.
```

Doesn't name CS 340 anywhere in the text — you only know the class from the
source tag the pipeline attaches, not the chunk itself. Minor gap in short,
title-less tail chunks.

**Chunk 3** — source: `course_stat_150.txt#0` — produced by: `chunker.py::split_documents`

```
STAT 150 Applied Statistics

Transferred in last year, so take this with a grain of salt. Format is
flipped: watch the recordings, class time is problem sets. Assessment:
three equally weighted midterms, no final. No curve, but the lowest
midterm is dropped.
```

Packed but one topic, coherent.

**Chunk 4** — source: `health_center.txt#1` — produced by: `chunker.py::split_documents`

```
Counselling is separate, in the same building, and has its own intake
process with a shorter wait than people expect — usually three or four
days for a first session.
```

Clean, answers a specific question on its own.

**Chunk 5** — source: `housing_morrow_house.txt#3` — produced by: `chunker.py::split_documents`

```
Laundry costs $1.50 wash, $1.25 dry, coin or card. On noise: loud until
about 1am on weekends, no enforced quiet hours.
```

Two unrelated facts merged here because the laundry line alone was under
60 characters. Both still read fine, but a noise question will also pull
back laundry pricing. Real cost of the merge approach, not a bug.

## Sample Answer

Question: How much does a dryer cost in Fenwick Court?
Answer: Based on housing_fenwick_court_laundry.txt, a dryer in Fenwick Court costs $1.75.

My relevance cutoff: 0.6. In-scope questions landed at 0.18-0.34 and out-of-scope at 0.79-0.92, with no overlap.

| Question | In corpus? | Best distance |
|---|---|---|
| CS 210 lab percentage | Yes | 0.342 |
| Kestrel Commons salad bar | Yes | 0.259 |
| Fenwick Court dryer cost | Yes | 0.280 |
| Campus store price-match | Yes | 0.294 |
| Weekend shuttle frequency | Yes | 0.180 |
| Capital of Mongolia | No | 0.787 |
| Diesel oil change | No | 0.923 |
| 1994 World Cup | No | 0.847 |
| Ibuprofen dosage | No | 0.824 |
| Rust for loop | No | 0.877 |


## How I Used AI

1. My push was rejected and a rebase conflicted with questions I wrote last week. I pasted the error into Claude and asked what to do. It told me not to overwrite anything until we checked who wrote the remote's questions. I confirmed they were mine, aborted the rebase, and reset to my remote, which kept my work.

2. I asked Claude for a command that prints the best distance for all ten questions at once. Its first draft used questions it had invented instead of mine, so I reran it using the list in questions.py, and re-indexed with my chunker so the numbers matched my 177 chunks.
---

# Unit 2

## Run Log — Before

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

## The Improvement

**What I changed:**

**Why I picked it:**

### Run Log — After

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

## What's Still Broken

## What I'd Do Differently
