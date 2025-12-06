letter = '''Dear <|name|>,
                you are selected! <|date|>'''

print(letter.replace("<|name|>", "Awais").replace("<|date|>", "24 september 2050"))