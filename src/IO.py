import os

def load_passwords():
    Passwords = {'Hard':[], 'Medium':[], 'Easy':[]}
    path = os.path.join(os.path.abspath(__file__), "..", "..", 'passwords')

    with open(os.path.join(path, 'hard.txt'), 'rt', encoding='utf-8') as file:
        for line in file:
            Passwords['Hard'].append(line.strip())

    with open(os.path.join(path, "medium.txt"), 'rt', encoding='utf-8') as file:
        for line in file:
            Passwords['Medium'].append(line.strip())

    with open(os.path.join(path, "easy.txt"), 'rt', encoding='utf-8') as file:
        for line in file:
            Passwords['Easy'].append(line.strip())

    return Passwords

def save_passwords(Passwords):
    path = os.path.join(os.path.abspath(__file__), "..", "..", 'passwords')

    with open(os.path.join(path, 'hard.txt'), 'w', encoding='utf-8') as file:
        for word in Passwords['Hard']:
            file.write(word + "\n")

    with open(os.path.join(path, "medium.txt"), 'w', encoding='utf-8') as file:
        for word in Passwords['Medium']:
            file.write(word + '\n')

    with open(os.path.join(path, "easy.txt"), 'w', encoding='utf-8') as file:
        for word in Passwords['Easy']:
            file.write(word + '\n')

            #nowe zmiany - Statystyki

def load_stats():
    Statistics = {'stat1':[],'stat2':[],'stat3':[]} #trzeba zmienić żeby pasowało 
    path = os.path.join(os.path.abspath(__file__), "..", "..", 'stats')

    with open(os.path.join(path, 'statistics.txt'), 'rt', encoding='utf-8') as file:
        for line in file:
            Statistics['stat1'].append(line.strip())

    with open(os.path.join(path, 'statistics2.txt'), 'rt', encoding='utf-8') as file:
        for line in file:
            Statistics['stat2'].append(line.strip())

    with open(os.path.join(path, 'statistics3.txt'), 'rt', encoding='utf-8') as file:
        for line in file:
            Statistics['stat3'].append(line.strip())

    return Statistics

def save_stats(Statistic):
    path = os.path.join(os.path.abspath(__file__), "..", "..", 'stats')

    with open(os.path.join(path, 'statistics.txt'), 'w', encoding='utf-8') as file:
        for word in Statistic['stat1']:
            file.write(word + "\n")
            
    with open(os.path.join(path, 'statistics2.txt'), 'w', encoding='utf-8') as file:
        for word in Statistic['stat2']:
            file.write(word + "\n")

    with open(os.path.join(path, 'statistics3.txt'), 'w', encoding='utf-8') as file:
        for word in Statistic['stat3']:
            file.write(word + "\n")

    # nowe zmiany - Zapisy

def load_saves():
    Saves = {'save-1':[], 'save-2':[], 'save-3':[]}
    path = os.path.join(os.path.abspath(__file__), "..", "..", 'saves')

    with open(os.path.join(path, 'saves1.txt'), 'rt', encoding='utf-8') as file:
        for line in file:
            Saves['save-1'].append(line.strip())

    with open(os.path.join(path, 'saves2.txt'), 'rt', encoding='utf-8') as file:
        for line in file:
            Saves['save-2'].append(line.strip())

    with open(os.path.join(path, 'saves3.txt'), 'rt', encoding='utf-8') as file:
        for line in file:
            Saves['save-3'].append(line.strip())

    return Saves

def save_saves(Saves):
    path = os.path.join(os.path.abspath(__file__), "..", "..", 'saves')

    with open(os.path.join(path, 'saves1.txt'), 'w', encoding='utf-8') as file:
        for word in Saves['save-1']:
            file.write(word + "\n")

    with open(os.path.join(path, 'saves2.txt'), 'w', encoding='utf-8') as file:
        for word in Saves['save-2']:
            file.write(word + "\n")

    with open(os.path.join(path, 'saves3.txt'), 'w', encoding='utf-8') as file:
        for word in Saves['save-3']:
            file.write(word + "\n")
