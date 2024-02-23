import pandas as pd
import requests as req
import json    


districts = ['東區','西區','南區','北區','中區','西屯區','北屯區','南屯區']

# api的網址需要手動抓下來，每過一段時間就需要更新網址，否則抓不到任何資訊。
urls = ['https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/091f118f42a00663d4f414b16de460d3?q=VTJGc2RHVmtYMTljMWdaeDJWcjRRRU1xTkNzR3Bsd21uZ0UzeXNaWkNHMi9laS8zcG9ZbjdJV1JTY0djaUYwNms4UWQzTll5QjZoK0VVT3dJZG1SM3VneUJRTkhGQkJXS3I0UFRZU3ZpbjdDamJHYWU3TVhsaGhKdnNFdlgrR1JZWVJnNmMrblp0UjZ4U0hxREdhaHJVSjFmbks2ZmtkY0t6bnNBa0pDOWQrdS9JNEVKaW03TGV4V21qUzMzTnB5dEJuZ1JlKzR3VWF2dG9SZWR6cXJOV3pQMWdPSWlObW9jOFk1aGU2dFR0TklJek1oY1Z6RDVZQzMxdU9OdE4rTUUyT0hsRjMvWVIxbUxvMExIQ3U5S3JVa013OHBtZFBwTUY2MVdJTjNpZVVjMHNPVUxEM3VQSVpIdGlCcUpLREdEc3RJN0RZQSsxWmdWTWwzazVJY0o5YmsyVy9iY3U5RVlyL2FGWVY1MkZ1eFBFaTZnOCtFVUJXUTR5MFhZSVRpYWxNLzFJa1ZDR3duazZrN3I1YlhVRkhkcDdFTURsRVNRWUJyTEUrZEJ0Q045alFFbGw1M0svNXFJOHNwbDRXMTN0ZUFPbmNyWUV6UlhTd1lsNVJGZUs3NzVHTnlFQnNJNk9QV1RtSnowempxeFlDZVl5eDR3VnhBclZEdUFrbFF4VlZwaTJsNjlRZ0dlVWhWUXJJaXdiUkM0TWcvVExabVp3akpuR1JtT3FHelhaRWsrSmp3QlNzbnlVb1FRenNiZDZVZlE2NXdoMFhacmFmaStHenZTTmhIRmhaV2o4KzJzTU1aekZiaEJYQXhTV0tSWXNYQ09UZGRXZmxrUmFtTWxJKzFSMlVNaTUzV1NhbHlRcjErVjRvYnBQN0FKeEthei9CZVF1ZEtHRVJvS2M4d2t2WGdYSk5KKzB5cWQwbnM3d2M4TEN0aUZ5RzVCTlZBOWhCY0Z3PT0=',
        'https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/103fa5a68df69a15ffd3d4d4c78652be?q=VTJGc2RHVmtYMS9sUWw2VzJWQXBmK1VaTURmZDR2alZPMGZuQ3I5QTYrUkpRc0RFdzFjL1BVc0JET3NlNlBJUlAwWTFONHluQzRvL3RtVCtHREpCQkFtTDdnN2xPbDNrc2tScmg1YUxXWTlTQmYyOGF0RUJicTFweWNFMFFiMkpTR1RKMjkxQmVXeU1IdE5BMGRNbkZRbDdPM3BUSG05aTQvdlZsQWpMQTRsY05XVkhGWDArMXIvUEIwa256dkRBWEZMREtkd0RsRlBZMnN1ZDVzN2NBSWs0OU9HK0xPMlVYSFhDS1JjdlJYcERKdTVGRlBLMDRxRFVxMkJHTzV5bzF0YnFDM3lXSE1rdEdYOXhBZWJKT1BaOHR0RWdhcElGTFpQN3JFME1KSklHaTJqbDBjZFJOVFZoY0tNVnFWL1BJbmh1d0Fod1pIbTl1aExBTDJHbE4zZzByaVpvNnYzZGh4Mjc5RnhZbTFoYkF0enpuZ2VXcytPRGNDYTdMbk9wRDNiT0NhS3hkVEtZb2dXT1g3cHhycTBZVU9BVGpVdytRZC9rQkZmd01uMGo5dmpMUVRVVzlHS2lGWmZSVjN4c2dhYlBRa1pXRFZnVG43OEdGV2hVcjNKSWlPaFRkN0gyU2VCMThYNDlDcmpPYko4Mmp6R3dsUUtsWVdDRjFCQkhlb2E0V0tvdE9UNDBFd1VockU1b1A5T0tnUit4M25ZTHZZVWxqY1hsTU9UNXFrRGgrSnNLSVcrSk9GMFljNzFPak8wdG5EbXBDRS92MWRMcG4wNkl1cnFhVmNZQkxGOXFrOUNrSFpVcWlDUG4zckRCdklZc09sMHNlMTFTb0pYM0xCVFluNFgrSXFvVkh5RkZZMXY0dWdIeHZ5aUNZdWQrZEVSWlFjQTFVc1plbW1RWC83cDdDbFBBYWxrSjQydzlnZGttVFJoNzY3ejNRV2dkNmlMUTFnPT0=',
        '',
        '',
        'https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/8eb12279a698f70698e6005a5e81c2fc?q=VTJGc2RHVmtYMStYelFjK3VvaHVsS1NpQTQ4OVp6cUhkNTVwV0lXVFE1bGFxcm5MSXRsWjZyQlRMb1Z1d1ZmOTc2eFRtV0ZhZktTYVcrK1FSeUZCRU1Zc0dHTkVSWS9OeExsbDExV3N4R2NHbkdXZ3lxKzRnS0tkRVlwVnFxeGEweFhqM0x0QnRWZ1FQUlhmZFZCNGVoU0luSzNndTl0YW02QlVUeW5lZW9yNE5JUFhtdkgyQ2wyUVJDcDlKa2duZUNRSEhXYUV4T0pwdmM0aFRsWkJISDlKYy9XLy9rQ0ZkUVo3ZldsYVU4cFpnYkJDR0tUbVpSc2RhRWJ1elRHMjl1KzRsalI3aFNWdjFLUjkvU2ZDOWhLeXJveEpqcUtybVh0ZmdnWDM4cUxhNGhUZDM1NkVjZUFPWUIzdWRmRGtkRXhhL0hrNmo4cFBpdGMwTnUwRHN5cW1PWExwU1RscHhETG1TM3FvZkt1aUZHajliaHcxWDQxbzVxUFdlSk5LeGdGK1BxQTcyeUMwSWh3ckVXTVZMWlZKUE13UnVHblVKMTRJWXVURm5hQmVsUEVORC9JYzRsY2NacVBRYmtBRkU2Ym5VaElGT3U1dXduTFZYUEQ2dzFRQ0krZmp3eHpxTHBUYnRUZXRUVXZpbkNhK0pxSDlqVEZpWmhNK1dFRzlSMkR6akZyWmhuUkNoM0dvLzRKekl6TU9rRzlOT2JVU3k1bkpqRnJyNGNrVThPTTB2eDRpQXpxa2ZKUkIwU2hUKzlnVWQxZ0VvbkZtcFJ4dWdyWHM2SUdEeHVBSkdFNERyLzBLRkF6T2FoYnUxTnpTK1FUYVkxUWJiUVgvdDJETE84bnJhK3lyb0lCbFlvSWdZc0o2UlNHdGtZZGlscDBadnJzcU1WSXFqcUMrdzEyMWFOQ2VmTmE4UyswUW9lTmI4Ly9JdEVpVHp0ZWVVOTRFb05wcCt3PT0=',
        '',
        '',
        '',
        ]

df = pd.DataFrame()
for i in range(0,8):
    print('正再爬取 「{0}」 106年月至111年1月的資料'.format(districts[i]))
    resp=req.get(urls[i])
    data=json.loads(resp.text)
    print('一共抓到 {0} 筆台中市{1} 101年8月至111年12月的資料'.format(len(data),districts[i]))

    house_object=[]
    for object in data :  
        one_object={}              
        one_object['經度']= object['lon']            # 經度
        one_object['緯度']= object['lat']            # 緯度     
        one_object['屋齡'] = object['g']             # 屋齡
        one_object['面積'] = object['s']             # 面積    
        one_object['建物類型'] = object['b']         # 建物型態     
        one_object['用途'] = object['pu']            # 主要用途    
        one_object['樓別/樓高'] = object['f']        # 樓別/樓高   
        one_object['佈局'] = object['v']            # 幾房幾衛幾廳
        one_object['電梯'] = object['el']           # 有無電梯       
        one_object['管理員'] = object['m']          # 有無管理員          
        one_object['車位數量'] = object['l']        # 車位數量   
        one_object['成交日期'] = object['e']        # 成交日期   
        one_object['價格'] = object['tp']           # 價格
        house_object.append(one_object)

    #--- 將原始數據保存到 CSV 檔案
    cols=['經度','緯度','屋齡','面積','建物類型','用途',
        '樓別/樓高','佈局','電梯','管理員','車位數量',
        '成交日期','價格']
    df_house = pd.DataFrame (house_object, columns = cols) # 將list 轉換為 dataframe
    df_house['行政區'] = districts[i]
    df_house['交易年份'] = df_house['成交日期'].apply(lambda x: x.split('/')[0])        
    df = pd.concat([df,df_house],axis=0)
    
df.drop(['成交日期'],axis=1,inplace=True)
df = df.reset_index(drop=True)
print('完成')


df.to_csv('台中市房價.csv',index=False)