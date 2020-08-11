FROM amazonlinux
RUN yum update -y && yum clean all && yum install tar gzip -y

RUN amazon-linux-extras install epel corretto8 -y

RUN printf "[mongodb-org-4.4] \n\name=MongoDB Repository \n\baseurl=https://repo.mongodb.org/yum/amazon/2/mongodb-org/4.4/x86_64/\n\ gpgcheck=1 \n\ enabled=1 \n\ gpgkey=https://www.mongodb.org/static/pgp/server-4.4.asc" > /etc/yum.repos.d/mongodb-org-4.4.repo

RUN yum install -y mongodb-org

#WORKDIR /opt
VOLUME /var/lib/mongo
VOLUME /var/log/mongodb

CMD ["/bin/bash"]