class Building:

    #constructor
    def __init__(self, season, apartmentNumber, apartmentSize):
        self.season = season
        self.apartmentNumber = apartmentNumber
        self.apartmentSize = apartmentSize

    def rent_calc(self):
        base = 1000
        season_buffer = 0

        if self.season == "summer":
            season_buffer = 1.5

        elif self.season == "winter":
            season_buffer = 1.1

        elif self.season == "spring":
            season_buffer = 1.4

        elif self.season == "autumn":
            season_buffer = 1.3

        else:
            season_buffer = None

        if self.apartmentSize > 130:
            season_buffer += 0.1

            total = base + season_buffer

            #String formatting
            print('The buffer is: %s ' % season_buffer)
            print('The total is: %s ' % total)

        return total




    def monthly_maintainance(self , rent_price):
        maintainance = 0

        if rent_price > 3000:
            maintainance = 100
        else:
            maintainance = 50

            return maintainance


lease_contract_1 = Building("summer", 4, 135)
lease_contract_2 = Building("spring", 6, 100)

lease_contract_1.rent_calc()
print('the maintainance costs: %s' % lease_contract_1.monthly_maintainance(lease_contract_1.rent_calc()))

