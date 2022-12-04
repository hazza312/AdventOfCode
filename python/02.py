from sys import stdin

ROCK, PAPER, SCISSORS = 'ABC'
LOSER_OF = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}
WEIGHTS = {ROCK: 1, PAPER: 2, SCISSORS: 3}
WIN_SCORE, DRAW_SCORE = 6, 3

lines = stdin.read().splitlines()

def get_score_1(line):
	round = line.split()
	opponent, player = round[0], chr(ord(round[1]) - ord('X') + ord('A'))

	if opponent == player:
		return WEIGHTS[player] + DRAW_SCORE

	return WEIGHTS[player] + (opponent == LOSER_OF[player]) * WIN_SCORE

print(sum(map(get_score_1, lines)))


# part 2
WINNER_OF = dict((b, a) for a, b in LOSER_OF.items())
WANT_LOSE, WANT_DRAW, WANT_WIN = 'XYZ'

def get_score_2(line):
	opponent, goal = line.split()
	if goal == WANT_LOSE:
		return WEIGHTS[LOSER_OF[opponent]]

	elif goal == WANT_DRAW:
		return DRAW_SCORE + WEIGHTS[opponent]

	return WIN_SCORE + WEIGHTS[WINNER_OF[opponent]]


print(sum(map(get_score_2, lines)))
