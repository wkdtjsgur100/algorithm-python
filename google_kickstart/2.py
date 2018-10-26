def solution(S):
    # write your code in Python 3.6
    sentences = []
    for dot in S.split("."):
        for question in dot.split("?"):
            for exclamation in question.split("!"):
                sentences.append(exclamation.strip())
    ans = 0
    for sentence in sentences:
        if sentence:
            if ans < len(sentence.split()):
                ans = len(sentence.split())


print(solution("We test coders. Give us a try?"))
