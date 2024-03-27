# tính kế thừa
class dienthoai:
    manhinh = "cong"

class dienthoaixiaomi(dienthoai):
    pass

mi11 = dienthoaixiaomi()
print(mi11.manhinh)
# sửa đổi kế thừa
class dienthoai:
    manhinh = "cong"
    def __init__(self, para_kt, para_mau):
        self.kt = para_kt
        self.mau = para_mau

class dienthoaixiaomi(dienthoai):
    manhinh ="phẳng"
    def __init__(self, para_kt, para_mau, para_cl):
        self.kt = para_kt
        self.mau = para_mau
        self.cl = para_cl

mi11 = dienthoaixiaomi("6.4","xanh", "nhua")
print(mi11.manhinh)
print(mi11.__dict__)
# kế thừa từ cha và kế thừa phương thức
class dienthoai:
    manhinh = "cong"
    def __init__(self, para_kt, para_mau):
        self.kt = para_kt
        self.mau = para_mau
    def review(self):
        print("Đây là điện thoại xịn")

class dienthoaixiaomi(dienthoai):
    manhinh = "phẳng"
    def __init__(self, para_kt, para_mau, para_cl):
        super().__init__(para_kt, para_mau)
        self.cl = para_cl
mi11 = dienthoaixiaomi("6.4", "xanh", "nhựa")
print(mi11.manhinh)
print(mi11.__dict__)
mi11.review()

#getter setter và deleter
class lophoc:
    def __init__(self, ho ,ten):
        self.ho = ho
        self.ten = ten
        self.email = ho + '-' + ten + '@gmail.com'
    @property
    def hoten(self):
        return '{}{}'.format(self.ho,self.ten)
    @hoten.setter
    def hoten(self,tenmoi):
        homoi,tenmoi =tenmoi.split(' ')
        self.ho =homoi
        self.ten =tenmoi
    @hoten.deleter
    def hoten(self):
        self.ho = None
        self.ten = None
    def newemail(self):
        return self.ho + '-' + self.ten + '@gmail.com'
        
hocsinha = lophoc('huy','vũ')
hocsinha.ho = 'hương'
hocsinha.ten = 'giang'

print(hocsinha.ho)
print(hocsinha.ten)
print(hocsinha.email)
print(hocsinha.newemail())
print(hocsinha.hoten)
