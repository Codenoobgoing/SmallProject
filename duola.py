from PIL import Image
import time

start  = time.time()
code = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`''. '
count =len(code)

def transfrom(image_file):
    pic=''
    imode = list(image_file.getbands())
    print('原图通道：', imode)
    print('原图像素：',image_file.size)
    for h in range(0,image_file.size[1]):
        for w in range(0,image_file.size[0]):
            if imode[-1]=='A':
                r,g,b,a = image_file.getpixel((w,h))
            elif imode[-1]=='B':
                r,g,b = image_file.getpixel((w,h))
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            #gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            pic = pic+code[int((count-1)*gray/256)]
        pic = pic+'\r\n'
    return pic

f = open("test.jpg",'rb')
image_file = Image.open(f)
image_file = image_file.resize((int(image_file.size[0]*1),int(image_file.size[1]*1)))
print('字符画像素:',image_file.size[0],' ',image_file.size[1])
end = time.time()
print('耗时：',end-start,'s')

tem = open("test.txt",'w')
tem.write(transfrom(image_file))
tem.close()




#"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
#gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
#code = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`''. '