from PIL import Image
import requests
from io import BytesIO
import numpy as np

create_url = lambda _x, _y: "https://khms0.google.com.tr/kh/v=863?x=%d&y=%d&z=19" % (_x,_y)
def download_2x2(path, x, y):
    urls = [ create_url(x,y), create_url(x+1,y), create_url(x,y+1), create_url(x+1,y+1) ]
    imgs = [ np.array(Image.open(BytesIO(requests.get(url).content))) for url in urls ]

    img = np.zeros((512, 512, 3), dtype="uint8")

    img[:256, :256, :] = imgs[0]
    img[:256, 256:, :] = imgs[1]
    img[256:, :256, :] = imgs[2]
    img[256:, 256:, :] = imgs[3]

    Image.fromarray(img).save(path)

def download_general(path, x, y, x_span, y_span):
    img = np.zeros((256*y_span, 256*x_span, 3), dtype="uint8")
    for i in range(x_span):
        for j in range(y_span):
            url = create_url(x+i, y+j)
            im = np.array(Image.open(BytesIO(requests.get(url).content)))
            img[j*256:(j+1)*256, i*256:(i+1)*256, :] = im
            
    Image.fromarray(img).save(path)

for x in range(268982,269017,2):
    for y in range(175749,175847,2):
       download_general("%d_%d.png"%(x,y), x, y, 2, 2)     

#download_general("b.png", 290479, 173745, 4, 4)