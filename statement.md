# Project Statement & Scope

## 1. Problem Statement
Conducting simple quizzes and tests often requires heavy software, constant internet connectivity, or tedious manual grading. Instructors, students, and self-learners need a lightweight, offline tool to assess knowledge quickly. Specifically:
- **Manual Grading:** Checking multiple-choice answers by hand takes time and is prone to human error.
- **Complex Setup:** Setting up a quiz shouldn't require advanced coding or database knowledge; it should be as easy as editing a simple text file.
- **Lack of Instant Feedback:** Learners need to know immediately if they got an answer right or wrong to understand their mistakes.

This project addresses these challenges by offering a simple, lightweight, and offline Command Line Interface (CLI) application for taking exams.

---

## 2. Scope of the Project

### In-Scope:
- **Command-Line Interface:** Providing a simple text-based examination loop for the user[cite: 1].
- **Local Data Loading:** Reading custom questions, multiple-choice options, and correct answers directly from a local `questions.json` file[cite: 1].
- **Automated Grading:** Tracking the user's score automatically as they answer questions[cite: 1].
- **Final Results Calculation:** Computing and displaying the user's final score and overall percentage at the end of the exam[cite: 1].

### Out-of-Scope:
- Graphical User Interface (GUI) or mobile app interface (this is strictly CLI-based).
- Complex cloud databases (e.g., SQL, MongoDB) or internet connectivity requirements.
- Advanced user authentication (e.g., login passwords, multi-user accounts).

---

## 3. Target Users
- **Educators & Instructors:** Teachers looking for a fast, no-fuss way to create and administer multiple-choice quizzes using simple JSON files.
- **Students & Self-Learners:** Individuals who want to test their own knowledge (like Python basics) in a distraction-free, offline environment.

---

## 4. High-Level Features
- **Simple User Entry:** A basic login system that prompts the user for their name to personalize the exam experience[cite: 1].
- **Dynamic Question Loading:** Automatically loads and formats questions and options from `questions.json`[cite: 1].
- **Instant Feedback:** Instantly tells the user if their guess is correct or wrong, and reveals the right answer if they make a mistake[cite: 1].
- **Results Engine:** Calculates the total correct answers out of the total questions and computes the final accuracy percentage[cite: 1].