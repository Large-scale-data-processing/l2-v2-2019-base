# L2 v2 - 2019

## Scope

1. Docker - Dockerfile, docker-compose, containers in general
2. Python - pip, requirements
3. Celery
4. Task queue


## Tasks

1. Investigate existing codebase:
    - why we use a broker
    - why there is no broker URL defined in code
    - how the broker URL is build (what is guest etc.)
    - change RabitMQ logs to appropriate severity (warning)
    - do tasks need to return results?
    - can we schedule periodical tasks?
    - why the worker is logging twice? can we fix that?
    - why we can see celery errors at the beginning?
    - what is the context of docker image building process defined in docker-compose file?
    - can we somehow exclude some files from docker image building context?
2. Decide if you are using an API approach or scrapping based approach. Create fine-grained tasks for everything.
    - Scrapping approach
        1. Implement Twitter page URL provider that will create appropriate tasks
        2. Implement Twitter Page scrapper that utilizes the provided URL and fetch Twitter data:
             - check further tasks to know what date you will need
    - API approach
        1. Get credentials
        2. Select client lib
        3. Create code that will create tasks required for tweets fetching
        4. Create code that will consume tasks and fetch tweets
3. Take care of new tweets fetching. Add appropriate task scheduling, that will fetch new tweets. (How to check if the tweet is new? Utilize current time, tweet creation time, schedule interval)
4. Add process monitoring:
    - Utilize Prometheus or InfluxDB (add them to docker-compose, remember about volumes for data persistency)
    - Publish some metrics about the data fetching process (submission counts, lengths, properties distributions, timings etc.) at least:
        - submission fetch times (avg, histogram)
        - 2 counters 
        - 2 distributions (histogram)
    - publish general celery metrics (you can use a library)
    - Visualize metrics using Grafana (add it to docker-compose, remember about volume for dashboard persistency)
5. Add tox with proper style checking as in List 1, fix all issues. (MUST HAVE!)

