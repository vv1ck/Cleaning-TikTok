try:
	import threading
	from requests import get,post
	from time import sleep
	from json import JSONDecodeError
except Exception as Joker:input(Joker);exit()
PRNT=threading.Lock()
red = "\033[1;31;40m";yel = '\033[1;33;40m'
grn = '\033[1;32;40m';errorSN='"session expired, please sign in again"'
def vv1ck(*a, **b):
	with PRNT:print(*a, **b)
class TikTok_followers:
	def __init__(self,ID,SEC,S):
		self.sisn=S
		self.ID=ID
		self.SEC=SEC
		self.err=0
		print('━━━━━━━━━━━━━'*3,'\n')
		self.url='https://api16-normal-c-alisg.tiktokv.com/aweme/v1/user/follower/list/?ac=WIFI&op_region=JO&app_skin=white&vcd_count=0&offset=0&address_book_access=1&gps_access=0&sec_user_id={}&count=20&source_type=1&user_id={}&vcdAuthFirstTime=0&max_time=0&'
		self.headers={'Host': 'api16-normal-c-alisg.tiktokv.com','Connection': 'keep-alive','x-Tt-Token': '01'+self.sisn+'022d273d75acc99d264eed0ede586d4abf9748ef61ac9d7b7e374ee7a183f5c064993edfd37584b60d89456cd050a8f6d5d3aed733504c196492e73fad0ec24d68b1aab6d4eb934387b469c487eb2fe634f-1.0.1','sdk-version': '1','User-Agent': 'TikTok 16.6.0 rv:166011 (iPhone; iOS 13.5; ar_JO@numbers=latn) Cronet','x-tt-store-idc': 'alisg','x-tt-store-region': 'jo','X-SS-DP': '1233','x-tt-trace-id': '00-f93ad7fa106178e4fb15d8c6051a04d1-f93ad7fa106178e4-01','Cookie': 'sessionid='+self.sisn,'X-Khronos': '1636268954','X-Gorgon': '8402c0f720009a44d6aa4efafa6015fd7e1bdbe057fa07330a57','x-common-params-v2': 'pass-region=1&pass-route=1&language=ar&version_code=16.6.0&app_name=musical_ly&vid=D89D043C-FEE3-4404-895E-C9536618B96F&app_version=16.6.0&is_my_cn=0&channel=App%20Store&mcc_mnc=&device_id=7023615385938740741&tz_offset=7200&account_region=&sys_region=JO&aid=1233&residence=JO&screen_width=750&uoo=0&openudid=b391b6c4a559f59af4481dcf8899e10de5f73803&os_api=18&os_version=13.5&app_language=ar&tz_name=Asia/Amman&current_region=JO&device_platform=iphone&build_number=166011&device_type=iPhone8,1&iid=7027721008694167297&idfa=3D876826-942D-4BFE-A9AA-5E34E6A6E72D&locale=ar&cdid=6C789D0F-7930-40F5-9C6E-422B790044F7&content_language='}
		self.get_followers()
	def UNfollos(self):
		global IDS,User
		get('https://api16-normal-c-alisg.tiktokv.com/aweme/v1/remove/follower/?device_id=7023615385938740741&os_version=13.5&is_my_cn=0&residence=JO&iid=7027721008694167297&app_name=musical_ly&pass-route=1&locale=ar&pass-region=1&ac=WIFI&sys_region=JO&version_code=16.6.0&vid=D89D043C-FEE3-4404-895E-C9536618B96F&channel=App%20Store&op_region=JO&os_api=18&idfa=3D876826-942D-4BFE-A9AA-5E34E6A6E72D&device_platform=iphone&device_type=iPhone8,1&openudid=b391b6c4a559f59af4481dcf8899e10de5f73803&account_region=&tz_name=Asia/Amman&tz_offset=7200&current_region=JO&build_number=166011&app_skin=white&aid=1233&mcc_mnc=&screen_width=750&uoo=0&content_language=&language=ar&cdid=6C789D0F-7930-40F5-9C6E-422B790044F7&app_language=ar&app_version=16.6.0&user_id='+IDS,headers={'Host': 'api16-normal-c-alisg.tiktokv.com','Connection': 'keep-alive','x-Tt-Token': '01'+self.sisn+'022d273d75acc99d264eed0ede586d4abf9748ef61ac9d7b7e374ee7a183f5c064993edfd37584b60d89456cd050a8f6d5d3aed733504c196492e73fad0ec24d68b1aab6d4eb934387b469c487eb2fe634f-1.0.1','sdk-version': '1','User-Agent': 'TikTok 16.6.0 rv:166011 (iPhone; iOS 13.5; ar_JO@numbers=latn) Cronet','x-tt-store-idc': 'alisg','x-tt-store-region': 'jo','X-SS-DP': '1233','x-tt-trace-id': '00-f93c8446106178e4fb15d8c605e304d1-f93c8446106178e4-01','Cookie': 'sessionid='+self.sisn,'X-Khronos': '1636269064','X-Gorgon': '8402804b2000404e2e2fba468c29cf17bdafe7599d87e5ebe60c'})
		vv1ck(red+f'[+] UNfollo >> {User}')
	def get_followers(self):
		global IDS,User
		while 1:
			GET=get(self.url.format(self.SEC,self.ID),headers=self.headers)
			try:
				IDS =str(GET.json()['followers'][0]['uid'])
				User=GET.json()['followers'][0]['unique_id']
				self.UNfollos()
			except IndexError:
				self.err+=1
				if self.err==6:input(grn+'[+] Deleted successfully ✅');exit('By Joker')
				else:pass
			except JSONDecodeError:
				input(yel+'[!] Please try again later ..');exit()
"|######################|"
class TikTok_following:
	def __init__(self,ID,SEC,S):
		self.sisn=S
		self.ID=ID
		self.SEC=SEC
		vv1ck('━━━━━━━━━━━━━'*3,'\n')
		self.err=0
		self.get_following()
	def UNfollog(self,IDS,User):
		UNful=get('https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/follow/user/?ac=WIFI&js_sdk_version=1.77.0.2&op_region=JO&tma_jssdk_version=1.77.0.2&idfv=3D876826-942D-4BFE-A9AA-5E34E6A6E72D&user_id='+IDS+'&type=0&sec_user_id=&previous_page=following&',headers={'Host': 'api16-normal-c-alisg.tiktokv.com','User-Agent': 'TikTok 20.5.0 rv:205020 (iPhone; iOS 13.5; ar_JO@numbers=latn) Cronet','Cookie': 'sessionid='+self.sisn,'X-Argus': '6GcIPqHpj254NmWUQL7H2Y32q5Q0QZLjlWwr0QTX1MpzlcXKoHOcsmP6+NLaE9b5DAW40Z4nUMke/0kjuA7g+HXRdtVWir2xSSqxQhdU3cGG9Nc70ZbMsdIZqvbJ4sYVboUdmSJiwMJjvN4SU025JXkYEOpJTpAnSr6Yk4Z96eKzfG8zUJj1rBwpVN2TM2363C2yFFqCg1L52DjKc50pzKBrq23xGVicI9U7Zy/2A1yomyGqq1z8etvIFFuxs+xWeBDdsv77mIkCXQysy4g8PpG78Z0IwNmHSg0Go4OkfEQ123MNUd+bHmAVwyrm6hgUVTmZy6BIiBNqiddYlVbEISwr','X-Gorgon': '8404e0580000025b62c8b99cbe848daa3db9a1398962887e142b','x-common-params-v2': 'language=ar&version_code=20.5.0&app_name=musical_ly&app_version=20.5.0&channel=App%20Store&mcc_mnc=&device_id=7023615385938740741&tz_offset=7200&account_region=&sys_region=JO&aid=1233&residence=JO&screen_width=750&uoo=0&openudid=4bf5c9491d8f851bee9cb8a73a48ce3935a30d6b&os_api=18&os_version=13.5&app_language=ar&tz_name=Asia/Amman&current_region=JO&device_platform=iphone&build_number=205020&device_type=iPhone8,1&iid=7027405281118750470&idfa=3D876826-942D-4BFE-A9AA-5E34E6A6E72D&locale=ar&cdid=A0DF5056-F002-4CF3-B02A-1E362753CC57&content_language='})
		vv1ck(grn+f'[+] UNfollo >> {User}')
	def get_following(self):
		while 1:
			sleep(1)
			GET=get('https://api2-16-h2.musical.ly/aweme/v1/user/following/list/?version_code=12.0.0&pass-region=1&pass-route=1&language=ar&app_name=musical_ly&vid=D89D043C-FEE3-4404-895E-C9536618B96F&app_version=12.0.0&residence=JO&is_my_cn=0&channel=App%20Store&mcc_mnc=&device_id=7023615385938740741&tz_offset=7200&account_region=&sys_region=JO&aid=1233&screen_width=750&uoo=0&openudid=b391b6c4a559f59af4481dcf8899e10de5f73803&os_api=18&ac=WIFI&os_version=13.5&app_language=ar&tz_name=Asia/Amman&current_region=JO&device_platform=iphone&build_number=120008&device_type=iPhone8,1&iid=7027799084266424070&idfa=3D876826-942D-4BFE-A9AA-5E34E6A6E72D&offset=0&sec_user_id='+self.SEC+'&address_book_access=1&gps_access=0&source_type=2&count=20&user_id='+self.ID+'&max_time=0',headers={'Host': 'api2-16-h2.musical.ly','Connection': 'keep-alive','x-tt-store-idc': 'alisg','x-tt-store-region': 'jo','X-SS-DP': '1233','Cookie': 'sessionid='+self.sisn,'X-Khronos': '1636287035','X-Pods': '','X-Gorgon': '8300a60d2001fef8e08b3f7d1eccb4d6a997682985911a998c64','x-Tt-Token': '01'+self.sisn+'0127e2928aa6c29cf7d2757d13ce88f5ec64ced2158c43e6ef61b50bff98482ea80c13528d2a7b2a60028586c336e666116a2255f4944a0502d22f8ed33da2725a37d3ec2c6532b9d3da0054924e91eef7b-1.0.1','User-Agent': 'TikTok 12.0.0 rv:120008 (iPhone; iOS 13.5; ar_JO@numbers=latn) Cronet'})
			try:
				IDS =GET.json()['followings'][0]['uid']
				User=GET.json()['followings'][0]['unique_id']
				self.UNfollog(str(IDS),User)
			except KeyError:
				input(yel+'[!] Please try again later ..');exit()
			except IndexError:
				self.err+=1
				if self.err==6:input(grn+'[$] Deleted successfully ✅');exit('By Joker')
				else:pass
			except JSONDecodeError:
				input(yel+'[!] Please try again later ..');exit()
"|==============|"
def get_ID(M0D):
	S=input('\n$:~ Enter sessionid : ')
	if S:pass
	else:input('$:~ Please enter a sessionid : ')
	GET_ID=get('https://api16-normal-c-alisg.tiktokv.com/passport/account/info/v2/?scene=normal&multi_login=1&account_sdk_source=app&passport-sdk-version=19&os_api=25&device_type=A5010&ssmix=a&manifest_version_code=2018093009&dpi=191&carrier_region=JO&uoo=1&region=US&app_name=musical_ly&version_name=7.1.2&timezone_offset=28800&ts=1628767214&ab_version=7.1.2&residence=SA&cpu_support64=false&current_region=JO&ac2=wifi&ac=wifi&app_type=normal&host_abi=armeabi-v7a&channel=googleplay&update_version_code=2018093009&_rticket=1628767221573&device_platform=android&iid=7396386396296286392&build_number=7.1.2&locale=en&op_region=SA&version_code=200705&timezone_name=Asia%2FShanghai&cdid=f61ca549-c9ee-450b-90da-8854423b74e7&openudid=3e5afbd3f6dde322&sys_region=US&device_id=7296396296396396393&app_language=en&resolution=576*1024&device_brand=OnePlus&language=en&os_version=7.1.2&aid=1233&mcc_mnc=2947',headers={'Host': 'api16-normal-c-alisg.tiktokv.com', 'Cookie': 'sessionid='+S,'Accept-Encoding': 'gzip, deflate',
	'User-Agent': 'com.zhiliaoapp.musically/2022107060 (Linux; U; Android 7.1.2; en_US; G011A; Build/N2G48H;tt-ok/3.10.0.2)'})
	if errorSN in GET_ID.text:input(red+'[!!] The session is not working !!')
	elif 'user_id' in GET_ID.text:
		ID=str(GET_ID.json()['data']['user_id'])
		SEC=GET_ID.json()['data']['sec_user_id']
		if M0D==1:TikTok_following(ID,SEC,S)
		elif M0D==2:TikTok_followers(ID,SEC,S)
	else:vv1ck(GET_ID.text)
if __name__ == '__main__':
	M0D=int(input('''          .-"""-.
        //       \\   Cleaning TikTok
        \\       //     By JR @vv1ck
 .-"""-.-`.-.-.<  _
/      _,-\ ()()_/:)
\     / ,  `     `| 
 '-..-| \-.,___,  / 
       \ `-.__/  / 1- Delete following
        `-.__.-'` 2- Delete followers '''));get_ID(M0D)
