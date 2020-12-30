import requests
import json
import os


def query(username):
    url = 'https://api.github.com/users/' + username + '/repos'
    token = open("APIToken", "r")
    r = requests.get(url, auth=(username, token))
    data = r.json()
    return data


def return_all_projects(username):
    return_data = []
    data = query(username)

    for r in data:
        return_data.append(r['name'])
    return return_data


def language_used(username):
    return_data = []
    data = query(username)

    for j in data:
        if j['language'] is not None:
            return_data.append(j['language'])

    return return_data


def return_all_projects_size(username):
    return_data = []
    data = query(username)

    for r in data:
        return_data.append(r['size'])
    return return_data


def largest_project(username):
    data = query(username)
    max_size = 0

    for j in data:
        if j['size'] > max_size:
            max_size = j['size']
    return max_size


def smallest_project(username):
    data = query(username)
    min_size = 0

    for j in data:

        if j['size'] < min_size or min_size < 0:
            min_size = j['size']
    return min_size


def average_project_size(username):
    data = query(username)

    product = 0
    total_software_projects = 0

    for j in data:
        if j['language'] is not None:
            product += j['size']
            total_software_projects += 1
    average = round((product / total_software_projects), 2)
    return average


def how_much_language_used(username):
    all_languages = []
    times_used = []
    found_language = False

    data = query(username)

    for j in data:
        if j['language'] is not None:
            for i in range(len(all_languages)):
                if j['language'] == all_languages[i]:
                    times_used[i] += 1
                    found_language = True
            if not found_language:
                all_languages.append(j['language'])
                times_used.append(1)
            found_language = False

    return_data = []
    for l in range(len(all_languages)):
        return_data.insert(len(return_data), [all_languages[l], times_used[l]])

    return_data = sort_data(return_data)
    #print(return_data)

    return return_data

def sort_data(data):

    holder = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[j][1] > data[i][1]:
                holder = data[j]
                data[j] = data[i]
                data[i] = holder
    return data


def total_languages_used(data):
    all_languages = []
    times_used = []
    found_language = False

    for k in range(len(data)):
        for j in range(len(data[k])):
            for i in range(len(all_languages)):
                if data[k][j][0] == all_languages[i]:
                    times_used[i] += data[k][j][1]
                    found_language = True
            if not found_language:
                all_languages.append(data[k][j][0])
                times_used.append(data[k][j][1])
            found_language = False

    return_data = []
    current_spot = 0
    for l in range(len(all_languages)):
        return_data.insert(current_spot, [all_languages[l], times_used[l]])
        current_spot += 1

    return_data = sort_data(return_data)

    return return_data


# TESTING

#print(json.dumps(query('GregoryPartridgeSweng'), indent = 5))

# print(return_all_projects('GregoryPartridgeSweng'))

# print(language_used('GregoryPartridgeSweng'))

# print(return_all_projects_size('GregoryPartridgeSweng'))

# print(largest_project('GregoryPartridgeSweng'))

# print(smallest_project('GregoryPartridgeSweng'))

# print(average_project_size("GregoryPartridgeSweng"))
language_data = []
new_data = []
corresponding_users_to_data = []


language_data.insert(len(language_data), how_much_language_used("GregoryPartridgeSweng"))
corresponding_users_to_data.insert(len(corresponding_users_to_data), "GregoryPartridgeSweng")

#print(corresponding_users_to_data)
#print(language_data)

for p in range(len(language_data)):
    string = language_data[p]
    print(corresponding_users_to_data[p]+": "+(str)(string))

for i in range(len(language_data)):
    new_data.insert(i, language_data[i])

print(total_languages_used(new_data))
