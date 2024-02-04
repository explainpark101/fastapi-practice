from config.settings import DEBUG, BASE_DIR, PORT
import uvicorn
import os

if __name__ == "__main__":
    print("현재 서버의 ip주소목록")
    for ip_address in os.popen('ipconfig').read().split('\n'):
        if 'IPv4' in ip_address:
            ip_address = ip_address.split(":")[-1]
            print(f'\thttp://{ip_address.strip()}:{PORT}')
    uvicorn.run("config:app", host='0.0.0.0', port=PORT, reload=DEBUG)