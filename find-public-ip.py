from requests import get

def main():
    ip = get('https://api.ipify.org').text
    print('My Public IP Address is: {}'.format(ip))

if __name__ == '__main__':
        main()
