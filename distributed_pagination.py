def generate_queries(instance):
    cursor = {
        "instance1": {
        "book": "eyJib29rX2lkIjoiaW5zdGFuY2UxX2JrXzEwMDg5NiIsIm5hbWUiOiJib29rMTAwODk2IiwiY291bnRyeV9pZHMiOlsiaW5zdGFuY2UxX2N0XzEwMDg5NiIsImluc3RhbmNlMV9jdF8xMDA4OTciXSwicHVibGlzaGVyX2lkIjoiaW5zdGFuY2UxX3BiXzM5OTE0MCJ9",
        "country":
            "eyJjb3VudHJ5X2lkIjoiaW5zdGFuY2UxX2N0XzEwMDg5NiIsIm5hbWUiOiJjb3VudHJ5MTAwODk2IiwiYm9va19pZHMiOlsiaW5zdGFuY2UxX2JrXzEwMDg5NiIsImluc3RhbmNlMV9ia18xMDA4OTUiXX0=",
        "capital":
            "eyJjYXBpdGFsX2lkIjoiaW5zdGFuY2UxX2NwXzEwMDg5NiIsIm5hbWUiOiJjYXBpdGFsXzEwMDg5NiIsImNvdW50cnlfaWQiOiJpbnN0YW5jZTFfY3RfMTAwODk2In0=",
        "publisher":
            "eyJwdWJsaXNoZXJfaWQiOiJpbnN0YW5jZTFfcGJfMTAwODk2IiwibmFtZSI6InB1Ymxpc2hlcl8xMDA4OTYifQ==",
        },
        "instance2": {
        "book": "eyJib29rX2lkIjoiaW5zdGFuY2UyX2JrXzEwODk1IiwibmFtZSI6ImJvb2sxMDg5NSIsImNvdW50cnlfaWRzIjpbImluc3RhbmNlMl9jdF8xMDg5NSIsImluc3RhbmNlMl9jdF8xMDg5NiJdLCJwdWJsaXNoZXJfaWQiOiJpbnN0YW5jZTJfcGJfMTI1MDUifQ==",
        "country":
            "eyJjb3VudHJ5X2lkIjoiaW5zdGFuY2UyX2N0XzE4OTk4IiwibmFtZSI6ImNvdW50cnkxODk5OCIsImJvb2tfaWRzIjpbImluc3RhbmNlMl9ia18xODk5OCIsImluc3RhbmNlMl9ia18xODk5NyJdfQ==",
        "capital":
            "eyJjYXBpdGFsX2lkIjoiaW5zdGFuY2UyX2NwXzE4OTk4IiwibmFtZSI6ImNhcGl0YWxfMTg5OTgiLCJjb3VudHJ5X2lkIjoiaW5zdGFuY2UyX2N0XzE4OTk4In0=",
        "publisher":
            "eyJwdWJsaXNoZXJfaWQiOiJpbnN0YW5jZTJfcGJfMTA4OTciLCJuYW1lIjoicHVibGlzaGVyXzEwODk3In0=",
        },
    }
    res = []
    for limit in [100, 1000, 5000, 9000]:
        res.extend([        
            {
                "name":f"booksConnection_pagination_{limit}_{instance}", 
                "query":"""{{
                    booksConnection(pagination: {{first:{limit}, after:"{cursor}"}}){{
                        books{{
                            book_id
                            name
                        }}
                    }}
                }}""".format(limit=limit, cursor=cursor[instance]["book"])
            },
            {
                "name":f"countriesConnection_pagination_{limit}_{instance}", 
                "query": """{{
                    countriesConnection(pagination: {{first:{limit}, after:"{cursor}"}}){{
                        countries{{
                            country_id
                            name
                        }}
                    }}
                }}""".format(limit=limit, cursor=cursor[instance]["country"])
            },
            {
                "name":f"capitalsConnection_pagination_{limit}_{instance}", 
                "query": """{{
                    capitalsConnection(pagination: {{first:{limit}, after:"{cursor}"}}){{
                        capitals{{
                            capital_id
                            name
                        }}
                    }}
                }}""".format(limit=limit, cursor=cursor[instance]["capital"])
            },
            {
                "name":f"publishersConnection_pagination_{limit}_{instance}", 
                "query":"""{{
                    publishersConnection(pagination: {{first:{limit}, after:"{cursor}"}}){{
                        publishers{{
                            publisher_id
                            name
                        }}
                    }}
                }}""".format(limit=limit, cursor=cursor[instance]["publisher"])
            }]
        )
    return res