from datetime import date
class User:
    def __init__(self,date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

def legal_age_only(func):
    def wrapper(user):
        if user.age < 18:
            raise ValueError('You are not of legal age')
        func(user)
    return wrapper

user1 = User(date(1997,2,10))

@legal_age_only
def enroll_user(user:User):
    print(f'You are of legal age, you have {user.age} years old!!! Now you are enrolled')

enroll_user(user1)

@legal_age_only
def get_drive_license(user:User):
    print(f'Here is your Drive License, you are already  {user.age} years old!!!')

get_drive_license(user1)