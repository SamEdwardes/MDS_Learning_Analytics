FROM amancevice/pandas

COPY requirements.txt /
RUN pip install -r /requirements.txt

RUN mkdir /myworkdir
WORKDIR /myworkdir
COPY ./ ./

RUN mkdir /usr/local/nltk_data
RUN python -m nltk.downloader -d /usr/local/nltk_data stopwords
RUN python -m nltk.downloader -d /usr/local/nltk_data punkt

CMD ["python", "app.py"]