try:
    num = 100
    print("num divided by 0 ", num / 0)
except Exception as e:
    print(e)
    print(e.__class__.__name__)
