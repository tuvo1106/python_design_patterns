def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


# decorator
@singleton
class Database:
    def __init__(self):
        print('Loading database')

D1 = Database()
D2 = Database()

print(D1 == D2)
