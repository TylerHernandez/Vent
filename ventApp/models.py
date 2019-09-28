class VentUser:

    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def __str__(self ):
        return self.name + " " + self.phoneNumber



class VentDoctor(VentUser)

    def __init__(self, name, phoneNumber):
        VentUser.__init__(self, name, phoneNumber)
