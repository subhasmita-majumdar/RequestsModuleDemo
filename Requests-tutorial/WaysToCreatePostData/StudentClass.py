class Students:
    def __init__(self,name,location,phone,courses):
        self.name = name
        self.location = location
        self.phone = phone
        self.courses = courses

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if len(name)<2:
            raise ValueError("Name must have atleast 2 characters")
        self._name=name

    @property
    def location(self):
        return self._location
    @location.setter
    def location(self,location):
        if len(location)<2:
            raise ValueError("Location must have atleast 2 characters")
        self._location = location

    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self,phone):
        if len(phone)<10:
            raise ValueError("Phone number cannot be less that 10 digits")
        self._phone = phone

    @property
    def courses(self):
        return self._courses
    @courses.setter
    def courses(self,courses):
        if len(courses) == 0:
            raise IndexError("List is empty")
        self._courses = courses

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "phone no": self.phone,
            "courses": self.courses,
        }
