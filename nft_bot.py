


class test:
  
  
  def f1(self,prenom="boaz"):
     print("le nom:",prenom)
     
  def m(self):
      print("hello")
      self.f1()


if __name__== "__main__":
      t = test()
      t.m()