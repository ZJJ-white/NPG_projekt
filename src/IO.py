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
    Statistics = {'stateasy':([]),'statmedium':([]),'stathard':([])} #trzeba zmienić żeby pasowało 
    path = os.path.join(os.path.abspath(__file__), "..", "..", 'stats')

    with open(os.path.join(path, 'StatsEasy.txt'), 'rt', encoding='utf-8') as file:
        for line in file:
            Statistics['stateasy'].append(line.strip())

    with open(os.path.join(path, 'StatsMedium.txt'), 'rt', encoding='utf-8') as file:
        for line in file:
            Statistics['statmedium'].append(line.strip())

    with open(os.path.join(path, 'StatsHard.txt'), 'rt', encoding='utf-8') as file:
        for line in file:
            Statistics['stathard'].append(line.strip())

    return Statistics

def save_stats(Statistic):
    path = os.path.join(os.path.abspath(__file__), "..", "..", 'stats')

    with open(os.path.join(path, 'StatsEasy.txt'), 'w', encoding='utf-8') as file:
        for word in Statistic['stateasy']:
            file.write(word + "\n")
            
    with open(os.path.join(path, 'StatsMedium.txt'), 'w', encoding='utf-8') as file:
        for word in Statistic['statmedium']:
            file.write(word + "\n")

    with open(os.path.join(path, 'StatsHard.txt'), 'w', encoding='utf-8') as file:
        for word in Statistic['stathard']:
            file.write(word + "\n")
    