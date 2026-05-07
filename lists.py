
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
        print(line, end='')

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