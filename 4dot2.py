def get_cats_info(path):
    cats_info = []
    with open(path, 'r', encoding='utf-8') as fh:
        for line in fh:
            parts = line.strip().split(',')
            if len(parts) == 3:
                id = parts[0].strip()
                name = parts[1].strip()
                age = parts[2].strip()
                info = {'id': id, 'name': name, 'age': age}
                cats_info.append(info)
            else:
                cats_info.append('Помилка')
    return cats_info

cats_info = get_cats_info("E:\\Git\\PROJECTS\\4dz\\cats.txt")
print(cats_info)
