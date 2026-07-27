import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'[ \t]*<div class="visual-proof-needed".*?</div>\n', '', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
