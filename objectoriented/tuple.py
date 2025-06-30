# class HighScore:
#     def __init__(name , age, score):
#         self.name = name
#         self.age = age
#         self.score = score

def getHighestScorer():
    score = (("Sam", 12, 490), ("Eva", 9, 495), ("Jay", 10, 480), ("Justin", 8, 300))
    maxhighscore = min(score, key=lambda t: t[2])
    print(maxhighscore)

getHighestScorer()

def gcd_euclidean(a, b):

    while(b):
        a, b = b, a % b
    return a

num1 = 60
num2 = 48
result = gcd_euclidean(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")  # Output: 12