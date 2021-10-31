PAGE_ACCESS_TOKEN = 'EAAI4mipBnY4BABla6GQS4Ie0RAcgoYIr63FoWQzmUrgSx99SjSYwoL05ZAe1Ta9Qx9xGQ94x3tGCMzHhlkPUOPi7XpQZAaKeH0xnZC7Ha1ZB0AOuDSN0rlQd02Jgp6cyLK1xzuwAGmPi8gZC4nyWsTKVeayaG6TGlxa9O9j9TyReRFgJBzvkTFwcuZBhpoaMsZD'



def func(**kwargs):

    i = 0
    x = len(kwargs)

    print(kwargs)
    buttons = []
    while i<x:

        buttons.append(kwargs)
        i += 3

    return buttons

print(func(type='postback', title="details", payload='bt1'))