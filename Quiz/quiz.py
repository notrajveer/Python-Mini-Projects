def run_quiz():
    questions = [
        {"prompt": "What allows you to iterate in Python?", "answer": "loops"},
        {"prompt": "What keyword defines a funtion?", "answer": "def"},
        {"prompt": "What data type is 'True'?", "answer": "boolean"},
    ]
    
    score = 0
    
    print("---Python Quiz---")
    
    for q in questions:
        print(q["prompt"])
        user_ans = input("Answer: ").lower().strip()
        
        if user_ans == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was: {q['answer']}\n")
    
    print(f"You got {score}/{len(questions)} correct.")
    
if __name__ == "__main__":
    run_quiz()