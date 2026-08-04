class Solution:

    def encode(self, strs: List[str]) -> str:
        start = "<s>"
        result = ""

        for s in strs:
            result += (s + start)
        
        return result

    def decode(self, s: str) -> List[str]:
        result = s.split("<s>")
        return result[:-1]
