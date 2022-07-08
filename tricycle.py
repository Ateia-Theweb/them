"""Wraparound countdown."""

txt = 'at.txt'

with open(txt, 'rt') as count:
    old = count.read()

new = {
    '@3': '@2',
    '@2': '@1',
    '@1': '@3', }.get(old, '@3')

with open(txt, 'wt') as count:
    count.write(new)

print(new)
