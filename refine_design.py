import re

with open('acts29_gen3.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Increase R values (border-radius)
html = html.replace('rounded-2xl', 'rounded-[2.5rem]')
html = html.replace('rounded-xl', 'rounded-[2rem]')

# 2. Fix card-on-card in line 531 if it still exists
html = re.sub(r'glass-card max-w-\[800px\] mx-auto p-10 mb-16', 'max-w-[800px] mx-auto mb-16 px-8', html)

# 3. Enhance logo overlay
html = html.replace('bg-primary-container/10 mix-blend-overlay', 'bg-primary-container/20 mix-blend-soft-light')

with open('acts29_gen3.html', 'w', encoding='utf-8') as f:
    f.write(html)
