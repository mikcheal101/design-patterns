text = 'hello'
parts = ['<p>', text, '</p>']
print(''.join(parts))

words = ['lorem', 'ipsume', 'is', 'a', 'vocabulary', 'on', 'its', 'own']
parts = ['<ul>']
for word in words:
    parts.append(f'    <li>{word}</li>')
parts.append('</ul>')
print('\n'.join(parts))