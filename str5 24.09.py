def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)
while True:
    text = input('Введите текст: ')
    if not text:
        break
    if is_palindrome(text):
        print('да, это палиндром')
    else:
        print('Нет, это не палиндром')