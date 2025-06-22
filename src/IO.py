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

def load_saves():
    path = os.path.join(os.path.abspath(__file__), "..", "..", 'saves')
    file_path = os.path.join(path, 'save.txt')
    saves = []

    if not os.path.exists(file_path):
        return saves  
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                
                parts = line.split(';')
                if len(parts) == 4:
                    nick, difficulty, score, remaining_time = parts
                    saves.append({
                        'nick': nick,
                        'difficulty': difficulty,
                        'score': int(score),
                        'remaining_time': int(remaining_time)
                    })
    return saves

def save_saves(score, remaining_time, nick, difficulty):

    path = os.path.join(os.path.abspath(__file__), "..", "..", 'saves')
    file_path = os.path.join(path, 'save.txt')

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"{nick};{difficulty};{score};{remaining_time}\n")

def remove_saves(index=0):
    path = os.path.join(os.path.abspath(__file__), "..", "..", 'saves')
    file_path = os.path.join(path, 'save.txt')
    if os.path.exists(file_path):
        os.remove(file_path)