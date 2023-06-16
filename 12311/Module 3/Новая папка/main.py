import  os

def Factorial(number: int):
    if number ==1:
        return number
    return number * Factorial(number-1)

curren_path = os.path.abspath(__file__)
parrent_path = os.path.join(curren_path, '..')
parrent_parrent_path = os.path.join(parrent_path, '..')
print(curren_path)



def get_all_paths(path):
    for i_file in os.listdir(path):
        new_path = os.path.join(path, i_file)
        if os.path.isdir(new_path):
            file = open(i_file, 'a', encoding='utf-8')
            file.close()
            print('Директория -->', new_path)
            get_all_paths(new_path,)
        else:
            print('\t -', new_path)

get_all_paths(parrent_parrent_path)