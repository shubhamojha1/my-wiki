from html.parser import HTMLParser
import sys

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
    
    def handle_data(self, data):
        text = data.strip()
        if text:
            self.text.append(text)

content = open(r'C:\Users\subha\.local\share\opencode\tool-output\tool_dd0729f50001Hmx6TE3XPBc2X9', encoding='utf-8').read()
parser = TextExtractor()
parser.feed(content)
with open(r'C:\Users\subha\Projects\my-wiki\extracted_full.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(parser.text))
print("Done")
