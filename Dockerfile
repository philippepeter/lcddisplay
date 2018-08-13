FROM alpine:3.8

RUN apk add python
RUN apk add py-pip
RUN pip install --upgrade pip --default-timeout=100
RUN pip install pySerial --default-timeout=100
RUN printf "import serial\nlcdstring=\"${lcdstring}\"\nif lcdstring:\n  ser = serial.Serial('/dev/ttyACM0', 9600)\n  ser.write('${lcdstring}'.encode())" >> lcdscript.py
RUN cat lcdscript.py
RUN python lcdscript.py
