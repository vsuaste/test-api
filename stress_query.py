def generate_queries(instance):
    return [ 
        {
            "name":"booksConnection_{instance}".format(instance=instance), 
            "query":"""{{
                booksConnection(search:{{field:book_id operator:like value:"{instance}%"}}, 
                pagination: {{first: 100}}){{
                    books{{
                        book_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"countriesConnection_{instance}".format(instance=instance), 
            "query": """{{
                countriesConnection(search:{{field:country_id operator:like value:"{instance}%"}}, 
                pagination: {{first:100}}){{
                    countries{{
                        country_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"capitalsConnection_{instance}".format(instance=instance), 
            "query": """{{
                capitalsConnection(search:{{field:capital_id operator:like value:"{instance}%"}}, 
                pagination: {{first:100}}){{
                    capitals{{
                        capital_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"publishersConnection_{instance}".format(instance=instance), 
            "query":"""{{
                publishersConnection(search:{{field:publisher_id operator:like value:"{instance}%"}}, 
                pagination: {{first:100}}){{
                    publishers{{
                        publisher_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"booksConnection_{instance}_1000".format(instance=instance), 
            "query":"""{{
                booksConnection(search:{{field:book_id operator:like value:"{instance}%"}}, 
                pagination: {{first: 1000}}){{
                    books{{
                        book_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"countriesConnection_{instance}_1000".format(instance=instance), 
            "query": """{{
                countriesConnection(search:{{field:country_id operator:like value:"{instance}%"}}, 
                pagination: {{first:1000}}){{
                    countries{{
                        country_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"capitalsConnection_{instance}_1000".format(instance=instance), 
            "query": """{{
                capitalsConnection(search:{{field:capital_id operator:like value:"{instance}%"}}, 
                pagination: {{first:1000}}){{
                    capitals{{
                        capital_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"publishersConnection_{instance}_1000".format(instance=instance), 
            "query":"""{{
                publishersConnection(search:{{field:publisher_id operator:like value:"{instance}%"}}, 
                pagination: {{first:1000}}){{
                    publishers{{
                        publisher_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"booksConnection_{instance}_5000".format(instance=instance), 
            "query":"""{{
                booksConnection(search:{{field:book_id operator:like value:"{instance}%"}}, 
                pagination: {{first: 5000}}){{
                    books{{
                        book_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"countriesConnection_{instance}_5000".format(instance=instance), 
            "query": """{{
                countriesConnection(search:{{field:country_id operator:like value:"{instance}%"}}, 
                pagination: {{first:5000}}){{
                    countries{{
                        country_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"capitalsConnection_{instance}_5000".format(instance=instance), 
            "query": """{{
                capitalsConnection(search:{{field:capital_id operator:like value:"{instance}%"}}, 
                pagination: {{first:5000}}){{
                    capitals{{
                        capital_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"publishersConnection_{instance}_5000".format(instance=instance), 
            "query":"""{{
                publishersConnection(search:{{field:publisher_id operator:like value:"{instance}%"}}, 
                pagination: {{first:5000}}){{
                    publishers{{
                        publisher_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"booksConnection_{instance}_9000".format(instance=instance), 
            "query":"""{{
                booksConnection(search:{{field:book_id operator:like value:"{instance}%"}}, 
                pagination: {{first: 9000}}){{
                    books{{
                        book_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"countriesConnection_{instance}_9000".format(instance=instance), 
            "query": """{{
                countriesConnection(search:{{field:country_id operator:like value:"{instance}%"}}, 
                pagination: {{first:9000}}){{
                    countries{{
                        country_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"capitalsConnection_{instance}_9000".format(instance=instance), 
            "query": """{{
                capitalsConnection(search:{{field:capital_id operator:like value:"{instance}%"}}, 
                pagination: {{first:9000}}){{
                    capitals{{
                        capital_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"publishersConnection_{instance}_9000".format(instance=instance), 
            "query":"""{{
                publishersConnection(search:{{field:publisher_id operator:like value:"{instance}%"}}, 
                pagination: {{first:9000}}){{
                    publishers{{
                        publisher_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        }
        ]