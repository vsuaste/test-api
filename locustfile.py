from locust import HttpUser, task
import query, stress_query_with_search, simple_query_no_search, query_no_data_loader, local_query

class ZendroStressTest(HttpUser):
    requests = 0
    limit = 100
    url1 = "http://graphql.zendro-dev.org/graphql"
    url2 = "http://siagro01.conabio.gob.mx:3003/graphql"

    queries_instance1 = query.generate_queries("instance1")
    queries_instance2 = query.generate_queries("instance2")

    stress_queries_instance1 = stress_query_with_search.generate_queries("instance1")
    stress_queries_instance2 = stress_query_with_search.generate_queries("instance2")

    queries_instance1_no = query_no_data_loader.generate_queries("instance1")
    queries_instance2_no = query_no_data_loader.generate_queries("instance2")

    simple_queries = simple_query_no_search.generate_queries()

    local_query_no_search = local_query.generate_queries("simple")
    local_query_search = local_query.generate_queries("search")

    def post_query(self, name, query, url):
        return self.client.post(url,
                name=name,
                headers={ "Accept": "application/graphql"},
                json={"query": query}
            )
    # @task
    # def test_url1(self):
    #     if self.requests==self.limit:
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
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.stress_queries_instance1)):
    #             self.post_query(self.stress_queries_instance1[i]["name"], self.stress_queries_instance1[i]["query"], 
    #                 self.url2)
    #         for i in range(len(self.stress_queries_instance2)):
    #             self.post_query(self.stress_queries_instance2[i]["name"], self.stress_queries_instance2[i]["query"], 
    #                 self.url2)
    #         self.requests+=2

    # @task
    # def test_url1_no_data_loader(self):
    #     if self.requests==self.limit:
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
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.simple_queries)):
    #             self.post_query(self.simple_queries[i]["name"], self.simple_queries[i]["query"], 
    #                 self.url1)
    #         self.requests+=1
    
    # @task
    # def simple_query_url2(self):
    #     if self.requests==self.limit:
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.simple_queries)):
    #             self.post_query(self.simple_queries[i]["name"], self.simple_queries[i]["query"], 
    #                 self.url2)
    #         self.requests+=1

    # @task
    # def local_query_url1(self):
    #     if self.requests==self.limit:
    #         self.environment.runner.quit()
    #     else:
    #         for i in range(len(self.local_query_no_search)):
    #             self.post_query(self.local_query_no_search[i]["name"], self.local_query_no_search[i]["query"], 
    #                 self.url1)
    #         for i in range(len(self.local_query_search)):
    #             self.post_query(self.local_query_search[i]["name"], self.local_query_search[i]["query"], 
    #                 self.url1)
    #         self.requests+=1

    @task
    def local_query_url2(self):
        if self.requests==self.limit:
            self.environment.runner.quit()
        else:
            for i in range(len(self.local_query_no_search)):
                self.post_query(self.local_query_no_search[i]["name"], self.local_query_no_search[i]["query"], 
                    self.url2)
            for i in range(len(self.local_query_search)):
                self.post_query(self.local_query_search[i]["name"], self.local_query_search[i]["query"], 
                    self.url2)
            self.requests+=1