class FeatureFlag:
    def __init__(self, name):
        self.name = name
        self.enabled = False

    def __repr__(self):
        return f"FeatureFlag(name={self.name}, enabled={self.enabled})"

    def __bool__(self):
        return self.enabled


def load_flag(name):
    raise NotImplemented



def flag(name):
    flag = load_flag(name)
    return bool(flag)
