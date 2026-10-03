"""Command line demo of the HR Policy assistant.
run with: 'python main.py'
"""

from hr_assistant.pipeline import ask, build_hr_assistant
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def main():
    logger.info("====CLI run started====")
    print("Build the HR Policy assistant")
    agent= build_hr_assistant()
    print("Assistant Ready!\n")

    demo_questions=[
        "How many paid leaves do I get?",
        "What is the notice period during probation?",
        "Can I work from home everyday?"
    ]

    for question in demo_questions:
        print("="*60)
        print("Question:", question)
        print("-"*60)
        answer = ask(agent, question)
        print("Answer:", answer)
        print("="*60)
        print()
        logger.info ("===CLI run completed===")

if __name__=="__main__":
    main()