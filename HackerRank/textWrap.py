def wrap(string, max_width):
    res = list(textwrap.wrap(string,max_width))
    return "\n".join(res)
