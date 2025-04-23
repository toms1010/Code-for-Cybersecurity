import time
import random

# Function to display introduction
def introduction():
    print("\n🔒 Welcome to the Social Engineering Awareness Tool 🔒")
    time.sleep(1)
    print("\nThis program will:")
    print("1. Explain common types of social engineering attacks.")
    print("2. Ask you questions to test your awareness.")
    print("3. Provide tips to protect yourself.\n")
    input("Press Enter to continue...")

# Function to display social engineering attack types
def explain_attacks():
    print("\n🔥 **Types of Social Engineering Attacks** 🔥")
    time.sleep(1)

    attacks = {
        "Phishing": "Fake emails or messages designed to trick you into revealing sensitive information.",
        "Pretexting": "Creating a false scenario to obtain information, such as pretending to be a trusted person.",
        "Baiting": "Leaving infected devices (like USBs) in public places to lure victims into using them.",
        "Tailgating": "An attacker gains physical access by following authorized personnel through secured doors.",
        "Vishing": "Phone-based scams where attackers impersonate trusted individuals or organizations."
    }

    for attack, description in attacks.items():
        print(f"\n🔹 {attack}:")
        print(f"   {description}")
        time.sleep(1)

# Function to ask questions and verify answers
def ask_questions():
    print("\n🛡️ **Social Engineering Awareness Quiz** 🛡️\n")

    questions = [
        {
            "question": "What is the main goal of phishing attacks?",
            "options": ["A) To gain physical access to a building", 
                        "B) To steal sensitive information", 
                        "C) To sell fake products"],
            "answer": "B"
        },
        {
            "question": "Which of the following is an example of vishing?",
            "options": ["A) Fake website asking for credentials",
                        "B) Phone call pretending to be tech support",
                        "C) Email asking for donation"],
            "answer": "B"
        },
        {
            "question": "What should you do if you receive a suspicious email?",
            "options": ["A) Click the link to investigate", 
                        "B) Reply to ask for more info", 
                        "C) Report it and delete it"],
            "answer": "C"
        },
        {
            "question": "What is baiting in social engineering?",
            "options": ["A) Fake social media accounts", 
                        "B) Using infected USBs or devices", 
                        "C) Fake job offers"],
            "answer": "B"
        }
    ]

    score = 0

    for q in questions:
        print(f"\n{q['question']}")
        for option in q['options']:
            print(option)
        answer = input("\nEnter your answer (A, B, C): ").upper()

        if answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was {q['answer']}.")

        time.sleep(1)

    return score, len(questions)

# Function to display results
def display_results(score, total):
    print("\n📊 **Quiz Results** 📊")
    print(f"You got {score}/{total} correct!")

    if score == total:
        print("🎯 Excellent! You are well aware of social engineering tactics.")
    elif score >= total * 0.7:
        print("👍 Good job! You have a solid understanding but stay alert!")
    else:
        print("⚠️ You need to improve your awareness. Review the tips below!")

# Function to display tips
def display_tips():
    print("\n💡 **Tips to Protect Yourself from Social Engineering** 💡")
    time.sleep(1)

    tips = [
        "✔️ Never share sensitive information with unverified individuals.",
        "✔️ Be cautious of unexpected emails or messages with links or attachments.",
        "✔️ Verify the sender's identity before responding to suspicious messages.",
        "✔️ Use multi-factor authentication (MFA) for added security.",
        "✔️ Do not plug unknown USBs or devices into your system.",
        "✔️ Regularly update your passwords and use strong, unique ones."
    ]

    for tip in tips:
        print(tip)
        time.sleep(1)

# Main function
def main():
    introduction()
    explain_attacks()
    
    score, total = ask_questions()
    display_results(score, total)
    
    display_tips()
    print("\n✅ Thank you for using the Social Engineering Awareness Tool! Stay safe! 🔐")

# Run the program
if __name__ == "__main__":
    main()
