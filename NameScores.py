# Josh Gibb

# Extracts information
def loadTextFile(name):
    f = open('Names.txt', 'r')
    content = f.read()
    f.close()
    content = content.replace("\"", "")
    content = content.split(",")
    return content

# Orders the list
def order(name):
    data = loadTextFile(name)
    data.sort()
    return data

# Finds the score of list
def score(name):
    data = order(name)
    score = 0
    pos = 1
    for name in data:
        temp = 0
        for char in name:
            temp += ord(char) - ord('A') +1
        score += temp*pos
        pos += 1
    return score

def main():
    print(score('Names.txt'))

if __name__ == "__main__":
    main()
