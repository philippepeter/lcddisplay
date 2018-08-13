FROM alpine:3.8

RUN apk add python
RUN apk add py-pip
#RUN pip install --upgrade pip --default-timeout=100
RUN pip install pySerial --default-timeout=100
RUN printf "import time\nimport serial\nimport sys\nif len(sys.argv) == 2:\n  lcdstring=sys.argv[1]\n  print 'lcstring=', lcdstring\n  ser = serial.Serial('/dev/ttyACM0', 9600)\n  time.sleep(2)\n  ser.write(lcdstring.encode())" >> lcdscript.py
RUN cat lcdscript.py
ENTRYPOINT ["python","lcdscript.py"]
