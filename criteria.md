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

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
I'm not aiming for 5 of 5 because of my Aldridge Hall question. There are three documents with  in the title ,but the walking time is  in transit_walking.txt. Those dorm documents could push the right chunk out of the top 5. The other four questions each have one clear document on the topic, so missing more than one would mean retrieval itself is broken

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
Every chunk is labeled with its file name, so all 5 answers should name one

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.



**Why this target:**
My out-of-scope questions have nothing to do with campus life, so they should come back far from every chunk and get refused. 

---

## 4. Something about your chunks

For at least 4 of my 5 test questions, the chunk that contains the answer also names what the answer is about.


**Why this target:**

My posts are short (183–554 characters) and each post is one chunk, so most answers can't be split away from their topic. But transit_walking.txt lists several routes in a row, and my retrieval showed dorm posts outranking it for the Aldridge question. If a chunk ever held "4 minutes" without "Aldridge Hall," the model couldn't tell which walk it was.

---

## 5. Your choice

For at least 4 of my 5 test questions, the system's answer contains the expects phrase I wrote in questions.py.
    


**Why this target:**

Retrieving the right chunk doesn't guarantee the model uses it correctly. It could round a number, mix up two facts, or answer too vaguely

---

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
> **Revised in unit 2:** For at least 4 of my 5 test questions, the system's answer states the same fact as my expects phrase, counting numbers written as words (e.g. "four minutes" = "4 minutes") as a match.
>
> **Why revised:** In run 2, the Aldridge answer said "four minutes" and my scorer marked it as a fail even though it was correct. The original criterion measured whether the model used my exact wording, not whether it got the fact right.
