class School:
    boyz = 0 
    girlz = 0
    people = boyz + girlz

    def __init__(self, name, new_boyz, new_girlz):
        self.new_boyz = new_boyz
        self.new_girlz = new_girlz

        School.boyz += self.new_boyz
        School.girlz += self.new_girlz

    def __del__(self):
        School.boyz -= self.new_boyz
        School.girlz -= self.new_girlz


ITE = School("ITE", 50, 50) 
IT = School("IT", 50, 50) 
GA = School("GA", 50, 50) 


print(School.boyz)