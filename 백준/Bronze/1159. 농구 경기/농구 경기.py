N = int(input())
player_list = []

for _ in range(N):
    player_list.append(input())

start_alphabet = [p[:1] for p in player_list]

res = []
for alphabet in start_alphabet:
    if len([player for player in player_list if player[0] == alphabet]) >= 5 and alphabet not in res:
        res.append(alphabet)

print("".join(sorted(res)) if len(res) > 0 else 'PREDAJA')