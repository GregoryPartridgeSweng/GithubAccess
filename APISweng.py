import requests
import numpy as np
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
new_data = (total_languages_used(new_data))


languages = []
times_languages_used = []

for p in range(len(new_data)):
    languages.append(new_data[p][0])
    times_languages_used.append(new_data[p][1])

print(languages)
print(times_languages_used)

# PLOTTING

fig, ax = plt.subplots(figsize=(6, 4), subplot_kw=dict(aspect="equal"))

wedges, texts = ax.pie(times_languages_used, wedgeprops=dict(width=0.6, edgecolor = 'black'), startangle=45)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(languages[i]+" :"+(str)(times_languages_used[i]), xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)

ax.set_title("Languages and how much they were used")

plt.show()
