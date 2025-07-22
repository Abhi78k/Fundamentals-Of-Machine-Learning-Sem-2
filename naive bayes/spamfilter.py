import pandas as pd
import string
import math

data = pd.read_csv('spam.csv')

totalRows = len(data)

# filter out the rows which are spam and which are ham
spam = data[data['Category']=='spam']
ham = data[data['Category']=='ham']

lenSpam = len(spam)
lenHam = len(ham)

probSpam = lenSpam/totalRows
probHam = lenHam/totalRows

# put all the spam mails together and ham mails togther for individual word frequency calculation
spamtxt = ' '.join(spam['Message'].to_list())
hamtxt = ' '.join(ham['Message'].to_list())

# remove all the uncessary punctuation marks in the words and replace with space
def remove_punctuation(text):
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    return text.translate(translator).lower()

spamtxt = remove_punctuation(spamtxt)
hamtxt = remove_punctuation(hamtxt)

spamdict={}
hamdict={}

spamlist = spamtxt.split()
hamlist = hamtxt.split()

# create the frequency dictionary
for i in spamlist:
  if i not in spamdict:
    spamdict[i]=1
  else:
    spamdict[i]+=1
    
for i in hamlist:
  if i not in hamdict:
    hamdict[i]=1
  else:
    hamdict[i]+=1
    
a = sum(spamdict.values())
b = sum(hamdict.values())

# Keep the original frequency dictionaries for Laplace smoothing
spamFreqDict = spamdict.copy()
hamFreqDict = hamdict.copy()

# update the frequency dictionary with probabilities for each of the words
spamdict = {i:spamdict[i]/a for i in spamdict}
hamdict = {i:hamdict[i]/b for i in hamdict}

vocab = set(list(spamdict.keys())+list(hamdict.keys()))
v = len(vocab)

print("Enter your email (press ENTER twice to finish):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

t = '\n'.join(lines)


t = remove_punctuation(t)
t = t.split()

# take log to avoid very small numbers
spamScore=math.log(probSpam)
hamScore=math.log(probHam)

for word in t:
  # perform laplace smoothing so that the words that are not in the given emails dont just make the probability 0 when multiplied.
  spamFreq = spamFreqDict.get(word,0)
  spamProb = (spamFreq+1)/(a+v)
  spamScore+=math.log(spamProb)
  
  hamFreq = hamFreqDict.get(word,0)
  hamProb = (hamFreq+1)/(b+v)
  hamScore+=math.log(hamProb)
    
if spamScore>hamScore:
  print("Spam mail!!")
else:
  print("Normal mail!!!")