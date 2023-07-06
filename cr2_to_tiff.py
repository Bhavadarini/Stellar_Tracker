import rawpy
import tifffile
import exifread
import json

image=input("Enter filename: ")
tiff_img=input("Enter name(base name only) of output file: ")+".tif"
with rawpy.imread(image) as raw:
    raw_data=raw.postprocess(gamma=(1,1),no_auto_bright=True,output_bps=16) #raw_image_visible.astype('uint16')
# writing metadata
f=open(image,'rb')
tags=dict(exifread.process_file(f))
meta=""
for i in tags.keys():
    if i not in ['JPEGThumbnail','TIFFThumbnail','Filename','EXIF MakerNote']:
        meta+="\n"+str(i)+"\t"+str(tags[i])
f.close()

meta=json.dumps(meta)
tifffile.imwrite(tiff_img,raw_data,description=meta)


