# Conner Skoumal
# Spider-Scrum
# MatchmakerPython

# Constants
INTRO = '''
______________________________________________________

              Conner Skoumal Presents
            With Help From Spider-Scrum
            Matchmaker: Conner Edition
______________________________________________________

This program is meant to find out how compatible as people 
you and me are. Maybe you'll be my friend, maybe we'll 
fall in love, or maybe I'll absolutely despise you. Below 
you will be presented with 5 different questions. You'll 
need to answer with a number 1-5. 1 would mean strongly 
disagree, 2 would mean disagree, 3 would be neutral, 4 
would be agree, and 5 would be strongly agree. After 
each question you will be told your compatibility score 
for that question. At the end it will tell you our total 
compatibility!

I hope you're my soulmate!

'''

question = [
  'Marvel Movies are Overrated: ',
  'Portillos is the Best!: ',
  'Star Trek is Better Than Star Wars: ',
  'Dogs are Better Than Cats: ',
  'I Love Playing Video-Games: ',
]

desiredResponse = [
  2, # Disagree
  5, # Strongly Agree
  1, # Strongly Disagree
  4, # Agree
  5, # Strongly Agree
]

response = []

compatibility = []

maxScore = 5 * len(question)

def validate(questionNumber):
  userResponse = str(input(question[questionNumber]))
  if not userResponse.isnumeric():
    print('\nThis is not a number!')
    return -1
  else:
    userResponse = int(userResponse)
    if userResponse >=1 and userResponse <=5:
      return userResponse
    else:
      print('\nThis is not a number between 1 and 5')
      return -1

# Program starts executing here.

print(INTRO)

# Ask all questions.

for l in range(len(question)):
  validResponse = -1
  while validResponse == -1:
    validResponse = validate(l)
    if validResponse == -1:
      print('Please try again.\n')
  response.append(validResponse)
  userCompatibility = 5 - abs(validResponse - desiredResponse[l])
  compatibility.append(userCompatibility)
  print('Question %d Compatibility: %d\n' % (l + 1, userCompatibility))

# Calculate total compatibility.

totalCompatibility = 0
for c in compatibility:
  totalCompatibility += c
totalCompatibility *= 100 / maxScore
print('Total Compatibility: %d\n\n' % (totalCompatibility))

if totalCompatibility < (100 / 3):
  print('I do not want to be in the same room as you!\n\n')
elif totalCompatibility < ((100 / 3) * 2):
  print('Hey, would you like to be friends with me?\n\n')
elif totalCompatibility < 100:
  print('Where have you been all my life?\n\n')