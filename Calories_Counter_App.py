class Food:
    __protein=float
    __carbs=float
    __fat=float
    __calories=int
    __name=str
    __serving=int
    __unit=str
    
    def __init__(self, n, p, c, f, cal ,s, u):
        self.__name = n
        self.__protein = p
        self.__carbs = c
        self.__fat = f
        self.__calories = cal
        self.__serving=s
        self.__unit=u
        
    def getName(self):
        return self.__name
    
    def getProtein(self):
        return self.__protein
        
    def getCarbs(self):
        return self.__carbs
    
    def getFat(self):
        return self.__fat
    
    def getCalories(self):
        return self.__calories
    
    def getServing(self):
        return self.__serving
    
    def getUnit(self):
        return self.__unit
    
    def setServ(self,s):
        self.__serving=s
        
    def totalProtein(self):
        if self.__unit=="gram":
            return self.__protein*(self.__serving/100)
        else:
            return self.__protein*self.__serving
        
    def totalCarbs(self):
        if self.__unit=="gram":
            return self.__carbs*(self.__serving/100)
        else:
            return self.__carbs*self.__serving
        
    def totalFat(self):
        if self.__unit=="gram":
            return self.__fat*(self.__serving/100)
        else:
            return self.__fat*self.__serving
        
    def totalCalories(self):
        if self.__unit=="gram":
            return self.__calories*(self.__serving/100)
        else:
            return self.__calories*self.__serving
      
class Person:
    __name=str
    __age=int
    __gender=str
    __weight=float
    __height=float 
    __target=float
    
    def __init__(self, fn=" ", a=0,g=" ", w=0, h=0, t=0):
        self.__name = fn
        self.__age = a
        self.__gender=g
        self.__weight = w
        self.__height = h
        self.__target = t
        
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    def getGender(self):
        return self.__gender
    
    def getWeight(self):
        return self.__weight
    
    def getHeight(self):
        return self.__height
    
    def getBMI(self):
        return self.__weight/(self.__height/100)**2
    
    def getTarget(self):
        return self.__target
    
    def setName(self,n):
        self.__name=n
        
    def setAge(self,a):
        self.__age=a
        
    def setGender(self,g):
        self.__gender=g
        
    def setWeight(self,w):
        self.__weight=w
        
    def setHeight(self,h):
        self.__height=h
        
    def setTarget(self,t):
        self.__target=t        

class PhoBo(Food):
    def __init__(self,s):
        super().__init__("Pho Bo",18,59,12,414,s,"bowl")        
    
class BanhCuon(Food):
    def __init__(self,s):
        super().__init__("Banh Cuon",26,65,26,590,s,"dish")       

class BanhMi(Food):
    def __init__(self,s):
        super().__init__("Banh Mi",7.9,52.6,0.8,249,s,"gram")
    
class BanhBao(Food):
    def __init__(self,s):
        super().__init__("Banh Bao",6.1,47.5,0.5,219,s,"gram")

class BunMoc(Food):
    def __init__(self,s):
        super().__init__("Bun Moc",28.1,59.3,19.4,514,s,"bowl")
 
class BunRieu(Food):
    def __init__(self,s):
        super().__init__("Bun Rieu",17.8,60.8,12.2,414,s,"bowl")
 
class BanhTrang(Food):
    def __init__(self,s):
        super().__init__("Banh Trang",6.1,78.9,0.2,333,s,"gram")
        
class PhoGa(Food):
    def __init__(self,s):
        super().__init__("Pho Ga",21.3,61.6,18,483,s,"bowl")
 
class Xoi(Food):
    def __init__(self,s):
        super().__init__("Xoi",1.8,27.9,2.5,138,s,"gram")
        
class MiGoi(Food):
    def __init__(self,s):
        super().__init__("Mi Goi",8.1,52.3,7.8,312,s,"pack")
 
class ChaoLong(Food):
    def __init__(self,s):
        super().__init__("Chao Long",30.8,42.5,13.5,412,s,"bowl")
   
class BanhGio(Food):
    def __init__(self,s):
        super().__init__("Banh Gio",13,38,10,300,s,"cake")
    
class KhoaiLang(Food):
    def __init__(self,s):
        super().__init__("Khoai Lang",0.8,28.5,0.2,119,s,"gram")
   
class ChaoSuon(Food):
    def __init__(self,s):
        super().__init__("Chao Suon",12.9,50.7,6.9,328,s,"bowl")
      
class BunBo(Food):
    def __init__(self,s):
        super().__init__("Bun Bo",12.5,68.2,5.7,376,s,"bowl")
   
class ComTrang(Food):
    def __init__(self,s):
        super().__init__("Com Trang",2,28.9,0.2,130,s,"gram")
 
class ComTam(Food):
    def __init__(self,s):
        super().__init__("Com Tam",20.7,82,13.3,527,s,"dish")
    
class ComRangDuaBo(Food):
    def __init__(self,s):
        super().__init__("Com Rang Dua Bo",20,61,20,496,s,"dish")
  
class Takoyaki(Food):
    def __init__(self,s):
        super().__init__("Takoyaki",4,15,2.5,100,s,"ball")
  
class Ramen(Food):
    def __init__(self,s):
        super().__init__("Ramen",5,26,7,190,s,"cup")
  
class Udon(Food):
    def __init__(self,s):
        super().__init__("Udon",12,66,1,400,s,"bowl")
   
class Pizza(Food):
    def __init__(self,s):
        super().__init__("Pizza",9,26,5,180,s,"slice")
 
class Hamburger(Food):
    def __init__(self,s):
        super().__init__("Hamburger",31,42,37,640,s,"burger")
  
class HotDog(Food):
    def __init__(self,s):
        super().__init__("Hot Dog",7,1.7,17,189,s,"hot dog")
 
class GaRan(Food):
    def __init__(self,s):
        super().__init__("Ga Ran",17,7,17,250,s,"gram")
 
class Kem(Food):
    def __init__(self,s):
        super().__init__("Kem",6,40,15,316,s,"cup")
  
class BanhNgot(Food):
    def __init__(self,s):
        super().__init__("Banh Ngot",0,66.9,12,370,s,"slice")
  
class Chocolate(Food):
    def __init__(self,s):
        super().__init__("Chocolate",0.5,4.2,3.1,46,s,"piece")
   
class Chips(Food):
    def __init__(self,s):
        super().__init__("Chips",2,15,10,150,s,"bag")
  
class UcGa(Food):
    def __init__(self,s):
        super().__init__("Uc Ga",31,0,3.6,165,s,"gram")
   
class Bo(Food):
    def __init__(self,s):
        super().__init__("Thit Bo",26,0,3.3,135,s,"gram")
  
class CaChep(Food):
    def __init__(self,s):
        super().__init__("Ca chep",20,0,5,105,s,"gram")
  
class Tom(Food):
    def __init__(self,s):
        super().__init__("Tom",20,0,0.5,85,s,"gram")
  
class DuiGa(Food):
    def __init__(self,s):
        super().__init__("Dui Ga",17,0,15,211,s,"gram")
  
class Heo(Food):
    def __init__(self,s):
        super().__init__("Thit Heo",27,0,12,215,s,"gram")
  
class Trau(Food):
    def __init__(self,s):
        super().__init__("Thit Trau",21,0,3.5,117,s,"gram")
   
class De(Food):
    def __init__(self,s):
        super().__init__("Thit De",20,0,3.5,105,s,"gram")
   
class Ngan(Food):
    def __init__(self,s):
        super().__init__("Thit Ngan",20,0,1.5,85,s,"gram")
   
class Cua(Food):
    def __init__(self,s):
        super().__init__("Cua",18,0,0.5,82,s,"gram")
        
class Vit(Food):
    def __init__(self,s):
        super().__init__("Thit Vit",16,0,28,337,s,"gram")
  
class Chim(Food):
    def __init__(self,s):
        super().__init__("Thit Chim",20,0,5,120,s,"gram")
   
class Tao(Food):
    def __init__(self,s):
        super().__init__("Tao",0.3,14,0.2,52,s,"apple")
  
class Chuoi(Food):
    def __init__(self,s):
        super().__init__("Chuoi",1.3,27,0.4,105,s,"banana")
   
class Dao(Food):
    def __init__(self,s):
        super().__init__("Dao",0.9,9,0.1,44,s,"peach")
  
class Nho(Food):
    def __init__(self,s):
        super().__init__("Nho",0.6,18,0.2,69,s,"grape")
    
class RauCai(Food):
    def __init__(self,s):
        super().__init__("Rau Cai",1.6,2.2,0.2,14,s,"gram")
   
class RauDen(Food):
    def __init__(self,s):
        super().__init__("Rau Den",1.6,2.2,0.2,14,s,"gram")
   
class RauMuong(Food):
    def __init__(self,s):
        super().__init__("Rau Muong",1.6,2.2,0.2,14,s,"gram")
  
class Trung(Food):
    def __init__(self,s):
        super().__init__("Trung",6,1.1,5,68,s,"egg")
  
class SuaBo(Food):
    def __init__(self,s):
        super().__init__("Sua Bo",7,11,8,150,s,"cup")
        
class Manager:
    food_list=[]
    
    def add(self,n):
        self.food_list.append(n)
        
    def remove(self,n):
        self.food_list.remove(n)
        
    def totalCalories(self):
        total=0          
        for item in self.food_list:
            total+=item.totalCalories()         
        return total
    
    def totalProtein(self):
        total=0
        for item in self.food_list:
            total+=item.totalProtein()           
        return total
        
    def totalCarbs(self):
        total=0
        for item in self.food_list:
            total+=item.totalCarbs()           
        return total
    
    def totalFat(self):
        total=0
        for item in self.food_list:
            total+=item.totalFat()
        return total
    
    def CalfromCarbs(self):
        return self.totalCarbs()*4
    
    def CalfromProtein(self):
        return self.totalProtein()*4
    
    def CalfromFat(self):
        return self.totalFat()*9