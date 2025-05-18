def load_passwords():
    hard = []
    medium = []
    easy = []
    
    with open(r"passwords\hard.txt", 'rt', encoding='utf-8') as file:
        for line in file:
            hard.append(line.strip())

    with open(r"passwords\easy.txt", 'rt', encoding='utf-8') as file:
        for line in file:
            easy.append(line.strip())

    with open(r"passwords\medium.txt", 'rt', encoding='utf-8') as file:
        for line in file:
            medium.append(line.strip())

    return (hard, medium, easy)

def save_passwords(hard, medium, easy):
    with open(r"passwords\hard.txt", 'w', encoding='utf-8') as file:
        for word in hard:
            file.write(word + "\n")

    with open(r"passwords\medium.txt", 'w', encoding='utf-8') as file:
        for word in medium:
            file.write(word + '\n')

    with open(r"passwords\easy.txt", 'w', encoding='utf-8') as file:
        for word in easy:
            file.write(word + '\n')