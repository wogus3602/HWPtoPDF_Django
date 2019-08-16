# boba_HWPtoPDF

## 개발 
------------------------------------------------------------------------------------------------------------------------------------------
||       Version    |      
|---| --------------------- |
|python3|      3.6.8     |  
|django|     2.2.4      |  
|ubuntu|     16.04      |   

---

## hwp -> xhtml
git clone https://github.com/mete0r/pyhwp.git
<br>
<hr>

## xhtml -> pdf
https://www.techoism.com/convert-html-document-to-pdf-on-ubuntu/

---

## 환경 변수 설정
[//]: # ({x-version-update-start:google-cloud-bom:released})
```xml
nano ~/.bashrc
export PATH="$PATH:/root/.local/bin"
export PATH="$PATH:/usr/local/bin"
```
---

## wkhtmltopdf 실행 시 cannot connect server 에러 발생시 해결방법
```
apt-get install xvfb // xvfb 설치
vim /usr/local/bin/wkhtmltopdf.sh  // wkhtmltopdf.sh 파일 생성 
xvfb-run -a -s "-screen 0 640x480x16" wkhtmltopdf "$@"  // vi 편집기를 통해 wkhtmltopdf.sh에 작성
chmod +x /usr/local/bin/wkhtmltopdf.sh // 실행 가능하게 퍼미션 부여
wkhtmltopdf.sh [대상 파일 or 주소] [변환 할 파일명.pdf] // 
```
---
# Result Image

![post_result](./post_result.png)
