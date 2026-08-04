class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0
        mp = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                mp[guess[i]] = mp.get(guess[i], 0) + 1

        for i in range(len(secret)):
            if secret[i] != guess[i]:
                if mp.get(secret[i], 0) > 0:
                    cows += 1
                    mp[secret[i]] -= 1

        return str(bulls) + "A" + str(cows) + "B"