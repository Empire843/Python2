class Score:
    def __init__(self, ho_ten, diem_cc, diem_btl, diem_thi_ck):
        self.ho_ten = ho_ten
        self.diem_cc = diem_cc
        self.diem_btl = diem_btl
        self.diem_thi_ck = diem_thi_ck

    def __getitem__(self, key):
        return getattr(self, key)

    def Diem_TK(self):
        return "{:.1f}".format(0.1 * self.diem_cc + 0.3 * self.diem_btl + 0.6 * self.diem_thi_ck)

name = input()
diem_cc = float(input())
diem_btl = float(input())
diem_thi_ck = float(input())
s = Score(name, diem_cc, diem_btl, diem_thi_ck)
print(s['ho_ten'], s.Diem_TK())
