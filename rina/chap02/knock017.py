"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはcut, sort, uniqコマンドを用いよ．

[Ref]
https://nlp100.github.io/ja/ch02.html

[Unix]
"""

types = []
with open("inputs/popular-names.txt", encoding="utf-8") as file:
    for line in file:
        cur_type = line.rstrip().split("	")[0]
        if cur_type not in types:
            types.append(cur_type)

print(set(types))

# {'Pamela', 'Ava', 'Bertha', 'Carol', 'Austin', 'Walter', 'Frank', 'Anthony', 'Ruth', 'Justin', 'Barbara', 'Lucas', 'Mason', 'Harper', 'Kathleen', 'Laura', 'Christopher', 'Marie', 'Ashley', 'Jacob', 'Deborah', 'Kelly', 'George', 'Ida', 'Megan', 'Andrew', 'Jason', 'Angela', 'Chloe', 'Gary', 'Mark', 'Nicholas', 'Brian', 'Jeffrey', 'Carolyn', 'Olivia', 'Frances', 'Richard', 'Logan', 'Madison', 'Melissa', 'Kimberly', 'Charlotte', 'Henry', 'Michelle', 'Harry', 'Doris', 'Scott', 'Charles', 'Amelia', 'Daniel', 'Karen', 'Nicole', 'Emma', 'Steven', 'Brittany', 'Samantha', 'Noah', 'Judith', 'Joan', 'Donald', 'Mary', 'Florence', 'Julie', 'Crystal', 'Virginia', 'Linda', 'Ethel', 'David', 'Alexis', 'Joseph', 'Elizabeth', 'Stephanie', 'Mia', 'Isabella', 'Benjamin', 'Sophia', 'Clara', 'Jayden', 'John', 'Alice', 'Heather', 'Oliver', 'Larry', 'Shirley', 'Abigail', 'Lisa', 'Cynthia', 'Aiden', 'Elijah', 'Debra', 'Rachel', 'Annie', 'William', 'Jessica', 'Lillian', 'Brandon', 'Liam', 'Ethan', 'Helen', 'James', 'Susan', 'Bessie', 'Alexander', 'Michael', 'Tammy', 'Minnie', 'Amanda', 'Sarah', 'Sharon', 'Rebecca', 'Lauren', 'Matthew', 'Anna', 'Taylor', 'Dorothy', 'Lori', 'Emily', 'Joshua', 'Ronald', 'Edward', 'Evelyn', 'Hannah', 'Patricia', 'Betty', 'Amy', 'Nancy', 'Tyler', 'Thomas', 'Jennifer', 'Margaret', 'Tracy', 'Robert', 'Sandra', 'Mildred', 'Donna'}
