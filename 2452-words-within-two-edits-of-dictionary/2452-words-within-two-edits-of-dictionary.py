class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        if not queries or not dictionary:
            return []

        paraDevolver = []

        for word1 in queries:
            for word2 in dictionary:
                contador = 0
                for c1, c2 in zip(word1, word2):
                    if c1 != c2:
                        contador += 1
                if(contador <= 2):
                    paraDevolver.append(word1)
                    break
        
        return paraDevolver
