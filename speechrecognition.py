import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to get a speech response
def get_speech(prompt):
    with sr.Microphone() as source:
        print(prompt)
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            response = recognizer.recognize_google(audio)
            print("You said: " + response)
            return response
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return None

def main():
    # Questions to ask
    questions = [
        "What region are you from? (Country, state, city, county, etc. In relation to accent dialect)",
        "What region is your family from?",
        "Do you speak a certain dialect? If so, which dialect?",
        "Do all the members of your family speak the same dialect?",
        "Do you speak another language? If so what language or languages?"
    ]

    responses = {}

    # Ask each question and store the response
    for question in questions:
        response = None
        while response is None:
            response = get_speech(question)
        responses[question] = response

    print("\nSummary of Responses:")
    for question, response in responses.items():
        print(f"{question}: {response}")

if __name__ == "__main__":
    main()
