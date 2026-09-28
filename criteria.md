# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.


## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
All five of my test questions came back with distances well under my cutoff
(0.18–0.34), so I expect this to hold most of the time. I'm not setting 5 of
5 because a rarer topic in my corpus could still come back weaker on a
different day, and I'd rather have room to miss once than call it broken for
a single fluke.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
The grounding prompt requires the model to always cite a source, and every
test answer I've seen so far has done this without exception. I'm setting
5 of 5 rather than 4 of 5 because this isn't really a retrieval-quality
question — it's whether the model follows a simple instruction — so I expect
it to hold unless the gate itself misfires.

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
<!-- What did your distances look like when you set the cutoff in Milestone 4?
     Was there a clean gap, or did the two groups overlap? -->

---

## 4. Chunks are answerable on their own

If I sample 10 chunks at random from across the corpus, at least 8 of them
should be answerable using only that chunk's own text, with no need for
what comes before or after.

**Why this target:**
My first sample of 5 came out 3/5. Two of those failures were about missing
context or merged topics, not something structurally broken — but 5 chunks
is too small a sample to trust. I'm sampling 10 for a steadier read, and
setting 8 as a stretch above my first result.


## 5. Answers return quickly

For at least 4 of my 5 test questions, `ask` returns a complete answer in
under 8 seconds.

**Why this target:**
Even during a Gemini outage, retrieval and embedding alone took 2.3–4.8
seconds per question, before the model call even started. 8 seconds gives
real room for the model's response time on top of that, without being so
loose that a genuinely slow answer would still pass.



<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
