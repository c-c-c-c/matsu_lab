#-*- coding:utf-8 -*-

# BMP ファイルの読み込み
def load_bmp(filename):
    file = open(filename,"rb")
    data = file.read()
    file.close() 
    header = data[0:54]
    file_size, header_size, width, height, bit = load_header_data(header)
    img = data[54:]
    return header, img, width, height, bit
    
    
# BMP ファイルのヘッダ部から画像情報を取得    
def load_header_data(header):
    #  ヘッダ部の情報を切り分け
    file_size = header[2:6] #  ファイルサイズを取得
    header_size = header[10:14] #  ヘッダサイズを取得
    width, height = header[18:22], header[22:26] #  画像の高さと幅を取得
    color_bit = header[28:30] # 1 画素の色数を取得   
  
    #  リトルエンディアン方式で 16 進数から 10 進数に変換
    file_size = int.from_bytes(file_size, 'little')
    header_size = int.from_bytes(header_size, 'little')
    width = int.from_bytes(width, 'little')
    height = int.from_bytes(height, 'little')  
    bit = int.from_bytes(color_bit, 'little') 
    return file_size, header_size, width, height, bit
    
    
# BMP ファイルの書き込み      
def save_bmp(filename, data):
    file = open(filename,"wb")
    file.write(data)
    file.close()
    
    
def main():
    # BMP ファイルの読み込み
    header, img, width, height, bit = load_bmp("color.bmp")
    
    #  データ部の各画素値を半分に
    img2 = [int(v*0.5) for v in img]
    
    #  ヘッダとデータ部 ( 処理後 ) を連結
    data2 = header + bytes(img2)
    
    # BMP ファイルに書き込み
    save_bmp("color2.bmp", data2)    
    
if __name__ == "__main__":
    main()