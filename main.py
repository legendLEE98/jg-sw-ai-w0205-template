wordDict = ["leet", "code"]
s = "leetcode"

result = []
start = 0
value = 0
word = ""
for i in range(len(s)):
    for j in range(start, i + 1):
        word += s[j]
        print(word)

        if word == wordDict[value]:
            start = i - 1
            value += 1
            result.append(word)
        
    word = ""

print(result)
# for i in range(len(s)):