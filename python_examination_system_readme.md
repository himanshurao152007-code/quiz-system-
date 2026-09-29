# Python Examination System

Hey everyone! This is my python examination system. its basically a simple quize app that runs right in your terminal.

The cool thing about this project is that all the questions are saved in a seperate `questions.json` file. So if you want to make a new quiz, you dont even have to touch the python code. You just edit the json file!

### What it does (Features)

* Asks for your name so it can greet you
* Loads everything dynamicly from the json file
* Tells you if your answer is correct or wrong immediatly
* Doesn't matter if you type capital 'A' or small 'a', it still works
* Calculates your final score and percentage at the very end
* wont crash if the json file is missing (it gives a nice error instead)

### Tech used

* Python 3
* JSON (its a builtin library so you dont need to install anything extra)

### How to install and run it

Its super simple to run this:

1. Download both `main.py` and `questions.json` and put them in the exact same folder.
2. Open your terminal or command prompt in that folder.
3. Type this command and hit enter:
   ```bash
   python main.py
   ```
   *(note: if your on mac or linux, u might need to type `python3 main.py` instead)*

### How to test it

If you wanna check if everything is working fine:

* Just play the game normally and see if your final score adds up right at the end.
* Try typing lowercase letters for your answers to make sure it accepts them.
* Try deleting `questions.json` and run the script. It shouldn't crash the whole program, it will just say "Error: questions.json file not found."
* Open the json file and try adding your own custom question. Then run the python file again to see it pop up!