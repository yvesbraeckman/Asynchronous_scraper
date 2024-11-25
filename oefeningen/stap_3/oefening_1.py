my_home_rolled_counter = {}

for word in list_of_words:

    current_count = my_home_rolled_counter.get(word, 0)

    my_home_rolled_counter[word] = current_count + 1
#Maar een simpelere manier om hetzelfde te bereiken is:

from collections import Counter

better_counter = Counter(list_of_words)