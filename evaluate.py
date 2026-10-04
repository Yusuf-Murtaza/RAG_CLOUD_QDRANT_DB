"""Run the correcteness evaluation and upload  results to LangSmith for analysis.

Run with: python evaluate.py
"""

#Display the marksheet to parent of student

from hr_assistant.evaluation import run_evaluation

def main():
    """Run the evaluation and upload results to LangSmith"""
    print("Running evaluation and uploading results to LangSmith...")
    results = run_evaluation()
    print("Done! Open your LangSmith dashboard to see the results.")
    print(results)

if __name__ == "__main__":
    main()