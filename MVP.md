# Viva LTI Tool -- MVP Roadmap

## Rationale

The rapid rise of generative AI has transformed how students produce
academic work. Traditional text-based assessments are now vulnerable to
AI-assisted plagiarism, contract cheating, and ghostwriting.
Universities are struggling to evaluate whether submitted work genuinely
reflects a student's understanding.

A viva-style defence of work remains one of the strongest methods of
establishing ownership and comprehension---but vivas are
labour-intensive, inconsistent, and impossible to scale for large
cohorts.

**This project introduces an AI‑powered, scalable, LTI‑integrated viva
system** that allows students to upload written work, undergo a
structured oral-style interrogation of their understanding, and provide
instructors with detailed transcripts, behavioural logs, and simple
integrity metrics.

This empowers educators to run authentic assessments at scale while
preserving academic integrity in an AI‑enabled world.

## Impact Statement

This tool has the potential to reshape assessment across higher
education:

-   **Strengthens academic integrity** by directly verifying student
    understanding rather than relying on static text analysis.
-   **Reduces staff workload** by automating viva-style questioning,
    enabling large cohorts to be assessed fairly and consistently.
-   **Offers new evidence for academic judgement**, such as behavioural
    traces, answer quality, and conversational patterns.
-   **Respects student agency** by providing supportive, formative
    feedback on viva performance.
-   **Integrates seamlessly with existing LMS systems** using LTI,
    enabling rapid adoption across institutions.

By combining AI-driven questioning with behavioural analytics, this tool
provides a new assessment modality suitable for the AI era---one that
prioritises understanding, authorship, and fairness.

------------------------------------------------------------------------

# MVP Development Roadmap

## MVP Goal

Deliver a minimal but functional end-to-end system that allows:

1.  A student to upload their submission\
2.  Automatic text extraction\
3.  A timed AI viva with conversational memory\
4.  Logging of basic behavioural events\
5.  Instructor review of transcript, logs, and basic metrics

This is enough to demo, run pilots, and validate demand.

------------------------------------------------------------------------

## Phase 1 --- Core Infrastructure

### 1.1 Minimal Models

-   `Assignment`
-   `Submission`
-   `VivaSession`
-   `VivaMessage`
-   `InteractionLog`

### 1.2 LTI Integration

-   Launch and deep linking already working\
-   Store assignment settings\
-   Redirect users to role-appropriate pages

### 1.3 Basic Instructor Home

-   Placeholder "no submissions yet" page

------------------------------------------------------------------------

## Phase 2 --- Student Submission Flow

### 2.1 Upload Page

-   Student uploads PDF/DOCX/TXT\
-   Stores raw file

### 2.2 Text Extraction

-   Convert file to text\
-   Save cleaned text into `Submission`

### 2.3 Submission Status Page

-   Display submission progress\
-   Enable Viva when extraction completes

------------------------------------------------------------------------

## Phase 3 --- AI Viva Session

### 3.1 Basic Viva UI

-   Show one question at a time\
-   Input box for answers\
-   On-screen countdown timer

### 3.2 AI Memory

Pass into OpenAI: - Submission text\
- Prior dialogue\
- System instructions\
- Latest student response

### 3.3 Session Limits

-   Client-side time limit\
-   Stop after duration or max questions

### 3.4 End-of-Session Handling

-   Save transcript\
-   Mark session complete

------------------------------------------------------------------------

## Phase 4 --- Behaviour Logging

### Basic MVP Logging:

-   paste\
-   cut\
-   copy\
-   focus/blur

Store in `InteractionLog` with timestamps.

------------------------------------------------------------------------

## Phase 5 --- Instructor Review

### 5.1 Submission List

-   Anonymous student ID\
-   Submission time\
-   Viva state\
-   "View" link

### 5.2 Submission Detail

-   Uploaded file\
-   Extracted text\
-   Full transcript\
-   Behaviour logs\
-   Session timestamps

This provides enough insight for academic evaluation.

------------------------------------------------------------------------

## Phase 6 --- Basic Metrics & Feedback

### 6.1 AI Summary Metrics (simple)

One post-processing call: - Overall understanding\
- Signs of weak authorship\
- High/medium/low confidence rating

### 6.2 Student Feedback

-   Friendly summary of viva performance

### 6.3 Instructor Notes

-   AI-generated concerns or flags

------------------------------------------------------------------------

## Phase 7 --- MVP Polish

### Includes:

-   Cleaning up UI\
-   Basic error handling\
-   Clear LTI navigation messages

At this point, the system is ready for pilot deployment.

------------------------------------------------------------------------

# Summary

This MVP delivers real, usable value:

-   A functioning viva engine\
-   Behavioural insight\
-   Clear instructor review workflow\
-   Seamless LMS launch and assignment flow

It is small enough to build quickly but strong enough to demonstrate the
concept to institutions and gather early adopters.
