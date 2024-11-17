def questionnaire(data):
    corret_answer=0
    wrong_answer=0
    for item in data:
        item["answer"] = input(item['question'] + "")
        if item["answer"] == ["answer"]:
            corret_answer+=1
        else:
            wrong_answer+=1
    print("\nResullt:")
    for item in data:
        print(f"Question:{item['question']}")
        print(f"Correct Answer:{item['corret_answer']}")
        print(f"Your Answer:{item['answer']}")
        
        print()

    print(f"Correct Answers:{corret_answer}")
    print(f"Wrong Answers:{wrong_answer}")  

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu",
        "corret_answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine",
        "corret_answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977",
        "corret_answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker",
        "corret_answer":"Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader",
        "corret_answer":"Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee",
        "corret_answer": "Wookiee"
    }
]

questionnaire(data)