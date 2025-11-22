def generate_quiz(summary):
    words = summary.split()
    return [
        f"What is the main idea of the summary: '{words[0]} ...'?",
        "List two key points covered in the video.",
        "Explain the topic of the video in one line."
    ]
