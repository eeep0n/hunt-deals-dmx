class DMXTarget:
    def __init__(self, manufactory, second_parameter):
        self.manufactory = manufactory
        self.second_parameter = second_parameter

    def get_info(self):
        print(f"{self.manufactory} | {self.second_parameter}")


