FROM python:3.8

ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"


RUN pip install git+https://github.com/winckles/calculator

CMD [ "python", "./calculator/calculator.py" ]