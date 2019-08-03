FROM odoo:12
LABEL maintainer="Daniel <danielvdmlfiis@gmail.com>"

USER root
RUN pip3 install numpy
RUN pip3 install pandas

#WORKDIR /libraries/sympy
RUN python3 setupegg.py develop
