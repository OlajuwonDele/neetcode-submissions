class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            word_length = len(word)
            res += str(word_length) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            i = j+1+length
            res.append(word)
        return res