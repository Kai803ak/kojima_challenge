import random
import os
import datetime

#リスト表示
global show_list
def show_list():
    print("")
    print("現在のリストを表示します")    
    for list_num in range(len(name)):
        print(str(list_num) + ")" + str(name[list_num]))
    print("")


#シャッフル実行
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


#名前編集
def name_edit():
    while True:
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
            write_data()
            print("編集を終了します")
            break
        else:
            print("1~5で入力してください")

#データ書き込み
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

#内容orファイルなしのときの初期設定
global first_run
def first_run():
    global name
    name = ['矢島','田島','小島','大島','輪島','川島','三島']
    write_data()
    print("(初期名前の書き込みが完了しました)")

#ループシャッフル実行
global LOOP
def shuffle_LOOP():
    while True:
        print("")
        print("ファイルに書き込みますか？")
        print("1:はい  2:いいえ")
        file_write = int(input("行いたい操作を選んでください:"))
        if file_write == 1:
            break
        elif file_write == 2:
            break
        else:
            print("1または2で入力してください。")
    if file_write == 1:
        LOOP_filename = ("kojima_") + str(datetime.datetime.now().strftime('%Y%m%d%H%M')) + (".txt")
        LOOP_file = open(LOOP_filename,'w')
    LOOP_times = 0
    LOOP_settime = int(input("何回実行するか入力してください:"))
    while True:
        result = shuffle_run()
        LOOP_times +=1
        if file_write == 1:
            LOOP_file.write(str(result[0]) + '\n' + str(result[1]) + '\n' + '\n')
        if LOOP_times == LOOP_settime:
            if file_write == 1:
                LOOP_file.write("成功回数:" + str(result[2]) + "回" + '\n' + "失敗回数:" + str(result[3]) + "回")
                LOOP_file.close()
            print("成功回数:" + str(result[2]) + "回")
            print("失敗回数:" + str(result[3]) + "回")
            break
        
#main
#ファイルの存在確認
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

#定義
list_show = True
success = 0
failed = 0

#メニュー
while True:
    if list_show == True:
        show_list()
    print("")
    print("1:チャレンジする！")
    print("2:連続チャレンジをする！")
    print("3:名前をいじる！")
    print("4:もうあきた帰る")
    print("")
    chosen = input("行いたい操作を選んでください:")
    if chosen == "1":
        list_show = False
        shuffle_run()
    elif chosen == "2":
        list_show = False
        success = 0
        failed = 0
        shuffle_LOOP()
    elif chosen == "3":
        list_show = False
        name_edit()
    elif chosen == "4":
        exit()
    else:
        print("1~4で入力してください")
