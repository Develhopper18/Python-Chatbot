try:
    from words import *
    import warnings
    from requirements import *
    import datetime
    import webbrowser
    import os

    # Warning for the user
    warnings.warn(
        "The first letter in the line should be capital or the code is useless", Warning, 2
    )

    # Greeting the user
    Greet()

    # Main Code
    while True:
        l = input(">> ")
        if l in Qs:
            print(f"You: {l}")
            speak(f"{Qs[l]}")
            print(f"chatbot: {Qs[l]}")
        elif l == "exit":
            print("Chatbot: Bye! see you soon")
            warnings.warn("You are leaving me Bye", Warning, 10)
            break
        elif l == "Search":
            webs()
        elif l == "wikipedia":
            wiking()
        elif l == "Read for me":
            pdf()
        elif l == "say" or "say":
            say()
        elif l in shrt:
            print(f"You: {l}")
            print(f"Chatbot: {shrt[l]}")
            speak(f"{shrt[l]}")
        elif l not in Qs:
            speak("Sorry I didn't under stand that")
            speak("Try again")
            print(f"Chatbot: Sorry I didn't under stand that")
            print(f"Chatbot: Try again")
        else:
            print("Sorry i can't understand you")
            speak("Sorry i can't understand you")
except Exception as e:
    print(f"error found ({e})")
    speak(e)