import wget

url = 'https://drive.google.com/file/d/1gI2XtHpVhO6BD4N7Q41vDbOhJWFgokVc/view?usp=sharing'
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]

file_name = 'train.csv'

wget.download(url, file_name)