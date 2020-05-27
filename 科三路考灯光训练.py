import random

TiMu_List={'1请开启前照灯':1,
           '2夜间直行通过路口':1,
           '3夜间在照明条件良好下行驶':1,
           '4夜间同方向近距离跟车行驶':1,
           '5夜间与机动车会车':1,
           '6夜间在窄路与机动车会车':1,
           '7夜间在有路灯的道路上行驶':1,
           '8夜间在没有路灯，照明条件不良条件下行驶':2,
           '9夜间通过拱桥、人行横道':3,
           '10夜间超越前方车辆':3,
           '11夜间通过急弯坡路':3,
           '12夜间通过没有交通信号灯控制的路口':3,
           '14夜间通过坡路、拱桥':3,
           '15夜间通过急弯、拱桥':3,
           '13路边临时停车':4,
           '16夜间道路上发生交通事故，妨碍交通又难以移动':4,}
DaAn_List={1:'近光灯',2:'远光灯',3:'远近交替',4:'示廓灯和危险警报灯'}

def Random_Timu():
    timu=random.choice(list(TiMu_List))
    return timu

if __name__=='__main__':
    while 1:
        timu=Random_Timu()
        print(timu)
        try:
            shuru=input("①近光灯②远光灯③远近交替④示廓灯和危险警报灯\n请输入答案序号：")
            if int(shuru) == int(TiMu_List[timu]):
                print("答案正确！下一题，回车键结束。\n")
            else:
                print("回答错误！\n\n答~~~错~~啦~...分割线，You are wrong!!Look me.")
                DaAn=TiMu_List[timu]
                print("正确答案为：{}{}\n\n".format(TiMu_List[timu],DaAn_List[DaAn]))
        except:
            break
