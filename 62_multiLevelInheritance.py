class Dad:
    basketball = 1
    football = 5
    def isfootball(self):
        return f"Yes I can play Football {self.football} no of times"


class Son(Dad):
    dance = 3
    basketball = 2
    football = 3

    def isdance(self):
        return f"Yes I can dance {self.dance} no. of times"


class GrandSon(Son):
    football = 7
    dance = 2



ram = Dad()
shyam = Son()
krish = GrandSon()

print(krish.dance)
print(krish.isdance())
print(krish.isfootball())
print(shyam.isfootball())