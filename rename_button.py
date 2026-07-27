import os
import glob

files = glob.glob('case-studies/*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('All Case Studies', 'All Projects')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
