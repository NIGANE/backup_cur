def say_hello():
    print("hello world")


res = {
    "name": "res",
    "greeting": say_hello
}
print(res['name'])
print(res["greeting"].__name__)
res["greeting"]()
