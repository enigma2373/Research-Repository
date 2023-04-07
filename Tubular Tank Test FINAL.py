# Final VErsion of The tubular tank test

# function to check age
def int_checker(question, low, high):
    valid = False
    while not valid:
        error = "Please enter a valid age \n"
        wrong_age = "Sorry, you have to be between the ages of 14 and 21 to take this test."
        correct_age = "this test is well suited for you"
        response = ""
        while not response:
            try:
                response = int(input(question.format(low, high)))
                if low <= response <= high:
                    print(correct_age)
                    return response

                elif response > high or response < low:
                    print(wrong_age)
                    print()
            except:
                print(error)
                print()

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

#stores the questions
question_prompts = [
    "(1) What was the tank made in WW2 by the group who made the original WW1 Tanks\n(a) TOG II\n(b) The Mark X\n",
    "(2) What Type of Cannon Did the Tiger 1 Equip\n(a) 76 mm gun M1 \n(b) 8.8 cm KwK 36\n",
    "(3) When did the Sherman Tank See its first combat\n(a) June 1944 \n(b) October 1942\n",
    "(4) What Class of tank was the M18 Hellcat\n(a) LT \n(b) TD\n",
    "(5) What was the cross-country Operational Distance of the Panther\n(a) 100km\n(b) 250km\n",
    "(6) What year was the first Tank on Tank combat\n (a) 1938 \n (b) 1918\n",
    "(7) What was the first heavy tank that the British made\n (a) The mother \n (b) The Mark 1\n",
    "(8) What was the length of the tog II \n(a) 10m \n(b) 15m\n",
    "(9) What was the name of the largest operational tank \n(a) Jagdtiger\n(b) Char 2c\n",
    "(10) What was the tank that had two huge front spoked wheels \n(a) Tsar tank\n(b) Kugelpanzer\n",
    "(11) What tank was the M3 Grant Based on \n(a) M3 stuart\n(b) M3 lee\n",
    "(12) What was the name of the First Main battle tank \n(a) Panther II\n(b) Centurion A41\n",
    "(13) What is the current German MBT \n(a) Leopard 2\n(b) Radkampfwagen 90\n",
    "(14) What Does APDS mean \n(a) Armour piercing discarding sabot\n(b) Armoured Personal Defence System\n",
    "(15) What was the Paste applied to the outside of some German tanks in WW2\n(a) Zimmerit\n(b) Epoxid\n",


]
# Contains the answers
questions = [
    Question(question_prompts[0], "A"),
    Question(question_prompts[1], "B"),
    Question(question_prompts[2], "B"),
    Question(question_prompts[3], "B"),
    Question(question_prompts[4], "A"),
    Question(question_prompts[5], "B"),
    Question(question_prompts[6], "A"),
    Question(question_prompts[7], "A"),
    Question(question_prompts[8], "B"),
    Question(question_prompts[9], "A"),
    Question(question_prompts[10], "B"),
    Question(question_prompts[11], "B"),
    Question(question_prompts[12], "A"),
    Question(question_prompts[13], "A"),
    Question(question_prompts[14], "A"),


]


def run_quiz():
    score = 0
    for question in questions:
        answer = input(question.prompt).upper()
        if answer == question.answer:
            score += 1
        print("so far you got", score, "out of", len(questions))


# Main Runtime
int_checker("What is your age? ", 14, 21)
run_quiz()
print("Thanks for playing my quiz")

