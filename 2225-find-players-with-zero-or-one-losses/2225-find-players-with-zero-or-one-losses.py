from collections import Counter

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        losses = Counter()
        players = set()

        # 1. Registrar las derrotas y el total de jugadores en O(N)
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losses[loser] += 1

        # 2. Clasificar según la cantidad de derrotas
        no_losses = []
        one_loss = []

        for player in players:
            if losses[player] == 0:
                no_losses.append(player)
            elif losses[player] == 1:
                one_loss.append(player)

        # 3. Ordenar los resultados finales
        no_losses.sort()
        one_loss.sort()

        return [no_losses, one_loss]