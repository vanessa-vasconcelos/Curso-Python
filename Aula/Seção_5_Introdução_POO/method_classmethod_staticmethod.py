# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
  def __init__(self, host='hostlocal'):
    self.host = host
    self.user = None
    self.password = None
    
  def set_user(self, user):
    self.user = user
    
  def set_password(self, password):
    self.password = password
    
  @classmethod
  def creat_whit_auth(cls, user, password):
    connection = cls()
    connection.user = user
    connection.password = password
    return connection
  
  @staticmethod
  def log(msg):
    print('Log: ', msg)
    
# c1 = Connection()
cone = Connection.creat_whit_auth('Vanessa', '22')
# c1.set_user('Luiz')
# c1.set_password('123')
# print(c1.user)
# print(c1.password)
print(Connection.log('Essa é a mensagem de log'))
print(cone.user)
print(cone.password)
