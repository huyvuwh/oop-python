# class
class chuot:
	pass
 
Chuot1 = chuot()
Chuot1.loai = "chuot cong"

# constructor
class tainghe:
    def __init__(self,para_loai,para_mau):
        self.loai = para_loai
        self.mau = para_mau
    def review(self):
        return(self.loai + " là tai nghe xịn")

        
tainghe1 = tainghe("bluetooth","xanh")

print(tainghe1.loai)
print(tainghe1.mau)
        
tainghe1 = tainghe("bluetooth","xanh")

print(tainghe1.loai)
print(tainghe1.mau)

print(tainghe1.review())

class tainghe:
    so_thu_tu = 1
    pin = 100
    def __init__(self,para_loai,para_mau):
        self.loai = para_loai
        self.mau = para_mau
        self.so_thu_tu = tainghe.so_thu_tu
        tainghe.so_thu_tu += 1
    def review(self):
        return(self.loai + " là tai nghe xịn")
    @classmethod
    def cap_nhat_pin(cls,battery):
        cls.pin = battery
        tainghe1.cap_nhat_pin(45)
        print(tainghe1.pin)

tainghe1 = tainghe("bluetooth","xanh")
tainghe2 = tainghe("có dây","đỏ")

tainghe1.pin = 97
print(tainghe1.pin)
print(tainghe2.pin)
print(tainghe1.so_thu_tu)
print(tainghe2.so_thu_tu)



class tainghe:
    pin = 100
    so_thu_tu = 1
    def __init__(self, para_loai, para_mau):
        self.loai = para_loai
        self.mau = para_mau
        self.so_thu_tu = tainghe.so_thu_tu
        tainghe.so_thu_tu += 1
        
    def review(self):
        return self.loai + " là tai nghe xịn"
    
    @classmethod
    def from_string(cls, s):
        lst = s.split('-')
        new_lst = [st.strip() for st in lst]
        the_loai, mau_sac = new_lst
        return cls(the_loai, mau_sac)
    @staticmethod
    def bum():
        print('Bùm')       
infor_str = "bluetooth - tim"
tainghe3 = tainghe.from_string(infor_str)
print(tainghe3.__dict__)
tainghe3.bum()