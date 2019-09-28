# encoding=utf-8

from PIL import Image
import string,json
out=[]
metrics=[0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x05, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x04, 0x04 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x04 ,
0x06, 0x03, 0x07, 0x06, 0x07, 0x06, 0x07, 0x03 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x07, 0x07 ,
0x08, 0x08, 0x05, 0x08, 0x08, 0x07, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x04, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x07, 0x07, 0x08, 0x08 ,
0x04, 0x07, 0x08, 0x04, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x07, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08 ,
0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08]+([0x08]*200)

with open('both.bin','rb') as f:
	outnum=0
	while True:
		width,height=metrics[outnum],0x0C
		sz=((width+7)//8)*height
		data=f.read(sz)
		if len(data)!=sz:
			break
		chars=''.join(['{0:08b}'.format(ord(c)) for c in data])
		chars=chars.replace('0','\0\0\0\xFF').replace('1','\xFF\xFF\xFF\xFF')
		im = Image.frombytes('RGBA',(width,height),chars)
		out.append(im)
		im.save('out/{}.png'.format(outnum))
		outnum+=1
if 1:
	w=sum(im.size[0] for im in out)
	h=out[0].size[1]
	outim=Image.new('RGBA',(w,h))
	outim.paste((255,0,255,255),(0,0,w,h))
	outx=0
	sizedata={
		'default':{
			'h':12,
			'y':0
		}
	}
	CHARS=(
		u' ()\0\u2E41+./0123456789'+
		string.ascii_uppercase+
		string.ascii_lowercase+
		u'=!"$%&*:?－[]'+
		u'。\'#\0←↑↓→+\0\0\0“”'+
		u'⓪☯⮋@ȦÄÇĖËȮÖ\0Ü'+
		u'àậáäçèêéëìîíï'+
		u'ùûúüòóôö'+
		u'Ññ♪♫Ï\0\0\0\0\0Ⓔ\0\0\0\0\0\0\0『』'+
		u'×＆☆□△※<>~⋯\0\0·「」＃\0／\0\0\0'+
		u'_○\0\0-０１２３４５６７８９％,;〈〉'
	)

	for i,im in enumerate(out):
		x,y=outx,0
		outim.paste((0,0,0,255),(x,y,x+im.size[0],y+h))
		outim.paste(im,(x,y),im)
		#if i<len(CHARS):
			#char=ord(CHARS[i])
			#if char!=0:
#				sizedata[char]={'x':outx, 'w':mw}
		outx+=im.size[0]+1

	outim.save('yi-font.png')
