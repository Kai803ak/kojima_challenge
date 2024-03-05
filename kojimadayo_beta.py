import random
import os
import datetime

global show_list
def show_list():
    print("")
    print("現在のリストを表示します")    
    list_num = 0
    for list_name in name:
        print(str(list_num) + ")" + str(list_name))
        list_num += 1
    print("")


def shuffle_run():
    global success
    global failed
    call_num = random.randint(0,len(name)-1)
    answ_num = random.randint(0,len(name)-1)
    print("")
    call = ("A:" + str(name[call_num]) + "さーん")
    print(call)
    if call_num == answ_num:
        answ = ("B:はーい")
        success += 1
    else:
        answ = "B:いや" + str(name[answ_num]) + "だよ(怒)"
        failed += 1
    print(answ)
    return call,answ,success,failed


def name_edit():
    global EDIT_loop
    EDIT_loop = True
    while EDIT_loop == True:
        show_list()
        print("1:編集する！")
        print("2:追加する！")
        print("3:消去する！")
        print("4:初期状態にリセットする！")
        print("5:もうあきた帰る")
        EDIT_chosen = input("行いたい操作を入力してください:")
        print("")
        if EDIT_chosen == "1":
            EDIT_num = int(input("何番目の人を編集しますか？:"))
            name[EDIT_num] = input("新しい名前を命名してください:")
            print("編集が完了しました")
        elif EDIT_chosen == "2":
            name.append(input("追加したい名前を命名してください:"))
            print("追加が完了しました")
        elif EDIT_chosen == "3":
            rm_num = int(input("抹消したい名前の番号を入力してください:"))
            name.pop(rm_num)
        elif EDIT_chosen == "4":
            first_run()
        elif EDIT_chosen == "5":
            EDIT_loop = False
            write_data()
            print("編集を終了します")
        else:
            print("1~5で入力してください")

global write_data
def write_data():
    global name
    global name_file
    tmp_file = open('tmp', 'w')
    for data in name:
        tmp_file.write(str(data)+ "\n")
    tmp_file.close()
    if opennamefile == True:
        name_file.close()
        os.remove("name_list.txt")
    os.rename("tmp","name_list.txt")
    name_file = open('name_list.txt', 'r')
    name = name_file.read().splitlines()
    return name

global first_run
def first_run():
    global name
    name = ['矢島','田島','小島','大島','輪島','川島','三島']
    write_data()
    print("(初期名前の書き込みが完了しました)")
    
#main
global opennamefile
if os.path.isfile("name_list.txt") == True:
    opennamefile = True
    name_file = open('name_list.txt', 'r')
    name = name_file.read().splitlines()
    if len(name) == 0:
        first_run()
else:
    opennamefile = False
    first_run()

global loop
loop = True
list_show = True
global success
global failed
success = 0
failed = 0
while loop == True:
    if list_show == True:
        show_list()
    print("")
    print("1:チャレンジする！")
    print("2:100回連続チャレンジをしてファイルに書き込む！")
    print("3:名前をいじる！")
    print("4:もうあきた帰る")
    print("")
    chosen = input("行いたい操作を選んでください:")
    if chosen == "1":
        list_show = False
        shuffle_run()
    elif chosen == "2":
        list_show = False
        LOOP_filename = ("kojima_") + str(datetime.datetime.now().strftime('%Y%m%d%H%M')) + (".txt")
        LOOP_file = open(LOOP_filename,'w')
        LOOP_times = 0
        success = 0
        failed = 0
        NONSTOP = True
        while NONSTOP == True:
            result = shuffle_run()
            LOOP_times +=1
            LOOP_file.write(str(result[0]) + '\n')
            LOOP_file.write(str(result[1]) + '\n')
            LOOP_file.write('\n')
            if LOOP_times == 100:
                LOOP_file.write("成功回数:" + str(success) + "回" + '\n')
                LOOP_file.write("失敗回数:" + str(failed) + "回")
                NONSTOP = False
        LOOP_file.close()
    elif chosen == "3":
        list_show = False
        name_edit()
    elif chosen == "4":
        exit()
    else:
        print("1~4で入力してください")
        chosen = "0"
