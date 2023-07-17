def reverse_text(text):
    index = len(text) - 1

    while index > -1:
        yield text[index]
        index -= 1


for char in reverse_text("Emil"):
    print(char, end="")  # limE
