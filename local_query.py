def generate_queries(instance):
    if instance == "simple":
        return [
            {
                "name":"local_booksConnection_100", 
                "query":"""{{
                    local_booksConnection(pagination: {{first: 100}}){{
                        books{{
                            book_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_countriesConnection_100", 
                "query": """{{
                    local_countriesConnection(pagination: {{first:100}}){{
                        countries{{
                            country_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_capitalsConnection_100", 
                "query": """{{
                    local_capitalsConnection(pagination: {{first:100}}){{
                        capitals{{
                            capital_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_publishersConnection_100", 
                "query":"""{{
                    local_publishersConnection(pagination: {{first:100}}){{
                        publishers{{
                            publisher_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_booksConnection_1000", 
                "query":"""{{
                    local_booksConnection(pagination: {{first: 1000}}){{
                        books{{
                            book_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_countriesConnection_1000", 
                "query": """{{
                    local_countriesConnection(pagination: {{first:1000}}){{
                        countries{{
                            country_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_capitalsConnection_1000", 
                "query": """{{
                    local_capitalsConnection(pagination: {{first:1000}}){{
                        capitals{{
                            capital_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_publishersConnection_1000", 
                "query":"""{{
                    local_publishersConnection(pagination: {{first:1000}}){{
                        publishers{{
                            publisher_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_booksConnection_5000", 
                "query":"""{{
                    local_booksConnection(pagination: {{first: 5000}}){{
                        books{{
                            book_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_countriesConnection_5000", 
                "query": """{{
                    local_countriesConnection(pagination: {{first:5000}}){{
                        countries{{
                            country_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_capitalsConnection_5000", 
                "query": """{{
                    local_capitalsConnection(pagination: {{first:5000}}){{
                        capitals{{
                            capital_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_publishersConnection_5000", 
                "query":"""{{
                    local_publishersConnection(pagination: {{first:5000}}){{
                        publishers{{
                            publisher_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_booksConnection_9000", 
                "query":"""{{
                    local_booksConnection(pagination: {{first: 9000}}){{
                        books{{
                            book_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_countriesConnection_9000", 
                "query": """{{
                    local_countriesConnection(pagination: {{first:9000}}){{
                        countries{{
                            country_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_capitalsConnection_9000", 
                "query": """{{
                    local_capitalsConnection(pagination: {{first:9000}}){{
                        capitals{{
                            capital_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_publishersConnection_9000", 
                "query":"""{{
                    local_publishersConnection(pagination: {{first:9000}}){{
                        publishers{{
                            publisher_id
                            name
                        }}
                    }}
                }}"""
            }
            ]
    else:
        return [
            {
                "name":"local_booksConnection_search_100", 
                "query":"""{{
                    local_booksConnection(search:{{field:book_id operator:like value:"local_bk_%"}}, 
                    pagination: {{first: 100}}){{
                        books{{
                            book_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_countriesConnection_search_100", 
                "query": """{{
                    local_countriesConnection(search:{{field:country_id operator:like value:"local_ct_%"}}, 
                    pagination: {{first:100}}){{
                        countries{{
                            country_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_capitalsConnection_search_100", 
                "query": """{{
                    local_capitalsConnection(search:{{field:capital_id operator:like value:"local_cp_%"}}, 
                    pagination: {{first:100}}){{
                        capitals{{
                            capital_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_publishersConnection_search_100", 
                "query":"""{{
                    local_publishersConnection(search:{{field:publisher_id operator:like value:"local_pb_%"}}, 
                    pagination: {{first:100}}){{
                        publishers{{
                            publisher_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_booksConnection_search_1000", 
                "query":"""{{
                    local_booksConnection(search:{{field:book_id operator:like value:"local_bk_%"}}, 
                    pagination: {{first: 1000}}){{
                        books{{
                            book_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_countriesConnection_search_1000", 
                "query": """{{
                    local_countriesConnection(search:{{field:country_id operator:like value:"local_ct_%"}}, 
                    pagination: {{first:1000}}){{
                        countries{{
                            country_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_capitalsConnection_search_1000", 
                "query": """{{
                    local_capitalsConnection(search:{{field:capital_id operator:like value:"local_cp_%"}}, 
                    pagination: {{first:1000}}){{
                        capitals{{
                            capital_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_publishersConnection_search_1000", 
                "query":"""{{
                    local_publishersConnection(search:{{field:publisher_id operator:like value:"local_pb_%"}}, 
                    pagination: {{first:1000}}){{
                        publishers{{
                            publisher_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_booksConnection_search_5000", 
                "query":"""{{
                    local_booksConnection(search:{{field:book_id operator:like value:"local_bk_%"}}, 
                    pagination: {{first: 5000}}){{
                        books{{
                            book_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_countriesConnection_search_5000", 
                "query": """{{
                    local_countriesConnection(search:{{field:country_id operator:like value:"local_ct_%"}}, 
                    pagination: {{first:5000}}){{
                        countries{{
                            country_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_capitalsConnection_search_5000", 
                "query": """{{
                    local_capitalsConnection(search:{{field:capital_id operator:like value:"local_cp_%"}}, 
                    pagination: {{first:5000}}){{
                        capitals{{
                            capital_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_publishersConnection_search_5000", 
                "query":"""{{
                    local_publishersConnection(search:{{field:publisher_id operator:like value:"local_pb_%"}}, 
                    pagination: {{first:5000}}){{
                        publishers{{
                            publisher_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_booksConnection_search_9000", 
                "query":"""{{
                    local_booksConnection(search:{{field:book_id operator:like value:"local_bk_%"}}, 
                    pagination: {{first: 9000}}){{
                        books{{
                            book_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_countriesConnection_search_9000", 
                "query": """{{
                    local_countriesConnection(search:{{field:country_id operator:like value:"local_ct_%"}}, 
                    pagination: {{first:9000}}){{
                        countries{{
                            country_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_capitalsConnection_search_9000", 
                "query": """{{
                    local_capitalsConnection(search:{{field:capital_id operator:like value:"local_cp_%"}}, 
                    pagination: {{first:9000}}){{
                        capitals{{
                            capital_id
                            name
                        }}
                    }}
                }}"""
            },
            {
                "name":"local_publishersConnection_search_9000", 
                "query":"""{{
                    local_publishersConnection(search:{{field:publisher_id operator:like value:"local_pb_%"}}, 
                    pagination: {{first:9000}}){{
                        publishers{{
                            publisher_id
                            name
                        }}
                    }}
                }}"""
            }
        ]