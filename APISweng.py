import requests
import numpy as np
import matplotlib.pyplot as plt



def query(username):
    url = 'https://api.github.com/users/' + username + '/repos'
    token = open("APIToken", "r")
    r = requests.get(url, auth=(username, token))
    data = r.json()
    return data


def how_much_language_used(data):
    all_languages = []
    times_used = []
    found_language = False

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

def main_language_corolation(new_data, languages):
    corrolation_table = [[0 for k in range(len(languages))] for j in range(len(languages))]
    languages_used_by_user = []
    for a in range(len(new_data)):
        for b in range(len(new_data[a])):
            for c in range(len(languages)):
                if new_data[a][b][0] == languages[c]:
                    languages_used_by_user.append(new_data[a][b][1])

        add_to_corrolation_table(corrolation_table, languages_used_by_user)
        languages_used_by_user = []

    return corrolation_table

def add_to_corrolation_table(table, lang_used):

    for p in range(len(lang_used)):
        if lang_used[p] == 7 or lang_used[p] == 8 or lang_used[p] == 9 or lang_used[p] == 10:
            print("HERE")

    for i in range(len(lang_used)):
        for k in range(len(lang_used)):
            if lang_used[i] != lang_used[k]:
                table[i][k] += 1
    return table

def most_connected_lang(table):

    language_connected = []
    counter = 0

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] != 0:
                counter += 1
        language_connected.append(counter)
        counter = 0

    return language_connected




# TESTING

#data = (query('GregoryPartridgeSweng'))

users_data = []
language_data = []
new_data = []
corresponding_users_to_data = []

users_data.append(query('GregoryPartridgeSweng')

for i in range(len(users_data)):
    language_data.insert(len(language_data), how_much_language_used(users_data[i]))
    corresponding_users_to_data.insert(len(corresponding_users_to_data), users_data[i])

for p in range(len(language_data)):
    string = language_data[p]
    #print(corresponding_users_to_data[p]+": "+(str)(string))

for i in range(len(language_data)):
    new_data.insert(i, language_data[i])
total_data = (total_languages_used(new_data))


languages = []
times_languages_used = []

for p in range(len(total_data)):
    languages.append(total_data[p][0])
    times_languages_used.append(total_data[p][1])

#print(languages)
#print(times_languages_used)

table = (main_language_corolation(new_data, languages))

most_connected_language = most_connected_lang(table)

for i in range(len(languages)):
    print((str)(languages[i])+": "+(str)(most_connected_language[i]))






# PLOTTING
plt.style.use('seaborn-darkgrid')

plt.rcParams.update({
    "figure.facecolor": "xkcd:wheat",
    "figure.edgecolor": "xkcd:wheat",
    "savefig.facecolor": "xkcd:wheat",
    "savefig.edgecolor": "xkcd:wheat"})

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

plt.style.use('seaborn')
plt.rcdefaults()
fig, ax = plt.subplots()

languages_used = languages
y_pos = np.arange(len(languages_used))
performance = most_connected_language

ax.barh(y_pos, performance, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(languages_used)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Times Used')
ax.set_title('How many languages are conncected to other languages')

plt.show()
