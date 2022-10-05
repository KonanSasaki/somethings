import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.io.img_tiles as cimgt
import time
import pigpio
from micropyGPS import MicropyGPS

#参考サイト　https://yyousuke.github.io/matplotlib/cartopy.html

    




def main():

    # シリアル通信設定
    baudrate = 9600
    #通信設定でいじるとしたらここのTX,RXだけど、ピン配置変えたい場合以外はいじらなくてok
    TX = 14
    RX = 15

    serialpi = pigpio.pi()
    serialpi.set_mode(RX,pigpio.INPUT)
    serialpi.set_mode(TX,pigpio.OUTPUT)

    pigpio.exceptions = False
    serialpi.bb_serial_read_close(RX)
    pigpio.exceptions = True

    serialpi.bb_serial_read_open(RX,baudrate,8)
    # gps設定
    #my_gpsにデータが格納される感じ
    my_gps = MicropyGPS(9, 'dd') # 引数はタイムゾーンの時差と出力フォーマット

    # 10秒ごとに表示
    #なんか10秒ごとに表示されてない気がするのでいじってみてほしい
    tm_last = 0
    count = 0
    # Create stamen terrain background instance
    request = cimgt.GoogleTiles()
    fig = plt.figure()
    while True:
        (count, sentence) = serialpi.bb_serial_read(RX)#ここはよくわからん、データが取れてるかどうか調べるところな気がする
        if len(sentence) > 0:
            for x in sentence:
                if 10 <= x <= 126:
                    stat = my_gps.update(chr(x))
                    if stat:
                        tm = my_gps.timestamp
                        tm_now = (tm[0] * 3600) + (tm[1] * 60) + int(tm[2])


                        # Create a GeoAxes in hte tile's projection
                        m1 = fig.add_subplot(111, projection=request.crs) #画面の領域が描写される　111の意味は、1行目1列の1番目という意味　参考サイト　https://qiita.com/kenichiro_nishioka/items/8e307e164a4e0a279734

                        # Set map extent to +- 0.01º of the received position
                        m1.set_extent([my_gps.longitude[0] + 0.01, my_gps.longitude[0] - 0.01, my_gps.latitude[0] + 0.01, my_gps.latitude[0] - 0.01]) #set_extent([西端の経度, 東端の経度, 南端の緯度, 北端の緯度 

                        # Get image at desired zoom
                        m1.add_image(request, 14) ##画像を指定するセルにはる　ここだとグーグルマップのタイルを貼っている
                        # Print data on console
                        print('=' * 20)
                        print(my_gps.date_string(), tm[0], tm[1], int(tm[2]))
                        print("latitude:", my_gps.latitude[0], ", longitude:", my_gps.longitude[0])    
                        time.sleep(1)#一秒停止
    
    # Plot the new position
                        m1.plot(my_gps.longitude[0], my_gps.latitude[0], '.', transform=ccrs.Geodetic())
                        plt.pause(0.1)

if __name__ == "__main__":
    main()