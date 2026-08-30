import time


PAUSE = 0.4

print("=" * 160)
print("BAYMAX v1.0".center(160))
print("=" * 160)
print()
print("STATUS: OFFLINE 🔴")
print()

print('Type "baymax" to activate.')
print()

activation_code = ""

while activation_code != "baymax":
    activation_code = input("Activation Command: ").lower().strip()

    if activation_code != "baymax":
        print("Invalid Activation Command...❌")
        print('Please type "baymax" to activate Baymax.')
        print()

print()
print("Activation Accepted...✅")
time.sleep(PAUSE)

print("Initializing Systems...")
time.sleep(PAUSE)

print("Checking Protocols...")
time.sleep(PAUSE)

print("Starting Core Modules...")
time.sleep(PAUSE)

print()
print("STATUS: ONLINE 🟢")
print()

print("Hello.")
time.sleep(PAUSE)

print("I am Baymax.")
time.sleep(PAUSE)

print("It is a pleasure to meet you.")
time.sleep(PAUSE)

name = input("\nTo personalize your experience, may I know your name?\n\nName: ").strip()
if not name:
    name = "friend"

print()
print(f"Welcome {name}.")
time.sleep(PAUSE)

print("It is a pleasure to meet you.")
time.sleep(PAUSE)

print("How may I assist you today?")
time.sleep(PAUSE)

knowledge_base = {
    "hi": "greeting",
    "hello": "greeting",
    "hey": "greeting",
    "good morning": "greeting",
    "good afternoon": "greeting",
    "good evening": "greeting",
    "hola": "greeting",

    "who are you": "identity",
    "who are you?": "identity",

    "what can you do": "capabilities",
    "what can you do?": "capabilities",
    "what do you do": "capabilities",
    "what do you do?": "capabilities",

    "what is ai": "what_is_ai",
    "what is ai?": "what_is_ai",
    "what is artificial intelligence": "what_is_ai",
    "what is artificial intelligence?": "what_is_ai",

    "what is python": "what_is_python",
    "what is python?": "what_is_python",
    "tell me about python": "what_is_python",
    "python": "what_is_python",

    "thanks": "thanks",
    "thank you": "thanks",
    "thankyou": "thanks",
}

responses = {
    "greeting": [
        f"Hello, {name}.",
        "It is nice to see you.",
        "How may I assist you today?",
    ],
    "identity": [
        "I am Baymax.",
        "I am a supportive study and wellness companion.",
        "I can offer general encouragement, but I do not provide medical advice.",
    ],
    "capabilities": [
        "I can perform simple rule-based tasks.",
        "I can greet you, answer basic questions about AI and Python, and respond to how you are feeling.",
        "I can also offer simple study support and end our chat when you type exit.",
        "My responses follow predefined rules, so I am still learning and cannot do everything.",
    ],
    "what_is_ai": [
        "AI stands for Artificial Intelligence.",
        "It allows machines to perform tasks that normally require human intelligence.",
    ],
    "what_is_python": [
        "Python is a high-level, interpreted programming language.",
        "It is known for its simplicity and readability.",
    ],
    "thanks": [
        "You are welcome.",
        f"I am always happy to help, {name}.",
    ],
}

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input in [
        "exit",
        "quit",
        "goodbye",
        "bye",
        "sayonara",
    ]:
        print(f"\nBaymax: It was a pleasure assisting you, {name}.")
        time.sleep(PAUSE)
        print("Baymax: Shutting down...")
        time.sleep(PAUSE)
        print("STATUS: OFFLINE 🔴")
        break

    elif user_input in ["how are you", "how are you?"]:
        print("\nBaymax: I am doing great.")
        time.sleep(PAUSE)

        print("Baymax: Thank you for asking.")
        time.sleep(PAUSE)

        print("Baymax: How are you feeling today?")
        time.sleep(PAUSE)

        feeling = input("\nYou: ").lower().strip()

        if feeling in [
            "good",
            "great",
            "happy",
            "fine",
        ]:
            print(f"\nBaymax: This is good to hear, {name}.")
            time.sleep(PAUSE)
            print("Baymax: I am glad you are feeling well.")
            time.sleep(PAUSE)
            print(f"Baymax: Remember, I am always here to assist you, {name}.")
            time.sleep(PAUSE)
            print(f"Baymax: Is there anything else I can assist you with, {name}?")
            time.sleep(PAUSE)

        elif feeling in [
            "bad",
            "sad",
            "unwell",
            "not good",
            "tired",
            "stressed",
        ]:
            print(f"\nBaymax: I am sorry to hear that, {name}.")
            time.sleep(PAUSE)

            print("Baymax: Would you like to talk about it?")
            time.sleep(PAUSE)

            talk = input("\nYou: ").lower().strip()

            if talk in [
                "yes",
                "sure",
                "okay",
                "yeah",
            ]:
                print("Baymax: Of course.")
                time.sleep(PAUSE)

                print("Baymax: I am listening. Feel free to share your thoughts and feelings with me.")
                time.sleep(PAUSE)

                problem = input("\nYou: ").lower().strip()

            elif talk in [
                "no",
                "nope",
                "not now",
            ]:
                print("\nBaymax: That is completely okay.")
                time.sleep(PAUSE)
                print(f"Baymax: I will be here if you need me, {name}.")
                time.sleep(PAUSE)
                continue

            else:
                problem = talk

            if any(word in problem for word in ["exam", "study", "studies", "studying"]):
                print("\nBaymax: I understand that you are concerned about your studies.")
                time.sleep(PAUSE)

                print("Baymax: That sounds like something we can work through together.")
                time.sleep(PAUSE)

                print("Baymax: Remember, you do not have to figure everything out at once.")
                time.sleep(PAUSE)

                print("Baymax: Would you like me to help you make a simple study plan?")
                time.sleep(PAUSE)

                study_plan = input("\nYou: ").lower().strip()

                if study_plan in [
                    "yes",
                    "sure",
                    "okay",
                    "yeah",
                ]:
                    print("\nBaymax: Of course.")
                    time.sleep(PAUSE)

                    print("Baymax: Let's make this simple and manageable.")
                    time.sleep(PAUSE)

                    print(f"Baymax: How many hours can you study today, {name}?")
                    time.sleep(PAUSE)

                    study_hours = input("\nYou: ").strip()

                    print(f"\nBaymax: Great. We can work with {study_hours} hours.")
                    time.sleep(PAUSE)

                    print("Baymax: I recommend dividing your time into focused study sessions.")
                    time.sleep(PAUSE)

                    print("Baymax: Remember to take short breaks between sessions.")
                    time.sleep(PAUSE)

                    print(f"Baymax: You have got this, {name}.")
                    time.sleep(PAUSE)

                elif study_plan in [
                    "no",
                    "nope",
                    "not now",
                ]:
                    print("\nBaymax: That is completely okay.")
                    time.sleep(PAUSE)

                    print(f"Baymax: I will be here whenever you are ready, {name}.")
                    time.sleep(PAUSE)

                else:
                    print("\nBaymax: I understand.")
                    time.sleep(PAUSE)

                    print("Baymax: We can work on it whenever you are ready.")
                    time.sleep(PAUSE)

            else:
                print("\nBaymax: I understand.")
                time.sleep(PAUSE)

                print("Baymax: Thank you for sharing that with me.")
                time.sleep(PAUSE)

                print(f"Baymax: I am here for you, {name}.")
                time.sleep(PAUSE)

        else:
            print("\nBaymax: Thank you for telling me.")
            time.sleep(PAUSE)

            print(f"Baymax: I am here if you would like to talk, {name}.")
            time.sleep(PAUSE)

    else:
        intent_key = knowledge_base.get(user_input)

        if intent_key is not None:
            reply_lines = responses[intent_key]

            print()
            for line in reply_lines:
                print(f"Baymax: {line}")
                time.sleep(PAUSE)

        else:
            print("\nBaymax: I am sorry.")
            time.sleep(PAUSE)

            print("Baymax: I do not understand that command yet.")
            time.sleep(PAUSE)

            print("Baymax: Could you please ask another question?")
            time.sleep(PAUSE)
