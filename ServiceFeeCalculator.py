class ServiceFeeCalculator:
    def __init__(self,supporters_set,specials_map,standard_fee):
        self.supporters_set = supporters_set
        self.specials_map = specials_map
        self.standard_fee = standard_fee

    def calculate(self, ktAddress):
        service_fee=self.standard_fee

        if ktAddress in self.supporters_set:
            service_fee=0.0
        elif ktAddress in self.specials_map:
            service_fee=self.specials_map[ktAddress]

        return service_fee


