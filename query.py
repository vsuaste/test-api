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
    return [ 
        {
            "name":"readOneBook_{instance}".format(instance=instance), 
            "query":"""{{
                readOneBook(book_id:"{instance}_bk_12323"){{
                    book_id
                    name
                    country_ids
                    publisher_id
                }}
            }}""".format(instance=instance)
        },
        { 
            "name":"readOneCountry_{instance}".format(instance=instance), 
            "query":"""{{
                readOneCountry(country_id:"{instance}_ct_123232"){{
                    country_id
                    name
                    book_ids
                }}
            }}""".format(instance=instance)
        },
        { 
            "name":"readOneCapital_{instance}".format(instance=instance), 
            "query":"""{{
                readOneCapital(capital_id:"{instance}_cp_12322"){{
                    capital_id
                    country_id
                    name
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"readOnePublisher_{instance}".format(instance=instance), 
            "query":"""{{
                readOnePublisher(publisher_id:"{instance}_pb_190322"){{
                    publisher_id
                    name
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"countBooks_{instance}".format(instance=instance), 
            "query":"""{{
                countBooks(search:{{field:book_id operator:like value:"{instance}%"}})
            }}""".format(instance=instance)
        },
        {
            "name":"countCountries_{instance}".format(instance=instance), 
            "query":"""query {{
                countCountries(search:{{field:country_id operator:like value:"{instance}%"}})
            }}""".format(instance=instance)
        },
        {
            "name":"countCapitals_{instance}".format(instance=instance), 
            "query":"""{{
                countCapitals(search:{{field:capital_id operator:like value:"{instance}%"}})
            }}""".format(instance=instance)
        },
        {
            "name":"countPublishers_{instance}".format(instance=instance), 
            "query":"""{{
                countPublishers(search:{{field:publisher_id operator:like value:"{instance}%"}})
            }}""".format(instance=instance)
        },
        {
            "name":"booksConnection_{instance}".format(instance=instance), 
            "query":"""{{
                booksConnection(search:{{field:book_id operator:like value:"{instance}%"}}, 
                pagination: {{first:25}}){{
                    books{{
                        book_id
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"countriesConnection_{instance}".format(instance=instance), 
            "query": """{{
                countriesConnection(search:{{field:country_id operator:like value:"{instance}%"}}, 
                pagination: {{first:25}}){{
                    countries{{
                        country_id
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"capitalsConnection_{instance}".format(instance=instance), 
            "query": """{{
                capitalsConnection(search:{{field:capital_id operator:like value:"{instance}%"}}, 
                pagination: {{first:25}}){{
                    capitals{{
                        capital_id
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"publishersConnection_{instance}".format(instance=instance), 
            "query":"""{{
                publishersConnection(search:{{field:publisher_id operator:like value:"{instance}%"}}, 
                pagination: {{first:25}}){{
                    publishers{{
                        publisher_id
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"readOneBook_association_{instance}".format(instance=instance), 
            "query":"""{{
                readOneBook(book_id:"{instance}_bk_12323"){{
                book_id
                name
                country_ids
                publisher_id
                publisher(search: null){{
                    name
                }}
                countriesConnection(pagination: {{first:2}}){{
                    countries{{
                        name
                    }}
                }}
                countFilteredCountries(search: null)
                }}
            }}""".format(instance=instance)
        },
        { 
            "name":"readOneCountry_association_{instance}".format(instance=instance), 
            "query":"""{{
                readOneCountry(country_id:"{instance}_ct_123232"){{
                country_id
                name
                book_ids
                capital(search: null){{
                    name
                }}
                available_booksConnection(pagination: {{first:2}}){{
                    books{{
                        name
                    }}
                }}
                countFilteredAvailable_books(search: null)
                }}
            }}""".format(instance=instance)
        },
        { 
            "name":"readOneCapital_association_{instance}".format(instance=instance), 
            "query":"""{{
                readOneCapital(capital_id:"{instance}_cp_12322"){{
                    capital_id
                    country_id
                    name
                    country(search: null){{
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"readOnePublisher_association_{instance}".format(instance=instance), 
            "query":"""{{
                readOnePublisher(publisher_id:"{instance}_pb_190322"){{
                    publisher_id
                    name
                    booksConnection(pagination: {{first:2}}){{
                        books{{
                            name
                        }}
                    }}
                    countFilteredBooks(search: null)
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"booksConnection_edge_pageInfo_{instance}".format(instance=instance), 
            "query":"""{{
                booksConnection(search:{{field:book_id operator:like value:"{instance}%"}}, 
                pagination: {{first:25}}){{
                    books{{
                        book_id
                    }}
                    edges {{
                        cursor
                        node {{
                            name
                        }}
                    }}
                    pageInfo{{
                        startCursor
                        endCursor
                        hasPreviousPage
                        hasNextPage
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"countriesConnection_edge_pageInfo_{instance}".format(instance=instance), 
            "query": """{{
                countriesConnection(search:{{field:country_id operator:like value:"{instance}%"}}, 
                pagination: {{first:25}}){{
                    countries{{
                        country_id
                    }}
                    edges {{
                        cursor
                        node {{
                            name
                        }}
                    }}
                    pageInfo{{
                        startCursor
                        endCursor
                        hasPreviousPage
                        hasNextPage
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"capitalsConnection_edge_pageInfo_{instance}".format(instance=instance), 
            "query": """{{
                capitalsConnection(search:{{field:capital_id operator:like value:"{instance}%"}}, 
                pagination: {{first:25}}){{
                    capitals{{
                        capital_id
                    }}
                    edges {{
                        cursor
                        node {{
                            name
                        }}
                    }}
                    pageInfo{{
                        startCursor
                        endCursor
                        hasPreviousPage
                        hasNextPage
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"publishersConnection_edge_pageInfo_{instance}".format(instance=instance), 
            "query":"""{{
                publishersConnection(search:{{field:publisher_id operator:like value:"{instance}%"}}, 
                pagination: {{first:25}}){{
                    publishers{{
                        publisher_id
                    }}
                    edges {{
                        cursor
                        node {{
                            name
                        }}
                    }}
                    pageInfo{{
                        startCursor
                        endCursor
                        hasPreviousPage
                        hasNextPage
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"booksConnection_pagination_{instance}".format(instance=instance), 
            "query":"""{{
                booksConnection(search:{{field:book_id operator:like value:"{instance}%"}}, 
                pagination: {{first:25, after:"{cursor}"}}){{
                    books{{
                        book_id
                    }}
                    edges {{
                        cursor
                        node {{
                            name
                        }}
                    }}
                    pageInfo{{
                        startCursor
                        endCursor
                        hasPreviousPage
                        hasNextPage
                    }}
                }}
            }}""".format(instance=instance, cursor=cursor[instance]["book"])
        },
        {
            "name":"countriesConnection_pagination_{instance}".format(instance=instance), 
            "query": """{{
                countriesConnection(search:{{field:country_id operator:like value:"{instance}%"}}, 
                pagination: {{first:25, after:"{cursor}"}}){{
                    countries{{
                        country_id
                    }}
                    edges {{
                        cursor
                        node {{
                            name
                        }}
                    }}
                    pageInfo{{
                        startCursor
                        endCursor
                        hasPreviousPage
                        hasNextPage
                    }}
                }}
            }}""".format(instance=instance, cursor=cursor[instance]["country"])
        },
        {
            "name":"capitalsConnection_pagination_{instance}".format(instance=instance), 
            "query": """{{
                capitalsConnection(search:{{field:capital_id operator:like value:"{instance}%"}}, 
                pagination: {{first:25, after:"{cursor}"}}){{
                    capitals{{
                        capital_id
                    }}
                    edges {{
                        cursor
                        node {{
                            name
                        }}
                    }}
                    pageInfo{{
                        startCursor
                        endCursor
                        hasPreviousPage
                        hasNextPage
                    }}
                }}
            }}""".format(instance=instance, cursor=cursor[instance]["capital"])
        },
        {
            "name":"publishersConnection_pagination_{instance}".format(instance=instance), 
            "query":"""{{
                publishersConnection(search:{{field:publisher_id operator:like value:"{instance}%"}}, 
                pagination: {{first:25, after:"{cursor}"}}){{
                    publishers{{
                        publisher_id
                    }}
                    edges {{
                        cursor
                        node {{
                            name
                        }}
                    }}
                    pageInfo{{
                        startCursor
                        endCursor
                        hasPreviousPage
                        hasNextPage
                    }}
                }}
            }}""".format(instance=instance, cursor=cursor[instance]["publisher"])
        },
        ]