import random

class Game():
    def __init__(self):
        self.lives = 5
        self.highest_score = 0
        self.questions = {
    # Geography (10 questions, 10%)
    "What is the capital city of Brazil?": "Brasília",
    "Which river is the longest in the world?": "Nile",
    "What is the largest desert in the world?": "Sahara",
    "Which country is the smallest by land area?": "Vatican City",
    "What is the tallest mountain in the world?": "Mount Everest",
    "Which ocean is the largest on Earth?": "Pacific Ocean",
    "What is the capital of Australia?": "Canberra",
    "Which country is known as the Land of the Rising Sun?": "Japan",
    "What is the largest island in the world?": "Greenland",
    "Which river flows through Paris?": "Seine",

    # History (10 questions, 10%)
    "In which year did World War II end?": "1945",
    "Who was the first president of the United States?": "George Washington",
    "What year did the Berlin Wall fall?": "1989",
    "Who led the Indian independence movement against British rule?": "Mahatma Gandhi",
    "Which ancient civilization built the pyramids?": "Egyptians",
    "In which year did Christopher Columbus first reach the Americas?": "1492",
    "Who was the first woman to win a Nobel Prize?": "Marie Curie",
    "Which war was fought between the North and South in the United States?": "Civil War",
    "What was the name of the ship that sank in 1912?": "Titanic",
    "Who was the Roman emperor when Jesus was crucified?": "Tiberius",

    # Science (40 questions, 40%)
    "What is the chemical symbol for water?": "H2O",
    "Which planet is closest to the Sun?": "Mercury",
    "What gas makes up about 78% of Earth's atmosphere?": "Nitrogen",
    "Who developed the theory of relativity?": "Albert Einstein",
    "What is the largest organ in the human body?": "Skin",
    "Which element has the atomic number 6?": "Carbon",
    "What is the primary source of energy for Earth's climate system?": "Sun",
    "Which gas is used in balloons to make them float?": "Helium",
    "What is the hardest naturally occurring substance?": "Diamond",
    "Who discovered penicillin?": "Alexander Fleming",
    "What is the chemical symbol for gold?": "Au",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest mammal in the world?": "Blue Whale",
    "Which force keeps planets in orbit around the Sun?": "Gravity",
    "What is the chemical formula for table salt?": "NaCl",
    "Which organ in the human body pumps blood?": "Heart",
    "What is the speed of light in a vacuum (in m/s)?": "299792458",
    "Which element is a noble gas used in light bulbs?": "Neon",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who proposed the theory of evolution by natural selection?": "Charles Darwin",
    "What is the chemical symbol for oxygen?": "O",
    "Which part of the cell contains DNA?": "Nucleus",
    "What is the boiling point of water in Celsius?": "100",
    "Which scientist discovered the laws of planetary motion?": "Johannes Kepler",
    "What is the chemical symbol for iron?": "Fe",
    "Which gas is produced by plants during photosynthesis?": "Oxygen",
    "What is the smallest unit of life?": "Cell",
    "Which planet has prominent rings?": "Saturn",
    "What is the chemical symbol for silver?": "Ag",
    "Which bone is the longest in the human body?": "Femur",
    "What is the primary source of energy for a hurricane?": "Warm Ocean Water",
    "Which scientist formulated the laws of motion?": "Isaac Newton",
    "What is the chemical formula for carbon dioxide?": "CO2",
    "Which organ filters blood in the human body?": "Kidney",
    "What is the name of the first artificial satellite?": "Sputnik",
    "Which element is used in pencil lead?": "Graphite",
    "What is the freezing point of water in Celsius?": "0",
    "Which gas is the second most abundant in Earth's atmosphere?": "Oxygen",
    "Who discovered the structure of DNA?": "Watson and Crick",
    "What is the chemical symbol for sodium?": "Na",

    # Mathematics (40 questions, 40%)
    "What is 2 + 2?": "4",
    "What is the value of pi to two decimal places?": "3.14",
    "What is 5 squared?": "25",
    "What is the square root of 16?": "4",
    "What is 10 divided by 2?": "5",
    "What is the sum of angles in a triangle?": "180",
    "What is 3 times 4?": "12",
    "What is the value of 2 to the power of 3?": "8",
    "What is 15 minus 7?": "8",
    "What is the area of a square with side length 5?": "25",
    "What is 20 percent of 100?": "20",
    "What is the circumference of a circle with radius 1 (use pi = 3.14)?": "6.28",
    "What is 7 factorial?": "5040",
    "What is the slope of the line y = 2x + 3?": "2",
    "What is the value of x in the equation 2x = 10?": "5",
    "What is the Pythagorean theorem for a right triangle?": "a^2 + b^2 = c^2",
    "What is the sum of the first 5 positive integers?": "15",
    "What is 100 divided by 4?": "25",
    "What is the value of sin(0 degrees)?": "0",
    "What is the area of a circle with radius 2 (use pi = 3.14)?": "12.56",
    "What is 9 cubed?": "729",
    "What is the value of x in 3x + 5 = 14?": "3",
    "What is the least common multiple of 6 and 8?": "24",
    "What is the value of cos(90 degrees)?": "0",
    "What is the perimeter of a rectangle with length 5 and width 3?": "16",
    "What is 4 to the power of 2?": "16",
    "What is the value of 1/2 + 1/3 (as a fraction)?": "5/6",
    "What is the sum of angles in a quadrilateral?": "360",
    "What is the square root of 25?": "5",
    "What is 12 divided by 3?": "4",
    "What is the value of x in 5x - 10 = 15?": "5",
    "What is the area of a triangle with base 6 and height 4?": "12",
    "What is 6 times 7?": "42",
    "What is the value of tan(45 degrees)?": "1",
    "What is the greatest common divisor of 12 and 18?": "6",
    "What is 2/5 as a decimal?": "0.4",
    "What is the value of 3 to the power of 4?": "81",
    "What is the perimeter of a square with side length 4?": "16",
    "What is the value of x in 4x + 2 = 18?": "4",
    "What is the sum of the first 10 positive integers?": "55",
    "What is the capital city of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "Who wrote 'Pride and Prejudice'?": "Jane Austen",
    "What is the chemical symbol for gold?": "Au",
    "In which year did the Berlin Wall fall?": "1989",
    "What is the largest mammal in the world?": "Blue Whale",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the currency of Japan?": "Yen",
    "Which element has the atomic number 1?": "Hydrogen",
    "What is the longest river in the world?": "Nile",
    "Who played the character of Harry Potter in the film series?": "Daniel Radcliffe",
    "What is the national sport of Canada?": "Lacrosse",
    "Which country is known as the Land of the Rising Sun?": "Japan",
    "What gas makes up about 78% of Earth's atmosphere?": "Nitrogen",
    "Who was the first woman to win a Nobel Prize?": "Marie Curie",
    "What is the smallest country in the world?": "Vatican City",
    "Which band performed the song 'Bohemian Rhapsody'?": "Queen",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who discovered penicillin?": "Alexander Fleming",
    "What is the capital of Australia?": "Canberra",
    "Which animal is known as the 'King of the Jungle'?": "Lion",
    "What is the main ingredient in guacamole?": "Avocado",
    "In which sport is the term 'home run' used?": "Baseball",
    "What is the tallest mountain in the world?": "Mount Everest",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare",
    "What is the chemical formula for water?": "H2O",
    "Which country hosted the 2016 Summer Olympics?": "Brazil",
    "What is the largest desert in the world?": "Sahara",
    "Who is the lead singer of the band Coldplay?": "Chris Martin",
    "What is the official language of Brazil?": "Portuguese",
    "Which scientist developed the theory of relativity?": "Albert Einstein",
    "What is the capital city of Canada?": "Ottawa",
    "Which fruit is known as the 'king of fruits' and has a strong smell?": "Durian",
    "In which year did World War II end?": "1945",
    "What is the name of the fictional wizarding school in Harry Potter?": "Hogwarts",
    "Which element is a noble gas used in light bulbs?": "Neon",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "Who directed the movie 'Titanic'?": "James Cameron",
    "What is the national animal of Australia?": "Kangaroo",
    "Which planet is closest to the Sun?": "Mercury",
    "What is the primary source of energy for Earth's climate system?": "Sun",
    "Who was the first person to walk on the moon?": "Neil Armstrong",
    "What is the capital of Italy?": "Rome",
    "Which gas is essential for human respiration?": "Oxygen",
    "What is the name of the river that flows through Egypt?": "Nile",
    "Who wrote 'The Great Gatsby'?": " F. Scott Fitzgerald",
    "What is the hardest naturally occurring substance known?": "Diamond",
    "Which country is the largest by land area?": "Russia",
    "What is the name of the famous clock tower in London?": "Big Ben",
    "Which animal is the fastest land animal?": "Cheetah",
    "What is the capital of Spain?": "Madrid",
    "Who composed the 'Moonlight Sonata'?": "Ludwig van Beethoven",
    "What is the chemical symbol for iron?": "Fe",
    "Which country is known for the dance called Tango?": "Argentina",
    "What is the largest species of shark?": "Whale Shark",
    "Who was the first president of the United States?": "George Washington",
    "What is the capital of Brazil?": "Brasília",
    "Which bird is a symbol of peace?": "Dove",
    "What is the name of the famous statue in New York Harbor?": "Statue of Liberty",
    "Which element is used in pencil lead?": "Graphite",
    "What is the longest bone in the human body?": "Femur",
    "Who starred as Jack Sparrow in 'Pirates of the Caribbean'?": "Johnny Depp",
    "What is the national flower of Japan?": "Cherry Blossom",
    "Which country is famous for the Great Wall?": "China",
    "What is the smallest planet in our solar system?": "Mercury",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the capital of Russia?": "Moscow",
    "Which animal is known for its black and white stripes?": "Zebra",
    "What is the main language spoken in Mexico?": "Spanish",
    "Who painted 'Starry Night'?": "Vincent van Gogh",
    "What is the chemical symbol for silver?": "Ag",
    "Which country is the Eiffel Tower located in?": "France",
    "What is the largest bird in the world?": "Ostrich",
    "Who was the first African American president of the United States?": "Barack Obama",
    "What is the capital of India?": "New Delhi",
    "Which gas is used in balloons to make them float?": "Helium",
    "What is the name of the ship that sank in 1912 after hitting an iceberg?": "Titanic",
    "Who is the creator of the theory of evolution by natural selection?": "Charles Darwin",
    "What is the capital of South Africa?": "Pretoria",
    "Which fruit is associated with Newton’s theory of gravity?": "Apple",
    "What is the name of the largest coral reef system in the world?": "Great Barrier Reef",
    "Who played the role of Forrest Gump in the 1994 film?": "Tom Hanks",
    "What is the chemical formula for table salt?": "NaCl",
    "Which country is known as the 'Land of a Thousand Lakes'?": "Finland",
    "What is the name of the famous detective created by Arthur Conan Doyle?": "Sherlock Holmes",
    "Which planet is known for its prominent rings?": "Saturn",
    "What is the capital of Egypt?": "Cairo",
    "Which animal is the largest living primate?": "Gorilla",
    "What is the name of the first man-made satellite launched by the Soviet Union?": "Sputnik",
    "Who wrote '1984'?": "George Orwell",
    "What is the capital of Germany?": "Berlin",
    "Which sport uses a shuttlecock?": "Badminton",
    "What is the chemical symbol for carbon?": "C",
    "Which country is famous for the pyramids?": "Egypt",
    "What is the name of the river that flows through Paris?": "Seine",
    "Who was the lead singer of The Beatles?": "John Lennon",
    "What is the largest organ in the human body?": "Skin",
    "Which country is known for the Taj Mahal?": "India",
    "What is the name of the currency used in the United Kingdom?": "Pound",
    "Who invented the telephone?": "Alexander Graham Bell"
}
        self.score = 0
        self.asked = set()
        



    def give_question(self):
        question = random.choice(list(self.questions.keys()))
        while question in self.asked and len(self.asked) < len(self.questions):
            question = random.choice(list(self.questions.keys()))
        self.asked.add(question)
        return question



    def check_answer(self,question,answer):
        if answer.lower() == self.questions[question].lower():
            self.score += 1
            return 'You answered correctly.'

        else:
            self.lives -= 1
            return 'Sorry, you just lost a life. Proceed with caution.'



    def play_game(self):
        while self.lives > 0:
            question = self.give_question()
            print(f"Lives:{'*'*self.lives}        Score:{self.score}")
            print(f'Question : {question} ')
            print('Your answer is : ')
            answer = input()
            print(self.check_answer(question, answer))
            print()

        self.highest_score = max(self.highest_score, self.score)
        
     

    def menu(self):
        print('Welcome, Player 1 to The Herculian Tasks')
        print()
        print('Menu:')
        print('1. Play a new game')
        print('2. Check highest score')
        print('3. Game Guide')
        print('4. Quit game')
        print()
        print('Enter your choice: ')
        choice = input()
        print()

        if choice == '1':
            self.lives = 5
            self.score = 0
            self.asked = set()
            self.play_game()
            if self.lives == 0:
                print('Seems like your\'e out of lives. I will be waiting for a better version of you. Did I forget to say that it\'s GAME OVER? 😂')
                print()
                self.menu()
                

        elif choice == '2':
            print(f"The highest score is {self.highest_score}")
            print()
            self.menu()

        elif choice == '3':
            print('GAME GUIDE:')
            print('This game is a very interesting one.')
            print('You are given a word or phrase, and you are to give us a word that directly correlates with word or phrase you are given.')
            print('Easy, right. Yeah. So you have only 5 chances, to prove your worth (we are very generous).')
            print('Good luck, or not; because you\'ll need more than just luck for this.')
            print()
            self.menu()

        elif choice== '4':
            exit('Quiting the game.')

        else:
            print('You trippin\'. Your input don\'t match anything on the list.')




if __name__ == '__main__':
    a = Game()
    a.menu()