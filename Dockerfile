FROM amancevice/pandas

COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt

RUN mkdir /myworkdir
WORKDIR /myworkdir
COPY ./ ./

CMD ["python", "app.py"]