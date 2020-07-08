lst =[]
def countingg_words(filename):
   with open(filename) as f:
       data = f.read()
       lst.append(len(data.split("\n")))

def counting_words(filename):
   with open(filename) as f:
       data = f.read()
       data.replace(",", " ")
       lst.append(len(data.split(" ")))
counting_words("words")
countingg_words("words")
print(lst)