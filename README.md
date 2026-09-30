# The Unofficial Guide

Swagat Khot — corpus: campus_life

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does
"I built a system that answers questions about campus life. It uses the campus_life corpus: 88 short posts from students about classes, dorms, campus jobs, orientation and admin stuff like study abroad and parking. You ask it something like "how much work is Econ 101 outside of class?" and it finds the posts that talk about that, then writes an answer and tells you which post it got it from. If you ask something that has nothing to do with campus, like who won the World Cup, it just says it doesn't know instead of making something up."

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size:** one whole post per chunk (the longest post is 554 characters)
**Overlap:** 0

When I ran the starter chunker, it made 88 chunks from 88 posts, so it never split anything. My posts are short (183 to 554 characters), and when I read them, each one covers a single topic: one course, one dorm, one deadline. Splitting them would separate facts from what they're about. For example, "4 minutes" could end up in a different chunk from "Aldridge Hall." So I rewrote `split_documents` to keep each post as one chunk. I first set CHUNK_SIZE to 600 in config.py to fit the longest post, then decided to keep posts whole directly in the code, so overlap doesn't matter because nothing is split.

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->


## Sample Chunks

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_biol_160.txt#0` — produced by: `chunker.py::split_documents`

```
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::split_documents`

```
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::split_documents`

```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_innisfree_hall.txt#0` — produced by: `chunker.py::split_documents`

```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**when does application open for study abroad

**Answer:**Applications for study abroad open in October for the following academic year (admin_study_abroad.txt).

```
```

**My relevance cutoff:** 0.6

My five real questions had best distances between 0.25 and 0.44. My five off-topic questions were between 0.82 and 0.93. So there's a wide gap from 0.44 to 0.82 with no overlap, and 0.6 sits in it with room on both sides.

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| when does application open for study abroad | Yes | 0.2474 |
| how much econ 101 work outside of class | Yes | 0.3951 |
| whats the maximum hours a week i can work on campus | Yes | 0.3618 |
| how much actually matters in orientation week | Yes | 0.3629 |
| how much time from Aldridge Hall to the science quad | Yes | 0.4353 |
| What is the capital of Mongolia? | No | 0.8246 |
| How do I change the oil in a diesel engine? | No | 0.9340 |
| Who won the 1994 World Cup? | No | 0.8859 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8442 |
| How do I write a for loop in Rust? | No | 0.8960 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** I asked Claude to look at how long my documents were so I could pick a chunk size. It found that my posts range from 183 to 554 characters, about 320 on average. I first tried 560 to fit the longest post, but Claude pointed out that with 120 overlap, the chunker would still create small duplicate chunks from the ends of my longer posts. So I set the size to 600 to leave some room, and changed the overlap to 0, since each post is one chunk and nothing gets split.

**2.** I asked Claude to write the function that splits my documents. It first gave me a complicated version that split long posts by paragraph, which I undid because I didn't need it. Then I asked for a simple version that keeps each post as one chunk. I checked that it set `produced_by` to `chunker.py::split_documents` so my README's Sample Chunks would match the code, and I confirmed it still produced 88 chunks..

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Answer chunk also names what it's about | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Answer contains the expects phrase | 4 of 5 | 5/5 | 4/5 | 5/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

Full log: `results/run_2026-09-29_2015_before.md`, produced by `run_eval.py::main`. Chunks from `chunker.py::split_documents`, retrieval by `store.py::search`, answers by `generate.py::answer_from_chunks`, pass/fail by `scorer.py::judge`.

**Criterion 1: retrieved chunk contains the answer (Aldridge question, run 1).** The file with the answer, `transit_walking.txt`, was retrieved, but ranked below the dorm post:

```
- Best distance: 0.4353 (passed the gate)
- Sources retrieved: dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, housing_aldridge_hall.txt, housing_aldridge_hall_noise.txt, transit_walking.txt
```

**Criterion 2: every answer names a source (work hours question, run 2).**

```
The maximum is 20 hours a week during the term. 

Source: money_jobs.txt
```

**Criterion 3: gate stops out-of-corpus questions** (`run_eval.py::check_out_of_scope`, cutoff 0.6, refused 5 of 5):

```
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.896 | refused |
```

**Criterion 4: answer chunk also names what it's about (Aldridge question).** The answer came from a whole-post chunk where the place and the time are in the same line:

```
It takes 4 minutes to get from Aldridge Hall to the science quad. 

Source documents: `housing_aldridge_hall.txt` and `transit_walking.txt`
```

**Criterion 5: answer contains the expects phrase (Aldridge question, run 2, the one fail).** Expected "4 minutes"; the answer spelled it out:

```
It takes four minutes to get from Aldridge Hall to the science quad (from **housing_aldridge_hall.txt** and **transit_walking.txt**).
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | All 5 questions retrieved a file containing the answer in all 3 runs (5/5 each time, target 4 of 5). For Aldridge, transit_walking.txt ranked 5th, but housing_aldridge_hall.txt also says "four minutes", so the answer was in the top result too. |
| 2 | Every answer names a source | MET | All 15 answers named at least one .txt file (5/5 in every run, target 5 of 5). |
| 3 | Gate stops out-of-corpus questions | MET | All 5 off-topic questions were refused (5/5). The closest was 0.825, well above my 0.6 cutoff. |
| 4 | Answer chunk also names what it's about | MET | 5/5 in every run. Each post is one chunk, so the answer and its topic were always together, e.g. "Aldridge Hall to the science quad: 4 minutes" is in one chunk. |
| 5 | Answer contains the expects phrase | MET (close) | Runs were 5/5, 4/5, 5/5, so every run reached 4 of 5. The one fail was Aldridge in run 2: the answer said "four minutes" instead of "4 minutes". The answer was correct, but my scorer only matches the exact phrase. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->
I missed nothing: all five criteria were met in all three runs. That probably means my targets were safe, not that my system is excellent.

**The one close call (criterion 5, Aldridge question, run 2).** Stage: generation, then measurement. Two retrieved posts state the same fact in different forms. transit_walking.txt says "4 minutes" and housing_aldridge_hall.txt says "four minutes to a 9am lab". In run 2 the model used the dorm post's wording, and scorer.py::judge only checks for the exact text "4 minutes", so a correct answer was marked as a fail. The problem is my measurement: my expects phrase only matched one of the two posts that contain the answer.

**Pattern.** My targets were set low. Every question has one short post that answers it directly, and because each post is one chunk, criterion 4 could not fail at all. My off-topic questions were also too easy: the closest one was 0.825, far above my 0.6 cutoff.

**What I'd tighten:**
- Criterion 1, to "for 5 of 5 questions, the top-ranked chunk contains the answer." This would fail: for Econ 101, the #1 result was course_econ_101_exams.txt, which doesn't mention "4 hours". The posts that do came #2 and #3.
- Criterion 3, to use near-miss campus questions my posts don't answer (like "what time does the gym open?") instead of questions from completely different subjects. Those would land much closer to my 0.6 cutoff and actually test the gate.

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
