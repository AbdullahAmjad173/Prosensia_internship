# Function to store and return the questions and their correct answers
def get_questions():
    # Storing questions and answers in a dictionary
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What color do you get when you mix red and white?": "Pink",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is the largest planet in our solar system?": "Jupiter"
    }
    return questions

# Function to ask a question and check if the answer is correct
def ask_question(question, correct_answer):
    user_answer = input(question + " ")
    
    # Check if the user's answer is correct (case-insensitive)
    if user_answer.strip().lower() == correct_answer.lower():
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
        return False

# Main function to run the quiz game
def run_quiz():
    questions = get_questions()  # Load the questions
    score = 0  # Initialize the score

    # Iterate through the questions and ask them to the user
    for question, correct_answer in questions.items():
        if ask_question(question, correct_answer):
            score += 1  # Increment the score if the answer is correct

    # Final score output
    print(f"\nYour final score is {score} out of {len(questions)}.")

# Run the quiz game
if __name__ == "__main__":
    run_quiz()
