FROM anaderi/rep-develop:latest
MAINTAINER Andrey Ustyuzhanin <anaderi@yandex-team.ru>

RUN apt-get install -y libpython3-dev python3-pip vim
RUN apt-get install -y unzip

#LIBS
RUN pip install git+https://github.com/arogozhnikov/hep_ml.git

# George
RUN pip install cython
RUN apt-get install -y libeigen3-dev
RUN pip install git+https://github.com/dfm/george.git


# Bayesian Opt
RUN pip install git+https://github.com/scr4t/BayesianOptimization.git

# Update pandas
RUN pip install -U pandas

# Stuff
RUN pip install astroML
RUN pip install seaborn


RUN pip3 install ipython[all]==3.2.1

# add support for Python2 kernels
RUN ipython2 kernelspec install-self

#
ENV JOBLIB_TEMP_FOLDER /tmp
ENV TERM xterm

RUN mkdir /work
VOLUME /work

EXPOSE 8888
COPY notebook.sh /root/notebook.sh
CMD ["/root/notebook.sh"]
