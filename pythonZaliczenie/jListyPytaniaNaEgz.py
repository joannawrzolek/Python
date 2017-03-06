import random

exam_questions = ["1", "2", "3","4", "5", "Programowanie strukturalne a obiektowe", "Typy sieci komputerowych", "Topologie sieci", "Algorytmy sortujace i ich zlozonosc", "UML"]

random.seed()
lottery = random.sample(exam_questions,3)

print(lottery)