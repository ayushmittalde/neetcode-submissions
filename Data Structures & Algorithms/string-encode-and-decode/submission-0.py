class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str=''
        for str in strs:
            encoded_str+=str+'@yush'
        return encoded_str

    def decode(self, s: str) -> List[str]:
        y=s.split('@yush')
        y.pop()
        return y

