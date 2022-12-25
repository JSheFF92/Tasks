def solution(string, ending):
    print(string.endswith(ending))

    last_sym = string[2:]

    if last_sym == ending or ending == '':
        print('True')
    else:
        print('False')


if __name__ == "__main__":
    solution('samurai', '')
