from PIL import Image
import requests
from io import BytesIO
import numpy as np
import streetview

create_url = lambda _panoid,_x, _y: "https://cbk0.google.com/cbk?output=tile&panoid=%s&zoom=4&x=%d&y=%d" % (_panoid,_x,_y)


def download_general(path, x, y, x_span, y_span):
    
    panoids = streetview.search_panoramas(lat=x/10000, lon=y/10000)
    pano_shape = 512
    img = np.zeros((pano_shape*y_span, pano_shape*x_span, 3), dtype="uint8")
    for i in range(x_span):
        for j in range(y_span):
            panoid =panoids[0].pano_id
            url = create_url(panoid,i, j)
            print(url)
            im = np.array(Image.open(BytesIO(requests.get(url).content)))
            img[j*pano_shape:(j+1)*pano_shape, i*pano_shape:(i+1)*pano_shape, :] = im
            
    Image.fromarray(img).save(path)

for x in range(407538,408000,2):
    for y in range(-739969,-739000,2):
       download_general("%d_%d.png"%(x,y), x, y, 2, 2)     

#download_general("b.png", 290479, 173745, 4, 4)