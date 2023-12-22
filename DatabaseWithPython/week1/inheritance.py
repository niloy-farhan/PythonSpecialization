class party_animal:
    x = 0
    name = ""

    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")

    def party(self):
        self.x += 1
        print(self.name, "party count", self.x)


class fan(party_animal):
    y = 0

    def extra(self):
        self.y += 7
        print(self.name, "party count", self.x, "extra credit", self.y)


s = party_animal("Sally")
a = fan("Adam")

a.party()
a.extra()
s.party()

