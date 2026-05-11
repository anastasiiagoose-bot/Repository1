# file = open('requirements.txt')
#
# content = file.read()
# print(content)
# file.seek(0)
# content = file.read()
# print(content)
# # 1/0
#
# file.close()
# content = file.read()
# ...


# open file
with open('README.md', mode='r', encoding='utf-8') as file:
    # # all rows
    # content = file.read()
    # print(content)

    # # all rows as list of strings
    # lines = file.readlines()
    # print(lines)
    # for line in lines:
    #     # '\n\n'
    #     print(line, end='')

    flag = True
    while flag:
        line = file.readline()
        # print(line, end='')

        if 'tornado' in line:
            break
        if not line:
            # break
            flag = False

# read file
# with open('new.txt', mode='w', encoding='utf-8') as file:
with open('new.txt', mode='a', encoding='utf-8') as file:
    file.write('first line1\n')
    file.write('second line\n')


with open('logs.csv', mode='a', encoding='utf-8') as file:
    file.write('Alex;Bush;167654;Los Angeles\n')

print()


# binary files
# import requests
#
# url = 'https://moemisto.ua/img/cache/blog_show_photo/blog/0004/75/fe2a5835d6d62a84d64cc357061c8186a244a1a8.jpeg'
#
# response = requests.get(url)
# content = response.content
# print(content)


# with open('spring.jpeg', mode='bw') as image_file:
#     image_file.write(content)

# with open('spring.jpeg', mode='br')  as image_file:
#     print(image_file.read())

# with open('spring.jpeg', mode='ba')  as image_file:
#     image_file.write(b' hello 5655 =-00')


# JSON
import json

# dict -> json

user_data_as_dict = {
    'name': "Василь",
    'age': 18,
    "more_data": None,
    'hobbies': ['tennis']
}

user_data_as_json = json.dumps(user_data_as_dict, ensure_ascii=False)
# print(user_data_as_json)

# json -> dict

user_data_from_json = json.loads(user_data_as_json)
# print(user_data_from_json)

# dict -> file.json

with open('user_data.json', mode='w', encoding='utf-8') as file:
    json.dump(user_data_from_json, file, ensure_ascii=False, indent=4)

# file.json -> dict
with open('user_data.json', mode='r', encoding='utf-8') as file:
    user_data_from_file = json.load(file)
    print(user_data_from_file)


