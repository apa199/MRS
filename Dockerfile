FROM python:3.12

# Expose port you want your app on
EXPOSE 8501
WORKDIR /app
# Upgrade pip and install requirements
COPY requirements.txt requirements.txt
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*
RUN pip install -U pip
# # RUN pip install -r requirements.txt
# # RUN git clone https://github.com/streamlit/streamlit-example.git .

RUN pip install -r requirements.txt
COPY . .

# Copy app code and set working directory

CMD streamlit run app.py


# # Run

# ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
