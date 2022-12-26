from settings import token
import requests

class YaUploader:
    host='https://cloud-api.yandex.net:443'

    def __init__(self, token):
        self.token = token

    
    def get_upload_link(self,file_name):
        uri='/v1/disk/resources/upload'
        url=self.host+uri
        params={'path':f'/{file_name}', 'overwrite':'true'}
        response=requests.get(url, headers=self.get_headers(), params=params)
        result=response.json()['href']
        return result
        

    def upload_from_pc(self, file_name, disk_file_name):
        upload_link=self.get_upload_link(disk_file_name)
        response=requests.put(upload_link,headers=self.get_headers(), data=open(file_name, 'rb'))
        print(response.status_code)
        if response.status_code== 201:
            print('Загрузка прошла успешно')

    def get_headers(self):
        return {'Content_Type':'application/json', 'Authorization':f'OAuth {self.token}'}

if __name__ == '__main__':
    uploader = YaUploader(token)
    uploader.get_upload_link('2.jpg')
    uploader.upload_from_pc('2.jpg','2.jpg')
    
