languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

s = "{0} was created by {1}"
for language, author in languages.items():
    print(s.format(language, author))