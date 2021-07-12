from locust import HttpUser, task
import query, stress_query

class ZendroStressTest(HttpUser):
    requests = 0
    limit = 40
    url1 = "http://graphql.zendro-dev.org/graphql"
    url2 = "http://siagro01.conabio.gob.mx:3003/graphql"

    queries_instance1 = query.generate_queries("instance1")
    queries_instance2 = query.generate_queries("instance2")

    stress_queries_instance1 = stress_query.generate_queries("instance1")
    stress_queries_instance2 = stress_query.generate_queries("instance2")


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

    @task
    def stress_test_url1(self):
        if self.requests==self.limit:
            self.environment.runner.quit()
        else:
            for i in range(len(self.stress_queries_instance1)):
                self.post_query(self.stress_queries_instance1[i]["name"], self.stress_queries_instance1[i]["query"], 
                    self.url1)
            for i in range(len(self.stress_queries_instance2)):
                self.post_query(self.stress_queries_instance2[i]["name"], self.stress_queries_instance2[i]["query"], 
                    self.url1)
            self.requests+=1