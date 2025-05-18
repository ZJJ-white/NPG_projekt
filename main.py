from src import IO

(hard, medium, easy) = IO.load_passwords()

print(f'Hasła trudne: {hard}')
print(f'Hasła średnie: {medium}')
print(f'Hasła łatwe: {easy}')