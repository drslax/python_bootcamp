from string import punctuation


def text_analyzer(*args, **kwargs):

    text_analyzer.__doc__ = "This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."
    # Variable
    p, u, l, s, t = 0, 0, 0, 0, 0
    if len(args) == 0:
        str = input("Enter a Text: \n")
    else:
        str = args[0]
    for c in str:
        if c in punctuation:
            p += 1
        elif (c.isupper()):
            u += 1
        elif (c.islower()):
            l += 1
        elif (c.isspace()):
            s += 1
        t += 1
    print('Punctuation:', p, ' Upper:', u,
          ' Lower:', l, ' Space:', s, ' Total:', t)


text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")
# text_analyzer()
print(text_analyzer.__doc__)
