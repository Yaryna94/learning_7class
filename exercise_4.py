from faker import Faker

faker = Faker()
class Card:

   def __init__(self, name, surname,  email):
       self.name = name
       self.surname = surname
       #self.company_name = company_name
       #self.adress =adress
       self.email=email
       
      
   @property
   def label_length(self):
        
        return f" long name {len(self.name)} long surname {len(self.surname)}"


class BusinessContact(Card):
    def __init__(self, job, number, adress, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.job = job
       self.number = number
       self.adress = adress
      
    def __str__(self):
     return f'{self.name} {self.surname} {self.job} {self.number}'

    def contact(self):
          return 'Я набираю %s та телефоную %s' %(self.number, self.name) 

    


class BaseContact (Card):
    def __init__(self, phone_number, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.phone_number = phone_number


    def __str__(self):
     return f'{self.name} {self.surname} {self.email} {self.phone_number}'

    
    def contact(self):
          return 'Я набираю %s та телефоную %s' %(self.phone_number, self.name)
    
    
def create_contacts():

 type_card=input('''Введи тип візитки. Приватна-1, робоча-2:  ''')
 number_card=int(input('Введи кількість: '))
 name = faker.name
 surname=faker.last_name
 phone_number=faker.phone_number
 email = faker.email
 job=faker.job
 compani_name=faker.company
 adress=faker.address
 number=faker.phone_number
 
 if type_card == '1':
   for i in range(number_card):
      print(BaseContact(faker.name(),faker.last_name(), faker.phone_number(),faker.email()))
   
 elif type_card =="2":
    for _ in range(number_card):
        print (BusinessContact(faker.name() , faker.last_name(), faker.job(), faker.address(), faker.phone_number(), faker.email()))

 
  
if __name__ == "__main__":
    

 basecontact_1 = BaseContact(name='Johnnie',surname='Harwell', phone_number=+480545698222, email = "csdcsd@gbbf.ggb")
 basecontact_2 = BaseContact(name='Shelley', surname='Gibson', phone_number= '+4805458587133', email='bsdfgb@fghnryh')
 card_3 = BusinessContact(name='Darrell', surname='Sanchez', job='Zany_Brainy', adress ='1567 Marigold Lane_Pompano_Beach',email='DarrellMSanchez@teleworm.us'  ,number='546845')
 card_4 = BusinessContact(name='Robert', surname='Petty', job='Warner_Brothers_Studio_Store', adress='684 Lena Lane_Jackson',email='RobertKPetty@armyspy.com',number='5896332')
 card_5 = BusinessContact(name='Phillip', surname='Brown', job='Leos_Stereo', adress='2968_Pickens_Way_Athens', email='PhillipJBrown@dayrep.com',number='8546985')
 

print(basecontact_1.contact())
#print(card_3.label_length)


#create_contacts()