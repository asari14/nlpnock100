"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．

[Ref]
https://nlp100.github.io/ja/ch02.html

[Unix]
"""

dic = {}
with open("inputs/popular-names.txt", encoding="utf-8") as file:
    for line in file:
        cur_type = line.rstrip().split("	")[0]
        if cur_type not in dic:
            dic[cur_type] = 0
        else:
            dic[cur_type] = dic[cur_type] + 1

print(sorted(dic.items(), key=lambda x: x[1], reverse=True))

# [('James', 117), ('William', 110), ('John', 107), ('Robert', 107), ('Mary', 91), ('Charles', 74), ('Michael', 73), ('Elizabeth', 72), ('Joseph', 69), ('Margaret', 59), ('George', 57), ('Thomas', 57), ('David', 56), ('Richard', 50), ('Helen', 44), ('Frank', 42), ('Christopher', 42), ('Anna', 40), ('Edward', 39), ('Ruth', 38), ('Patricia', 37), ('Matthew', 36), ('Dorothy', 35), ('Emma', 34), ('Barbara', 31), ('Daniel', 30), ('Joshua', 30), ('Sarah', 25), ('Linda', 25), ('Jennifer', 25), ('Emily', 25), ('Jessica', 24), ('Jacob', 24), ('Mildred', 23), ('Betty', 23), ('Susan', 23), ('Henry', 22), ('Ashley', 22), ('Nancy', 21), ('Andrew', 20), ('Florence', 19), ('Marie', 19), ('Donald', 19), ('Amanda', 19), ('Samantha', 18), ('Karen', 17), ('Lisa', 17), ('Melissa', 17), ('Madison', 17), ('Olivia', 17), ('Stephanie', 16), ('Abigail', 16), ('Ethel', 15), ('Sandra', 15), ('Mark', 15), ('Frances', 14), ('Carol', 14), ('Angela', 14), ('Michelle', 14), ('Heather', 14), ('Ethan', 14), ('Isabella', 14), ('Shirley', 13), ('Kimberly', 13), ('Amy', 13), ('Ava', 13), ('Virginia', 12), ('Deborah', 12), ('Brian', 12), ('Jason', 12), ('Nicole', 12), ('Hannah', 12), ('Sophia', 12), ('Minnie', 11), ('Bertha', 11), ('Donna', 11), ('Cynthia', 10), ('Alice', 9), ('Doris', 9), ('Ronald', 9), ('Brittany', 9), ('Nicholas', 9), ('Mia', 9), ('Noah', 9), ('Joan', 8), ('Debra', 8), ('Tyler', 8), ('Ida', 7), ('Clara', 7), ('Judith', 7), ('Taylor', 7), ('Alexis', 7), ('Alexander', 7), ('Mason', 7), ('Harry', 6), ('Sharon', 6), ('Steven', 6), ('Tammy', 6), ('Brandon', 6), ('Liam', 6), ('Anthony', 5), ('Annie', 4), ('Gary', 4), ('Jeffrey', 4), ('Jayden', 4), ('Charlotte', 4), ('Lillian', 3), ('Kathleen', 3), ('Justin', 3), ('Austin', 3), ('Chloe', 3), ('Benjamin', 3), ('Evelyn', 2), ('Megan', 2), ('Aiden', 2), ('Harper', 2), ('Elijah', 2), ('Bessie', 1), ('Larry', 1), ('Rebecca', 1), ('Lauren', 1), ('Amelia', 1), ('Logan', 1), ('Oliver', 1), ('Walter', 0), ('Carolyn', 0), ('Pamela', 0), ('Lori', 0), ('Laura', 0), ('Tracy', 0), ('Julie', 0), ('Scott', 0), ('Kelly', 0), ('Crystal', 0), ('Rachel', 0), ('Lucas', 0)]
