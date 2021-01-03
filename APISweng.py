import requests
import matplotlib.pyplot as plt


def query(username):
    url = 'https://api.github.com/users/' + username + '/repos'
    token = open("APIToken", "r")
    r = requests.get(url, auth=(username, token))
    data = r.json()
    return data


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

data = (query('GregoryPartridgeSweng'))

language_data = []
new_data = []
corresponding_users_to_data = []


language_data.insert(len(language_data), how_much_language_used("GregoryPartridgeSweng"))
corresponding_users_to_data.insert(len(corresponding_users_to_data), "GregoryPartridgeSweng")

for p in range(len(language_data)):
    string = language_data[p]
    #print(corresponding_users_to_data[p]+": "+(str)(string))

for i in range(len(language_data)):
    new_data.insert(i, language_data[i])
#print(total_languages_used(new_data))


languages = []
times_languages_used = []
for q in range(len(new_data)):
    for p in range(len(new_data[q])):
        languages.append(new_data[q][p][0])
        times_languages_used.append(new_data[q][p][1])

#print(languages)
#print(times_languages_used)

# PLOTTING

