import re
class Solution:
    def entityParser(self, text: str) -> str:
        chars={"&quot;":"\"",
               "&apos;":"\'",
              "&gt;":">",
              "&lt;":"<",
              "&frasl;":"/",
              "&amp;":"&"}
        for i,j in chars.items():
            text=re.sub(i,j,text)
        return text
