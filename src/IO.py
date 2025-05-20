def load_passwords():
    Passwords = {'Hard':[], 'Medium':[], 'Easy':[]}
    
    with open(r"passwords\hard.txt", 'rt', encoding='utf-8') as file:
        for line in file:
            Passwords['Hard'].append(line.strip())

    with open(r"passwords\easy.txt", 'rt', encoding='utf-8') as file:
        for line in file:
            Passwords['Medium'].append(line.strip())

    with open(r"passwords\medium.txt", 'rt', encoding='utf-8') as file:
        for line in file:
            Passwords['Easy'].append(line.strip())

    return Passwords

def save_passwords(Passwords):
    with open(r"passwords\hard.txt", 'w', encoding='utf-8') as file:
        for word in Passwords['Hard']:
            file.write(word + "\n")

    with open(r"passwords\medium.txt", 'w', encoding='utf-8') as file:
        for word in Passwords['Medium']:
            file.write(word + '\n')

    with open(r"passwords\easy.txt", 'w', encoding='utf-8') as file:
        for word in Passwords['Easy']:
            file.write(word + '\n')