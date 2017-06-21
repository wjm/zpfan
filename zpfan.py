import requests, os, time

url = 'http://www.zpfan.com/Home/productdetail.htm?id='
os.makedirs('zpfan', exist_ok=True)
for i in range (1,2060) :
	print('下载第'+str(i)+'个页面中')
	purl = url + str(i)
	r = requests.get(purl, allow_redirects=False)
	if r.status_code == 200 :
		htmlfile=open(os.path.join('zpfan', str(i)+'.htm'),'wb')
		for chunk in r.iter_content(100000) :
			htmlfile.write(chunk)
		htmlfile.close()
	else :
		print('在下载网页 '+purl+' 的时候出现了 '+str(r.status_code)+' 跳转')
	time.sleep(1)
	
print('done')