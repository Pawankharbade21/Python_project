from summary import generate_summary
from quiz_generator import generate_quiz

def main():
    link = input("Enter YouTube URL: ")

    print("\nExtracting video transcript...")
    transcript = "Sample transcript extracted from API for demo."

    print("\nGenerating summary...")
    summary = generate_summary(transcript)
    print("\nSummary:")
    print(summary)

    print("\nGenerating Quiz Questions...")
    quiz = generate_quiz(summary)
    
    print("\nQuiz Questions:")
    for q in quiz:
        print("-", q)

if __name__ == "__main__":
    main()
