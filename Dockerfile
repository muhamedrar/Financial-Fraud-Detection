FROM astrocrpublic.azurecr.io/runtime:3.1-3



COPY scripts /usr/local/airflow/scripts

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt


