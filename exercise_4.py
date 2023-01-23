from faker import Faker

faker = Faker()
class Card:

   def __init__(self, name, surname, company_name, adress,  email):
       self.name = name
       self.surname = surname
       self.company_name = company_name
       self.adress =adress
       self.email=email

class BusinessContact(Card):
    def __init__(self, position, number, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.position = position
       self.number = number
    
    def __str__(self):
     return f'{self.name} {self.surname} {self.position} {self.number}'

    def contact(self):
          return 'Я набираю %s та телефоную %s' %(self.number, self.name) 
   # @property
    def label_length(self):
        
        return f" long name {len(self.name)} long surname {len(self.surname)}"



class BaseContact (Card):
    def __init__(self, personal_phone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.personal_phone = personal_phone




    def __str__(self):
     return f'{self.name} {self.surname} {self.email} {self.personal_phone}'

    
    def contact(self):
          return 'Я набираю %s та телефоную %s' %(self.personal_phone, self.name)
    
    def label_length(self):
        
        return f" long name {len(self.name)} long surname {len(self.surname)}"



def create_contacts():
 aa=input('''Введи тип візитки. Приватна-1, робоча-2:  ''')
 bb=int(input('Введи кількість: '))
 
 if aa == '1':
     
   name = faker.name
   job = faker.job
   email = faker.email()
   personal_phone=faker.phone_number
   compani_name=faker.company()
   for _ in range(bb):
    print( faker.name(), faker.email(), faker.phone_number())

 elif aa =="2":
    for _ in range(bb):
        print(faker.name(), faker.email(), faker.phone_number(), faker.job(), faker.company())

 
        


  
if __name__ == "__main__":
    

 basecontact_1 = BaseContact('Johnnie','Harwell','BMW','4593_Collins_Avenue_Columbus','JohnnieJHarwell@armyspy.com', +480545698222)
 basecontact_2 = BaseContact(name='Shelley', surname='Gibson', company_name='Gottschalks', adress='3434_Daffodil_Lane_Herndon', email='ShelleyWGibson@rhyta.com',personal_phone= '+4805458587133')
 card_3 = BusinessContact(name='Darrell', surname='Sanchez', company_name='Zany_Brainy', adress ='1567 Marigold Lane_Pompano_Beach',email='DarrellMSanchez@teleworm.us', position='kok',number='546845')
 card_4 = BusinessContact(name='Robert', surname='Petty', company_name='Warner_Brothers_Studio_Store', adress='684 Lena Lane_Jackson',email='RobertKPetty@armyspy.com',position='model',number='5896332')
 card_5 = BusinessContact(name='Phillip', surname='Brown', company_name='Leos_Stereo', adress='2968_Pickens_Way_Athens', email='PhillipJBrown@dayrep.com',position='driver',number='8546985')

#print(card_5.contact())
#print(card_3.label_length())

create_contacts()