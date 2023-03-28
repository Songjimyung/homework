import random
from operator import eq
import time

# 플레이어


class Player():
    def __init__(self, name, hp, mp, power, mpower, job):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power
        self.mpower = mpower
        self.job = job
        self.alive = True
    # 상태창

    def Player_info(self):
        print(f"\n유저명 : {self.name} \n"
              f"직업 : {self.job} \n"
              f"HP : [{self.hp}/{self.max_hp}] \n"
              f"MP : [{self.mp}/{self.max_mp}]"
              f"물리공격력 : {self.power} \n"
              f"마법공격력 : {self.mpower} \n")
    # 공격 종류

    def attack_method(self, other, select):
        if select == 2:
            if self.mp >= 10:
                mdamage = random.randint(self.mpower - 5, self.mpower + 5)
                self.mp -= 8
                other.hp = max(other.hp - mdamage, 0)
                print(f"{self.name}의 마법 공격! {other.m_name}에게 {mdamage}의 피해를 입혔습니다.")
                if other.hp == 0:
                    print(f"{other.m_name}을(를) 쓰러트렸습니다!")
            else:
                print('마나가 부족합니다..')
            return choose_attack()
        elif select == 1:
            damage = random.randint(self.power - 2, self.power + 2)
            self.mp += 2
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 일반 공격! {other.m_name}에게 {damage}의 피해를 입혔습니다.")
            if other.hp == 0:
                print(f"{other.m_name}을(를) 쓰러트렸습니다!")

    def alive_check(self):
        if self.hp <= 0:
            self.alive = False

    # 공격 후 내 상태

    def show_status(self):
        print(
            f"{self.name}의 상태: HP : [{self.hp}/{self.max_hp}] MP : [{self.mp}/{self.max_mp}]")

# 전사의 클래스


class Warrior(Player):
    def __init__(self, name, hp, mp, power, mpower, job):
        self.attribute = "전사"
        super().__init__(name, hp, mp, power, mpower, job)

    # 전사 공격 overriding
    def attack_method(self, other, select):
        if self.alive == True and other.alive == True:

            if select == 2:
             if self.mp >= 10:
                mdamage = random.randint(self.mpower - 5, self.mpower + 5)
                self.mp -= 8
                other.hp = max(other.hp - mdamage, 0)
                print(
                    f"{self.name}의 마법 공격! 전사로 마법 공격을 왜 하셨죠...? {other.m_name}에게 {mdamage}의 피해밖에 입히지 못했습니다.")
                if other.hp == 0:
                    print(f"{other.m_name}을(를) 쓰러트렸습니다!")
             else:
                print('마나가 부족합니다..')
                return choose_attack()
            elif select == 1:
                damage = random.randint(self.power - 2, self.power + 2)
                other.hp = max(other.hp - damage, 0)
                print(f"{self.name}의 일반 공격! {other.m_name}에게 {damage}의 피해를 입혔습니다.")
                if other.hp == 0:
                    print(f"{other.m_name}을(를) 쓰러트렸습니다!")
            elif select == 3:
             if self.mp>= 5:
                 sdamage = random.randint(self.power + 5, self.power + 10)
                 self.mp -= 5
                 other.hp = max(other.hp - sdamage, 0)
                 print(f"{self.name}의 스매쉬! {other.m_name}에게 {sdamage}의 강한 피해를 입혔습니다.")
                 if other.hp == 0:
                    print(f"{other.m_name}을(를) 쓰러트렸습니다!")
             else:
                 print('마나가 부족합니다..')
                 return choose_attack()
        elif self.alive == True and other.alive == False:
            print('이미 죽은 상대입니다..')
            return choose_monster()
        else : print('죽은 상태에서는 할 수 없습니다')     

 # 마법사의 클래스


class Magician(Player):
    def __init__(self, name, hp, mp, power, mpower, job):
        self.attribute = "마법사"
        super().__init__(name, hp, mp, power, mpower, job)
    # 마법사 공격 overriding

    def attack_method(self, other, select):
        if self.alive == True and other.alive == True:
            
            if select == 2:
              if self.mp >= 10:
                 mdamage = random.randint(self.mpower - 2, self.mpower + 2)
                 self.mp -= 8
                 other.hp = max(other.hp - mdamage, 0)
                 print(f"{self.name}의 마법 공격! {other.m_name}에게 {mdamage}의 피해를 입혔습니다.")
                 if other.hp == 0:
                    print(f"{other.m_name}을(를) 쓰러트렸습니다!")
              else : 
                  print('마나가 부족합니다..')
                  return choose_attack()
            elif select == 1:
                damage = random.randint(self.power - 2, self.power + 2)
                self.mp += 5
                other.hp = max(other.hp - damage, 0)
                print(f"{self.name}의 일반 공격! {other.m_name}에게 {damage}의 피해를 입혔습니다.")
                if other.hp == 0:
                    print(f"{other.m_name}을(를) 쓰러트렸습니다!")
            elif select == 3:
              if self.mp >= 20:
                 sdamage = random.randint(self.mpower + 5, self.mpower + 10)
                 self.mp -= 20
                 other.hp = max(other.hp - sdamage, 0)
                 print(f"{self.name}의 화염구! {other.m_name}에게 {sdamage}의 화상피해를 입혔습니다.")
                 if other.hp == 0:
                    print(f"{other.m_name}을(를) 쓰러트렸습니다!")
              else : 
                  print('마나가 부족합니다..')
                  return choose_attack()
        elif self.alive == True and other.alive == False:
            print('이미 죽은 상대입니다..')
            return choose_monster()
        else : print('죽은 상태에서는 할 수 없습니다') 


class Priest(Player):
    def __init__(self, name, hp, mp, power, mpower, job):
        self.attribute = "성녀"
        super().__init__(name, hp, mp, power, mpower, job)

    def attack_method(self, other, users, select):
        if self.alive == True:
        
            if select == 2 and other.alive == True:
               mdamage = random.randint(self.mpower - 2, self.mpower + 2)
               self.mp -= 5
               other.hp = max(other.hp - mdamage, 0)
               print(f"{self.name}의 마법 공격! {other.m_name}에게 {mdamage}의 피해를 입혔습니다.")
               if other.hp == 0:
                  print(f"{other.m_name}을(를) 쓰러트렸습니다!")
            elif select == 1 and other.alive == True:
                 damage = random.randint(self.power - 2, self.power + 2)
                 other.hp = max(other.hp - damage, 0)
                 self.mp += 5
                 print(f"{self.name}의 일반 공격! {other.m_name}에게 {damage}의 피해를 입혔습니다.")
                 if other.hp == 0:
                    print(f"{other.m_name}을(를) 쓰러트렸습니다!")
            elif select == 3:
                if users.alive == True:
                   sdamage = random.randint(self.mpower + 5, self.mpower + 10)
                   self.mp -= 10                              
                   
                   if users.hp >= users.max_hp :
                       users.hp = users.max_hp
                       print(f"{self.name}의 힐! {users.name}은 이미 최대 체력입니다..")
                   else :
                       users.hp = min(users.hp + sdamage, users.max_hp)
                       print(f"{self.name}의 힐! {users.name}에게 {sdamage}의 회복을 하였습니다.")
                
                else:
                    print(f"{users.name}은 이미 죽어 있습니다...")
                    return team_choose()
        elif self.alive == True and other.alive == False:
            print('이미 죽은 상대입니다..')
            return choose_monster()
        
        elif self.alive == False:
            print('죽은 상태에서는 할 수 없습니다') 


# 몬스터
class Monster():
    def __init__(self, name, hp, mp, power, mpower):
        self.name = name
        if self.name == 1:
            self.m_name = "트롤"
        elif self.name == 2:
            self.m_name = "오거"
        elif self.name == 3:
            self.m_name = "고블린"
        elif self.name == 4:
            self.m_name = "오크"
        self.max_hp = hp
        self.hp = hp
        self.mp = mp
        self.power = power
        self.mpower = mpower
        self.alive = True

    def names(self):
        print(f"{self.m_name}이(가) 나타났다!")

    def attack(self, other):
        try:
            if self.alive == True and other.alive == True:
                attack_num = random.randint(1, 3)
                if attack_num == 3 and self.mp >= 5:
                    self.mp -= 5
                    sdamage = random.randint(self.mpower - 5, self.mpower + 5)
                    other.hp = max(other.hp - sdamage, 0)
                    print(
                        f"{self.m_name}의 특수 공격! {other.name}은 {sdamage}의 피해를 받았습니다.")
                    if other.hp == 0:
                        print(f"{other.name}이 쓰러졌습니다...")
                else:
                    damage = random.randint(self.power - 4, self.power + 4)
                    other.hp = max(other.hp - damage, 0)
                    print(f"{self.m_name}의 공격! {other.name}은 {damage}의 피해를 받았습니다.")
                    if other.hp == 0:
                        print(f"{other.name}이 쓰러졌습니다...")
            elif self.alive == False:
                print('')
            elif other.alive == False:
                return monster_attack()
        except:
            print('')

    def alive_check(self):
        if self.hp <= 0:
            self.alive = False

    def show_status(self):
        print(f"{self.m_name}의 상태: HP : [{self.hp}/{self.max_hp}]")


class Monster2(Monster):
    def __init__(self, name, hp, mp, power, mpower):
        self.attribute = "seceond"
        super().__init__(name, hp, mp, power, mpower)

    def attack(self, other):
        try:
            if self.alive == True and other.alive == True:
                attack_num = random.randint(1, 3)
                if attack_num == 3 and self.mp >= 5:
                    self.mp -= 5
                    sdamage = random.randint(self.mpower - 5, self.mpower + 5)
                    other.hp = max(other.hp - sdamage, 0)
                    print(
                        f"{self.m_name}의 특수 공격! {other.name}은 {sdamage}의 피해를 받았습니다.")
                    if other.hp == 0:
                        print(f"{other.name}이 쓰러졌습니다...")
                else:
                    damage = random.randint(self.power - 4, self.power + 4)
                    other.hp = max(other.hp - damage, 0)
                    print(f"{self.m_name}의 공격! {other.name}은 {damage}의 피해를 받았습니다.")
                    if other.hp == 0:
                        print(f"{other.name}이 쓰러졌습니다...")
            elif self.alive == False:
                print('')
            elif other.alive == False:
                return Mon2.attack()
        except:
            print('')

# 유저 아이디 생성


def user_id():
    id = input('닉네임을 입력해주세요 : ')
    return id

# 직업선택


def jobclass():
    character_class = input('원하는 직업을 선택해주세요 : 1. 전사 2. 마법사')
    if character_class == '':
        print("정확한 값을 입력해주세요")
        return jobclass()
    elif not character_class.isdigit():
        print("숫자로 입력해주세요")
        return jobclass()
    elif int(character_class) >= 3 or int(character_class) < 1:
        print("1에서 2 사이로 입력해 주세요")
        return jobclass()
    elif character_class == '1':
        myclass = '전사'
    elif character_class == '2':
        myclass = '마법사'
    # else:
    #     myclass = '성직자'                #전부 다르게 설정이 너무 어렵....일단 생략
    return myclass

# 직업에 따른 스탯분배


def Health():
    if eq(myjob, '전사'):
        H = 200
    elif eq(myjob, '마법사'):
        H = 120
    # else:
    #     H = 80
    return H


def Mana():
    if eq(myjob, '전사'):
        M = 20
    elif eq(myjob, '마법사'):
        M = 80
    # else:
    #     M = 60
    return M


def P_power():
    if eq(myjob, '전사'):
        P = 30
    elif eq(myjob, '마법사'):
        P = 10
    # else:
    #     P = 5
    return P


def M_power():
    if eq(myjob, '전사'):
        MG = 5
    elif eq(myjob, '마법사'):
        MG = 30
    # else:
    #     MG = 20
    return MG


# 몬스터 스탯값
def R_monster(name='', hp='', mp='', power='', mpower=''):
    name = random.randint(1, 4)
    hp = random.randint(150, 200)
    mp = random.randint(20, 40)
    power = random.randint(10, 30)
    mpower = random.randint(10, 30)
    return name, hp, mp, power, mpower


s = R_monster()
a = R_monster()

# 유저 아이디 생성
nickname = user_id()
# 유저 직업 생성
myjob = jobclass()
# 유저 스탯값
health_bar = Health()
mana_bar = Mana()
pysical = P_power()
magical = M_power()



#유저 생성
if eq(myjob, '전사'):
    users1 = Warrior(nickname, health_bar, mana_bar, pysical, magical, myjob)
elif eq(myjob, '마법사'):
    users1 = Magician(nickname, health_bar, mana_bar, pysical, magical, myjob)
# else:
#     users1 = Priest(nickname, health_bar, mana_bar, pysical, magical, myjob)
# 유저 생성 정보
users1.Player_info()

nickname2 = user_id()
myjob = jobclass()
health_bar2 = Health()
mana_bar2 = Mana()
pysical2 = P_power()
magical2 = M_power()

if eq(myjob, '전사'):
    users2 = Warrior(nickname2, health_bar2, mana_bar2, pysical2, magical2, myjob)
elif eq(myjob, '마법사'):
    users2 = Magician(nickname2, health_bar2, mana_bar2, pysical2, magical2, myjob)
# else:
#     users2 = Priest(nickname2, health_bar2, mana_bar2, pysical2, magical2, myjob)

users2.Player_info()
time.sleep(3)
print('\033[95m'+'성녀님이 합류했어요!\n'+'\033[0m')
users3 = Priest('성녀', 80, 60, 5, 20, 3)
users3.Player_info()



# class Create():
#     def __init__(self, Nickname, Health, Mana, Pysics, Magic,jobs,users):
#         self.Nickname = Nickname
#         self.Health = Health
#         self.Mana = Mana
#         self.Pysics = Pysics
#         self.Magic = Magic
#         self.jobs = jobs
#         self.users = users
#         if eq(jobs, '전사'):
#             users = Warrior(Nickname, Health, Mana, Pysics, Magic, jobs)
#         elif eq(jobs, '마법사'):
#             users = Magician(Nickname, Health, Mana, Pysics, Magic, jobs)
#         else:
#             users = Priest(Nickname, Health, Mana, Pysics, Magic, jobs)
# use1 = Create(user_id(),Health(),Mana(),P_power(),M_power(),jobclass(),)    

# use2 = Create(user_id(),Health(),Mana(),P_power(),M_power(),jobclass())    
 # 

# 로그가 천천히 뜨게
# time.sleep(3)
# # 동료
# print('\033[95m'+'동료들이 합류했어요!\n'+'\033[0m')
# # 동료 생성 및 동료 정보
# users2 = Magician('마법사', 120, 80, 10, 30, '마법사')
# users2.Player_info()
# time.sleep(2)
# users3 = Priest('성직자', 80, 60, 5, 20, '성직자')
# users3.Player_info()

# 몬스터 임의 생성
Mon = Monster(s[0], s[1], s[2], s[3], s[4])
Mon2 = Monster2(a[0], a[1], a[2], a[3], a[4])
time.sleep(2)
Mon.names()
time.sleep(1)
Mon2.names()
# 몬스터 등장


combat_num = 0  # 전투횟수
# 선택지 제공


def check_answer():
    while True:
        check = input("1.예 2.아니오 \n")
        if check == '':
            print("정확한 값을 입력해주세요. \n")
        elif not check.isdigit():
            print('숫자로 입력해주세요.')
        elif int(check) < 1 or int(check) > 2:
            print("1 또는 2 중에서 입력해주세요.\n")
        else:
            return int(check)
# 공격 선택지


def choose_attack():
    while True:
        choose = input("공격을 선택해주세요\n"
                       "1.물리 공격 \n"
                       "2.마법 공격 \n"
                       "3.특수 공격 \n")
        if choose == '':
            print("정확한 값을 입력해주세요")
        
              
        elif not choose.isdigit():
            print("숫자로 입력해주세요")
            
        elif int(choose) < 1 or int(choose) > 3:
            print("1에서 3사이로 입력해주세요")
            
        else:
            return int(choose)


# def choose_attack2():
#     while True:
#         choose2 = input(f"{nickname2}의 턴\n"
#                         "1.물리 공격 \n"
#                         "2.마법 공격 \n"
#                         "3.특수 공격 \n")
#         if int(choose2) < 1 or int(choose2) > 4:
#             print("1에서 3사이로 입력해주세요")
#         elif choose2 == '':
#             print("정확한 값을 입력해주세요")
#         elif not choose2.isdigit():
#             print("숫자로 입력해주세요")
#         else:
#             return int(choose2)


def choose_attack3():
    while True:
        choose3 = input("성녀의 공격\n"
                        "1.물리 공격 \n"
                        "2.마법 공격 \n"
                        "3.특수 공격 \n")
        if choose3 == '':
            print("정확한 값을 입력해주세요")
       
        
        elif not choose3.isdigit():
            print("숫자로 입력해주세요")
        elif int(choose3) < 1 or int(choose3) > 3:
            print("1에서 3사이로 입력해주세요")     
        else:
            return int(choose3)


def choose_monster():
    while True:
        choose_m = input("1.1번 몬스터 공격\n"
                         "2.2번 몬스터 공격\n")
        if choose_m == '':
            print("정확한 값을 입력해주세요")
        
        
        elif not choose_m.isdigit():
            print("숫자로 입력해주세요")
            
        if int(choose_m) < 1 or int(choose_m) > 2:
            print("1 또는 2 중에서 입력해주세요")
                
        else:
            return int(choose_m)

# def choose_monster2():
#     while True:
#         choose_m2 =input("1.1번 몬스터 공격\n"
#                         "2.2번 몬스터 공격\n")
#         if int(choose_m2) > 2 or int(choose_m2) < 1:
#             print("1 또는 2 중에서 입력해주세요")
#         elif choose_m2 == '':
#             print("정확한 값을 입력해주세요")
#         elif not choose_m2.isdigit():
#             print("숫자로 입력해주세요")
#         else :
#             return int(choose_m2)

# def choose_monster3():
#     while True:
#         choose_m3 =input("1.1번 몬스터 공격\n"
#                         "2.2번 몬스터 공격\n")
#         if int(choose_m3) > 2 or int(choose_m3) < 1:
#             print("1 또는 2 중에서 입력해주세요")
#         elif choose_m3 == '':
#             print("정확한 값을 입력해주세요")
#         elif not choose_m3.isdigit():
#             print("숫자로 입력해주세요")
#         else :
#             return int(choose_m3)


def team_choose():
    while True:
        choose_t = input("1.1번 팀원 힐\n"
                         "2.2번 팀원 힐\n"
                         "3.3번 팀원 힐\n")
        if int(choose_t) > 3 or int(choose_t) < 1:
            print("1에서 3사이로 입력해주세요")
        elif choose_t == '':
            print("정확한 값을 입력해주세요")
        elif not choose_t.isdigit():
            print("숫자로 입력해주세요")
        else:
            return int(choose_t)


def monster_attack():
    monster_choose = random.randint(1, 3)
    return int(monster_choose)


while True:
    if combat_num == 0:
        print("몬스터와 전투하시겠습니까?")
        Answer = check_answer()
    if Answer == 1:
        # 1번 유저 공격      # 유저가 성직자를 선택한 경우 실행 불가//수정할것
        user_attack = choose_attack()
        select_monster = choose_monster()
        if select_monster == 1:
            user_damage = users1.attack_method(Mon, user_attack)
        else:

            user_damage = users1.attack_method(Mon2, user_attack)

        Mon.alive_check()
        Mon2.alive_check()
        user2_attack = choose_attack()  # 2번 유저 공격
        select_monster2 = choose_monster()
        if select_monster2 == 1:

            user2_damage = users2.attack_method(Mon, user2_attack)
        elif select_monster2 == 2:

            user2_damage = users2.attack_method(Mon2, user2_attack)

        Mon.alive_check()
        Mon2.alive_check()
        user3_attack = choose_attack3()  # 3번 유저 공격
        if user3_attack < 3:
            select_monster3 = choose_monster()
            if select_monster3 == 1:

                user3_damage = users3.attack_method(Mon, '', user3_attack)
            elif select_monster3 == 2:

                user3_damage = users3.attack_method(Mon2, '', user3_attack)
        elif user3_attack == 3:  # 3번 성직자 힐스킬
            team_heal = team_choose()
            if team_heal == 1:
                user3_damage = users3.attack_method('', users1, user3_attack)
            elif team_heal == 2:
                user3_damage = users3.attack_method('', users2, user3_attack)
            else :
                user3_damage = users3.attack_method('', users3, user3_attack)
        Mon.alive_check()
        Mon2.alive_check()  # 플레이어 공격 후 몬스터 생존 확인부터.
        m_attack = monster_attack()
        if m_attack == 1:
            monster_damage = Mon.attack(users1)
        elif m_attack == 2:

            monster_damage2 = Mon.attack(users2)
        else:

            monster_damage3 = Mon.attack(users3)
        m2_attack = monster_attack()
        if m2_attack == 1:
            monster2_damage = Mon2.attack(users1)
        elif m2_attack == 2:
            monster2_damage2 = Mon2.attack(users2)
        else:
            monster2_damage3 = Mon2.attack(users3)
        users1.alive_check()
        users2.alive_check()
        users3.alive_check()  # 플레이어 생존확인
        users1.show_status()
        users2.show_status()
        users3.show_status()
        Mon.show_status()
        Mon2.show_status()
        combat_num += 1
    else:
        print('도망쳤습니다...')
        break
    if not users1.alive and users2.alive and users3.alive:
        print('모두 사망하였습니다... 당신은 패배하였습니다.')
        break
    if Mon.alive or Mon2.alive:
        print("아직 쓰러트리지 못했습니다, 다시 공격합니다!")
        continue
    elif not Mon.alive and Mon2.alive:
        print("몬스터를 전부 쓰러트리셨습니다!\n"
              "계속 진행할까요?")
        replay = check_answer()
        if replay == 1:
            combat_num = 0
            s = R_monster()
            a = R_monster()
            Mon = Monster(s[0], s[1], s[2], s[3], s[4])
            Mon2 = Monster2(a[0], a[1], a[2], a[3], a[4])
            time.sleep(2)
            Mon.names()
            time.sleep(1)
            Mon2.names()
        else:
            print('집으로 돌아갑시다')
            break


#문제점 힐이 