import json

def load_questions():
    """Load questions from the JSON file."""
    try:
        with open('questions.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: questions.json file not found.")
        return []

def run_exam(user_name, questions):
    """Run the examination loop."""
    score = 0
    total = len(questions)
    
    print(f"\n--- Welcome {user_name}! The exam starts now. ---")
    
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        guess = input("Your answer (A, B, C, or D): ").upper()
        
        if guess == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was {q['answer']}.")
            
    return score, total

def main():
    # Simple "Login"
    print("=== Python Examination System ===")
    name = input("Enter your name to begin: ")
    
    # Load and run
    questions = load_questions()
    if questions:
        score, total = run_exam(name, questions)
        
        # Display Final Results
        percentage = (score / total) * 100
        print("\n" + "="*30)
        print(f"EXAM COMPLETE: {name}")
        print(f"Final Score: {score}/{total}")
        print(f"Percentage: {percentage:.2f}%")
        print("="*30)
    else:
        print("No questions available. Please check questions.json.")

if __name__ == "__main__":
    main()