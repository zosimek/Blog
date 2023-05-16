from bs4 import BeautifulSoup

def find_class_names():
    file_path = input("filepath: ")
    with open(file_path, 'r') as file:
        content = file.read()
        soup = BeautifulSoup(content, "html.parser")
        lst = [node['class'] for node in soup.find_all() if node.has_attr('class')]


    for x in range(len(lst)):
        print(*lst[x], sep = "\n")

find_class_names()