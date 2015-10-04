import multiprocessing

bind = "127.0.0.1:8001"
workers = multiprocessing.cpu_count() * 2 + 1
threads = workers
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "debug"
proxy_allow_ips = "127.0.0.1"
user = "www-data"
group = "www-data"
