# 多继承Multiple Inheritance

class ShenXian:
    """神仙类"""

    def fly(self):
        print("神仙都会飞...")

    def fight(self):
        print("神仙在打架")


class Monkey:
    def eat_peach(self):
        print("猴子都喜欢吃桃子...")

    def fight(self):
        print("猴子在打架...")


class MonkeyKing(ShenXian, Monkey):  # 多继承

    def play_goden_stick(self):
        print("孙悟空玩金箍棒...")


sxz = MonkeyKing()
sxz.eat_peach()
sxz.fly()
sxz.play_goden_stick()
sxz.fight()  # 按顺序从左到右继承，深度优先，先找当前继承得父类，如没找到再找父类得父类
