import tkinter as tk
import tkinter.filedialog
import tkinter.font as tf
from wxpy import *
import os
import time

gname = ''
Saveadd=''


window = tk.Tk()
window.title('微信收作业')
window.geometry('430x850')
window.configure(bg='#7F7F7F')
window.resizable(0, 0)


def load2():
    global Saveadd
    Saveadd = tk.filedialog.askdirectory()
    if Saveadd == '':
        text.insert("end", '******请选择文件路径\r\n', 'tagy')
    else:
        text.insert("end", f'---已选择默认路径，路径"{Saveadd}"\r\n', 'tagw')

def usemoren():
    global gname
    gname = '数学交作业群'
    text.insert("end", f'---已使用默认群聊，名称"{gname}，请确认群聊名称"\r\n', 'tagw')


def useinput():
    global gname
    gname=r1.get()
    if gname=='':
        text.insert("end", '******请输入群聊名称\r\n', 'tagy')
    else:
        text.insert("end", f'---已使输入的名称，名称"{gname}"\r\n', 'tagw')

def run():
    if gname =='':
        text.insert("end", '******请输入群聊名称\r\n', 'tagy')
    elif Saveadd == '':
        text.insert("end", '******请选择文件路径\r\n', 'tagy')
    else:
        global bot
        bot = Bot(cache_path=True)
        text.insert("end", '微信登陆成功,等待同学交作业\r\n', 'tagg')
        try:
            g1 = bot.groups().search(str(gname))[0]
        except Exception:
            text.insert("end", '******请输入正确群聊名称\r\n', 'tagy')
            bot.logout()
            text.insert("end", '----微信已退出登陆，请重新输入信息\r\n', 'tagg')

        global t
        global name
        global addT
        t = time.strftime('%Y-%m-%d')
        name = []
        addT = []

        @bot.register(g1,except_self=False)
        def savefiles(msg):
            Sname = msg.raw.get('ActualNickName')
            add = os.path.join(Saveadd, t, Sname)
            if add not in addT:
                if os.path.exists(add):
                    addT.append(add)
                else:
                    os.makedirs(add)
                    addT.append(add)
            path = os.path.join(add, str(time.time())+str(msg.file_name))
            msg.get_file(path)
            text.insert("end", f'{Sname}交了作业，已保存到本地\r\n', 'tagw')
            if Sname not in name:
                name.append(Sname)
                with open(os.path.join(Saveadd, t,'已交名单.txt'), 'a', encoding='utf-8') as f:
                    f.write(f'\n{Sname}')
            # text.insert("end", f'已交作业名单：{name}\r\n', 'tagw')
        bot.join()

def close():
    text.insert("end", '交作业人员名单清查看保存目录下"已交名单.txt"\r\n', 'tagg')
    bot.logout()
    text.insert("end", '----微信已退出登陆\r\n', 'tagg')

# 输入变量entry
r1 = tk.StringVar()

l0 = tk.Label(window, text='Designed by MaguaG (-_0) E-mail:MaguaG9494@gmail.com', bg='black', font=('等线', 12),
              fg='white', width='200').pack()
l1 = tk.Label(window, text='-----------------------------------------------------', bg='#7F7F7F', font=('等线', 10), fg='white',
              width=400).pack()
l2 = tk.Label(window, text='设置微信群名称', bg='#7F7F7F', font=('等线', 20), fg='white', width=400).pack()
i2 = tk.Label(window, text='', bg='#7F7F7F', font=('等线', 10), fg='white',width=400).pack()
f0 = tk.Frame(window,bg='#7F7F7F')
f0l1 = tk.Label(f0, text='输入群聊名称：', font=('等线', 12), width=15, bg='#7F7F7F', fg='white').grid(row=1, column=1)
f0e1 = tk.Entry(f0, textvariable=r1, width=20).grid(row=1, column=2)
f0.pack()

i6 = tk.Label(window, text='', bg='#7F7F7F', font=('等线', 10), fg='white',width=400).pack()
fram4 = tk.Frame(window,bg='#7F7F7F')
submit2 = tk.Button(fram4, text='使用默认', bg='#3A414B', fg='white', font=('等线', 10), width=15, height=2,
                    command=usemoren).grid(row=1, column=3)
f6 = tk.Label(fram4, text='', font=('Arial', 30), width=2, bg='#7F7F7F').grid(row=1, column=2)
submit2 = tk.Button(fram4, text='使用输入', bg='#3A414B', fg='white', font=('等线', 10), width=15, height=2,
                    command=useinput).grid(row=1, column=1)
fram4.pack()


l4 = tk.Label(window, text='-----------------------------------------------------', bg='#7F7F7F', font=('等线', 10), fg='white',
              width=400).pack()
l5 = tk.Label(window, text='选择文件路径', bg='#7F7F7F', font=('等线', 20), fg='white', width=400).pack()
i3 = tk.Label(window, text='', bg='#7F7F7F', font=('等线', 10), fg='white',width=400).pack()
f1 = tk.Frame(window,bg='#7F7F7F')
f1l1 = tk.Label(f1, text='文件保存路径：', font=('等线', 12), width=15, bg='#7F7F7F', fg='white').grid(row=1, column=1)
f1b1 = tk.Button(f1, text='选择文件夹', bg='#3A414B', font=('等线', 11), fg='white', width=10, command=load2).grid(row=1,column=2)
f1.pack()
l8 = tk.Label(window, text='-----------------------------------------------------', bg='#7F7F7F', font=('等线', 10), fg='white',
              width=400).pack()

i4 = tk.Label(window, text='', bg='#7F7F7F', font=('等线', 10), fg='white',width=400).pack()


f222 = tk.Frame(window,bg='#7F7F7F')
sub = tk.Button(f222, text='开始运行', bg='#3A414B', fg='white', font=('等线', 12), width=15, height=2,
                    command=run).grid(row=1, column=1)
f62 = tk.Label(f222, text='', font=('Arial', 30), width=2, bg='#7F7F7F').grid(row=1, column=2)
sub2 = tk.Button(f222, text='结束运行', bg='#3A414B', fg='white', font=('等线', 12), width=15, height=2,
                    command=close).grid(row=1, column=3)
f222.pack()
i5 = tk.Label(window, text='', bg='#7F7F7F', font=('等线', 10), fg='white',width=400).pack()

text = tk.Text(window, width=300, height=32, borderwidth=0, bg='black')
text.pack()

# 设置text字体
ft = tf.Font(family='微软雅黑', size=10)
text.tag_add('tagg', 'end')
text.tag_config('tagg', foreground='green', font=ft)
text.tag_add('tagr', 'end')
text.tag_config('tagr', foreground='red', font=ft)
text.tag_add('tagy', 'end')
text.tag_config('tagy', foreground='#FFFF00', font=ft)
text.tag_add('tagw', 'end')
text.tag_config('tagw', foreground='white', font=ft)
window.mainloop()