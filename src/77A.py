n = int(input())

for i in range(n):
    word = input()
    k = len(word)

    if 10 < k:
        print(f"{word[0]}{k - 2}{word[-1]}")
    else:
        print(word)
