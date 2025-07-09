import random
import json
import html
import re

class Game():
    def __init__(self):
        self.lives = 5
        self.highest_score = 0
        self.score = 0
        self.asked = set()
        try:
            with open('trivia_questions.json', 'r', encoding='utf-8') as f:
                raw_data = f.read()
                self.questions = json.loads(raw_data)
            # Clean questions: decode HTML entities and remove unwanted control characters
            self.questions = {
                html.unescape(k): html.unescape(v).replace('\b', '').replace('\n', ' ').replace('\r', '')
                for k, v in self.questions.items()
            }
            print(f"Loaded {len(self.questions)} questions.")
        except FileNotFoundError:
            print("Error: trivia_questions.json not found. Please run the question fetch script first.Make sure that the trivia_questions file is in the same folder as the game.py file.")
            self.questions = {}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}. Check trivia_questions.json for formatting issues.")
            self.questions = {}

    def give_question(self):
        if not self.questions or len(self.asked) >= len(self.questions):
            return None
        question = random.choice(list(self.questions.keys()))
        while question in self.asked:
            question = random.choice(list(self.questions.keys()))
        self.asked.add(question)
        return question

    def check_answer(self, question, answer):
        if question is None:
            return 'Error: No question available.'
        if answer.lower().strip() == self.questions[question].lower():
            self.score += 1
            return 'You get a point for your efforts.'
        else:
            self.lives -= 1
            return 'Sorry, you just lost a life. Proceed with caution.'

    def play_game(self):
        if not self.questions:
            print("No questions available. Please run the question fetch script first.Make sure that the trivia_questions file is in the same folder as the game.py file.")
            return
        while self.lives > 0:
            question = self.give_question()
            if question is None:
                print('Congratulations! You answered all questions!')
                break
            # Display question with clean formatting
            print(f'Lives:   {self.lives*'#'}                        Score : {self.score}')
            print(f'Question: {question}')
            print('Your answer is:')
            answer = input().strip()
            print(self.check_answer(question, answer))
            print()
        if self.lives == 0:
            print(' GAME OVER 😂. Seems like you\'re out of lives. I will be waiting for a better version of you.')
        self.highest_score = max(self.highest_score, self.score)
        print(f'Your final score: {self.score}, Highest score: {self.highest_score}')
        print()

    def menu(self):
        while True:
            print('Welcome, Player 1 to The Herculian Tasks')
            print()
            print('Menu:')
            print('1. Play a new game')
            print('2. Check highest score')
            print('3. Game Guide')
            print('4. Quit game')
            print()
            print('Enter your choice:')
            choice = input().strip()
            print()

            if choice == '1':
                self.lives = 5
                self.score = 0
                self.asked = set()
                self.play_game()
            elif choice == '2':
                print(f'Highest score: {self.highest_score}')
                print()
            elif choice == '3':
                print('GAME GUIDE:')
                print('This game is a very interesting one.')
                print('You are given a question, and you must provide the correct answer.')
                print('You have 5 lives. An incorrect answer costs one life.')
                print('Earn 1 point for each correct answer. Good luck!')
                print()
            elif choice == '4':
                print('Quitting the game.')
                exit()
            else:
                print('Your input don\'t match anything on the list.')
                print()

if __name__ == '__main__':
    a = Game()
    a.menu()