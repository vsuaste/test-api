from locust import HttpUser, task
import query, stress_query_with_search, simple_query_no_search, distributed_pagination, query_association
import local_query, local_pagination, local_association_count
import query_no_data_loader
from locust import events
import locust.stats
import csv
import pandas as pd
from random import randrange
import time
locust.stats.PERCENTILES_TO_REPORT=[0.25, 0.75]

class ZendroStressTest(HttpUser):
    requests = 0
    limit = 100
    url1 = "http://graphql.zendro-dev.org/graphql"
    url2 = "http://siagro01.conabio.gob.mx:3003/graphql"
    num = str(randrange(100000))

    queries_instance1 = query.generate_queries("instance1")
    queries_instance2 = query.generate_queries("instance2")

    stress_queries_instance1 = stress_query_with_search.generate_queries("instance1")
    stress_queries_instance2 = stress_query_with_search.generate_queries("instance2")

    queries_instance1_no = query_no_data_loader.generate_queries("instance1")
    queries_instance2_no = query_no_data_loader.generate_queries("instance2")

    simple_queries = simple_query_no_search.generate_queries()

    local_query_no_search = local_query.generate_queries("simple")
    local_query_search = local_query.generate_queries("search")

    dist_pagination_instance1 = distributed_pagination.generate_queries("instance1")
    dist_pagination_instance2 = distributed_pagination.generate_queries("instance2")

    local_pagi = local_pagination.generate_queries()

    local_assoc_count = local_association_count.generate_queries()

    query_assoc_instance1 = query_association.generate_queries("instance1")
    query_assoc_instance2 = query_association.generate_queries("instance2")

    def context(self):
        return {"num": self.num}

    def post_query(self, name, query, url):
        return self.client.post(url,
            name=name,
            headers={ "Accept": "application/graphql"},
            json={"query": query}
        )

    def collect_raw_data(self, file_name):
        raw_data = pd.read_csv("./result/raw_data_"+self.num+".csv", header=None, index_col=0)
        res = raw_data.groupby([0]).agg(lambda x:','.join(map(str, x.array)))
        res = res[1].str.split(",", expand=True)
        res.to_csv("./result/"+file_name, header=None)

    @events.request.add_listener
    def my_request_handler(name, response_time, exception, context, **kwargs):
        content = response_time
        if exception:
            print(f"Request to {name} failed with exception {exception}")
            content = "fail"
        else:
            print(f"{name}: {response_time}")

        with open("./result/raw_data_"+context["num"]+".csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, content])

    # @task
    # def test_url1(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("test_url1_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.queries_instance1)):
    #             self.post_query(self.queries_instance1[i]["name"], self.queries_instance1[i]["query"], 
    #                 self.url1)
    #         for i in range(len(self.queries_instance2)):
    #             self.post_query(self.queries_instance2[i]["name"], self.queries_instance2[i]["query"], 
    #                 self.url1)
    #         self.requests+=1

    # @task
    # def test_url2(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("test_url2_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.queries_instance1)):
    #             self.post_query(self.queries_instance1[i]["name"], self.queries_instance1[i]["query"], 
    #                 self.url2)
    #         for i in range(len(self.queries_instance2)):
    #             self.post_query(self.queries_instance2[i]["name"], self.queries_instance2[i]["query"], 
    #                 self.url2)
    #         self.requests+=1

    # @task
    # def stress_test_url1(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("stress_test_url1_raw_data_"+self.num+".csv")
    #         # time.sleep(10)
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.stress_queries_instance1)):
    #             self.post_query(self.stress_queries_instance1[i]["name"], self.stress_queries_instance1[i]["query"], 
    #                 self.url1)
    #         for i in range(len(self.stress_queries_instance2)):
    #             self.post_query(self.stress_queries_instance2[i]["name"], self.stress_queries_instance2[i]["query"], 
    #                 self.url1)
    #         self.requests+=1

    # @task
    # def stress_test_url2(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("stress_test_url2_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.stress_queries_instance1)):
    #             self.post_query(self.stress_queries_instance1[i]["name"], self.stress_queries_instance1[i]["query"], 
    #                 self.url2)
    #         for i in range(len(self.stress_queries_instance2)):
    #             self.post_query(self.stress_queries_instance2[i]["name"], self.stress_queries_instance2[i]["query"], 
    #                 self.url2)
    #         self.requests+=1

    # @task
    # def test_url1_no_data_loader(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("test_url1_no_data_loader_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.queries_instance1_no)):
    #             self.post_query(self.queries_instance1_no[i]["name"], self.queries_instance1_no[i]["query"], 
    #                 self.url1)
    #         for i in range(len(self.queries_instance2_no)):
    #             self.post_query(self.queries_instance2_no[i]["name"], self.queries_instance2_no[i]["query"], 
    #                 self.url1)
    #         self.requests+=1

    # @task
    # def test_url2_no_data_loader(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("test_url2_no_data_loader_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.queries_instance1_no)):
    #             self.post_query(self.queries_instance1_no[i]["name"], self.queries_instance1_no[i]["query"], 
    #                 self.url2)
    #         for i in range(len(self.queries_instance2_no)):
    #             self.post_query(self.queries_instance2_no[i]["name"], self.queries_instance2_no[i]["query"], 
    #                 self.url2)
    #         self.requests+=1

    # @task
    # def simple_query_url1(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("simple_query_url1_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.simple_queries)):
    #             self.post_query(self.simple_queries[i]["name"], self.simple_queries[i]["query"], 
    #                 self.url1)
    #         self.requests+=1
    
    # @task
    # def simple_query_url2(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("simple_query_url2_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.simple_queries)):
    #             self.post_query(self.simple_queries[i]["name"], self.simple_queries[i]["query"], 
    #                 self.url2)
    #         self.requests+=1

    # @task
    # def local_query_url1(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("local_query_url1_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.local_query_no_search)):
    #             self.post_query(self.local_query_no_search[i]["name"], self.local_query_no_search[i]["query"], 
    #                 self.url1)
    #         for i in range(len(self.local_query_search)):
    #             self.post_query(self.local_query_search[i]["name"], self.local_query_search[i]["query"], 
    #                 self.url1)
    #         self.requests+=1

    # @task
    # def local_query_url2(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("local_query_url2_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.local_query_no_search)):
    #             self.post_query(self.local_query_no_search[i]["name"], self.local_query_no_search[i]["query"], 
    #                 self.url2)
    #         for i in range(len(self.local_query_search)):
    #             self.post_query(self.local_query_search[i]["name"], self.local_query_search[i]["query"], 
    #                 self.url2)
    #         self.requests+=1

    # @task
    # def baseline_request_response_time(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("basic_response_time_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         self.client.post(self.url1, name='baseline_url1', headers={ "Accept": "application/graphql"})
    #         self.client.post(self.url2, name='baseline_url2', headers={ "Accept": "application/graphql"})
    #         self.requests+=1

    # @task
    # def const_response_time(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("const_response_time_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         self.post_query("const_books_url1", "{ const_books{book_id name} }", self.url1)
    #         self.post_query("const_books_url2", "{ const_books{book_id name} }", self.url2)
    #         self.requests+=1

    # @task
    # def local_pagi_assoc_count_url1(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("local_pagi_assoc_count_url1_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.local_pagi)):
    #             self.post_query(self.local_pagi[i]["name"], self.local_pagi[i]["query"], 
    #                 self.url1)
    #         for i in range(len(self.local_assoc_count)):
    #             self.post_query(self.local_assoc_count[i]["name"], self.local_assoc_count[i]["query"], 
    #                 self.url1)
    #         self.requests+=1

    # @task
    # def local_pagi_assoc_count_url2(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("local_pagi_assoc_count_url2_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.local_pagi)):
    #             self.post_query(self.local_pagi[i]["name"], self.local_pagi[i]["query"], 
    #                 self.url2)
    #         for i in range(len(self.local_assoc_count)):
    #             self.post_query(self.local_assoc_count[i]["name"], self.local_assoc_count[i]["query"], 
    #                 self.url2)
    #         self.requests+=1

    # @task
    # def dist_pagi_url1(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("dist_pagi_url1_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.dist_pagination_instance1)):
    #             self.post_query(self.dist_pagination_instance1[i]["name"], self.dist_pagination_instance1[i]["query"], 
    #                 self.url1)
    #         for i in range(len(self.dist_pagination_instance2)):
    #             self.post_query(self.dist_pagination_instance2[i]["name"], self.dist_pagination_instance2[i]["query"], 
    #                 self.url1)
    #         self.requests+=1

    # @task
    # def dist_pagi_url2(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("dist_pagi_url2_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.dist_pagination_instance1)):
    #             self.post_query(self.dist_pagination_instance1[i]["name"], self.dist_pagination_instance1[i]["query"], 
    #                 self.url2)
    #         for i in range(len(self.dist_pagination_instance2)):
    #             self.post_query(self.dist_pagination_instance2[i]["name"], self.dist_pagination_instance2[i]["query"], 
    #                 self.url2)
    #         self.requests+=1

    @task
    def dist_pagi_url2(self):
        if self.requests==self.limit:
            self.collect_raw_data("query_assoc_url2_raw_data_"+self.num+".csv")
            self.environment.runner.quit()
        else:
            for i in range(len(self.query_assoc_instance1)):
                self.post_query(self.query_assoc_instance1[i]["name"], self.query_assoc_instance1[i]["query"], 
                    self.url2)
            for i in range(len(self.query_assoc_instance2)):
                self.post_query(self.query_assoc_instance2[i]["name"], self.query_assoc_instance2[i]["query"], 
                    self.url2)
            self.requests+=1

    # @task
    # def dist_pagi_url1(self):
    #     if self.requests==self.limit:
    #         self.collect_raw_data("query_assoc_url1_raw_data_"+self.num+".csv")
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.query_assoc_instance1)):
    #             self.post_query(self.query_assoc_instance1[i]["name"], self.query_assoc_instance1[i]["query"], 
    #                 self.url1)
    #         for i in range(len(self.query_assoc_instance2)):
    #             self.post_query(self.query_assoc_instance2[i]["name"], self.query_assoc_instance2[i]["query"], 
    #                 self.url1)
    #         self.requests+=1