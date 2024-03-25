from collections import defaultdict
import itertools

def create_graph(data):
    graph = defaultdict(dict)
    for line in data.split("\n"):
        if line:
            src, dest, cost = line.split(" ")
            graph[src][dest] = int(cost)
            graph[dest][src] = int(cost)
    return graph

def tsp(graph, start):
    # Generate all possible permutations of cities
    cities = list(graph.keys())
    permutations = itertools.permutations(cities)

    # Initialize variables to store the shortest path and its cost
    shortest_path = None
    shortest_cost = float('inf')

    # Iterate through all permutations and calculate the cost of each path
    for perm in permutations:
        # Ensure that the path starts and ends with the specified start city
        if perm[0] != start or perm[-1] != start:
            continue
        total_cost = 0
        for i in range(len(perm) - 1):
            src = perm[i]
            dest = perm[i + 1]
            # Check if the edge exists in the graph
            if dest in graph[src]:
                total_cost += graph[src][dest]
            else:
                # If the edge does not exist, skip this permutation
                total_cost = float('inf')
                break
        # Update the shortest path and its cost if applicable
        if total_cost < shortest_cost:
            shortest_cost = total_cost
            shortest_path = perm

    return shortest_path, shortest_cost

data = """
Białystok Olsztyn 210
Białystok Warszawa 132
Białystok Lublin 226
Białystok Bydgoszcz 306
Białystok Gdańsk 289
Białystok Łódź 209
Białystok Poznań 306
Białystok Szczecin 448
Białystok GorzówWielkopolski 391
Białystok Wrocław 333
Białystok Opole 343
Białystok Katowice 309
Białystok Kielce 247
Białystok Kraków 327
Białystok Rzeszów 320
Olsztyn Warszawa 161
Olsztyn Lublin 263
Olsztyn Bydgoszcz 187
Olsztyn Gdańsk 114
Olsztyn Łódź 211
Olsztyn Poznań 268
Olsztyn Szczecin 367
Olsztyn GorzówWielkopolski 353
Olsztyn Wrocław 335
Olsztyn Opole 350
Olsztyn Katowice 316
Olsztyn Kielce 273
Olsztyn Kraków 353
Olsztyn Rzeszów 355
Warszawa Lublin 118
Warszawa Bydgoszcz 200
Warszawa Gdańsk 229
Warszawa Łódź 104
Warszawa Poznań 198
Warszawa Szczecin 340
Warszawa GorzówWielkopolski 283
Warszawa Wrocław 225
Warszawa Opole 228
Warszawa Katowice 193
Warszawa Kielce 128
Warszawa Kraków 209
Warszawa Rzeszów 207
Lublin Bydgoszcz 286
Lublin Gdańsk 341
Lublin Łódź 189
Lublin Poznań 287
Lublin Szczecin 429
Lublin GorzówWielkopolski 372
Lublin Wrocław 314
Lublin Opole 319
Lublin Katowice 248
Lublin Kielce 148
Lublin Kraków 211
Lublin Rzeszów 114
Bydgoszcz Gdańsk 116
Bydgoszcz Łódź 155
Bydgoszcz Poznań 97
Bydgoszcz Szczecin 219
Bydgoszcz GorzówWielkopolski 183
Bydgoszcz Wrocław 197
Bydgoszcz Opole 254
Bydgoszcz Katowice 218
Bydgoszcz Kielce 156
Bydgoszcz Kraków 236
Bydgoszcz Rzeszów 238
Gdańsk Łódź 260
Gdańsk Poznań 212
Gdańsk Szczecin 315
Gdańsk GorzówWielkopolski 314
Gdańsk Wrocław 370
Gdańsk Opole 385
Gdańsk Katowice 353
Gdańsk Kielce 313
Gdańsk Kraków 355
Gdańsk Rzeszów 383
Łódź Poznań 140
Łódź Szczecin 284
Łódź GorzówWielkopolski 225
Łódź Wrocław 168
Łódź Opole 185
Łódź Katowice 135
Łódź Kielce 100
Łódź Kraków 182
Łódź Rzeszów 194
Poznań Szczecin 213
Poznań GorzówWielkopolski 163
Poznań Wrocław 154
Poznań Opole 207
Poznań Katowice 172
Poznań Kielce 155
Poznań Kraków 237
Poznań Rzeszów 247
Szczecin GorzówWielkopolski 157
Szczecin Wrocław 293
Szczecin Opole 308
Szczecin Katowice 276
Szczecin Kielce 237
Szczecin Kraków 305
Szczecin Rzeszów 334
GorzówWielkopolski Wrocław 144
GorzówWielkopolski Opole 198
GorzówWielkopolski Katowice 167
GorzówWielkopolski Kielce 122
GorzówWielkopolski Kraków 203
GorzówWielkopolski Rzeszów 215
Wrocław Opole 57
Wrocław Katowice 123
Wrocław Kielce 165
Wrocław Kraków 189
Wrocław Rzeszów 214
Opole Katowice 79
Opole Kielce 126
Opole Kraków 204
Opole Rzeszów 220
Katowice Kielce 83
Katowice Kraków 80
Katowice Rzeszów 161
Kielce Kraków 125
Kielce Rzeszów 125
Kraków Rzeszów 96
"""

graph = create_graph(data)
start_city = 'Warszawa'
shortest_path, shortest_cost = tsp(graph, start_city)
print("Najkrótsza ścieżka między wszystkimi miastami:", shortest_path)
print("Koszt najkrótszej ścieżki:", shortest_cost)
