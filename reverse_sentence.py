def reverse(user_input):
    user_input = user_input.replace(".", "")
    txt = user_input
    x = txt.split()
    x.reverse()
    y = " ".join(x)
    y = "".join((y, "."))
    return y
