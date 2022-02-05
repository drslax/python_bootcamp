def kata01(dics):
    for k, v in dics.items():
        print(k, 'was created by', v)

languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

kata01(languages)

