def generate_queries(instance):
    return [ 
        {
            "name":"readOneBook_{instance}".format(instance=instance), 
            "query":"""{{
                readOneBook(book_id:"{instance}_bk_12323"){{
                    book_id
                    name
                    country_ids
                    publisher_id
                    countriesConnection(pagination:{{first: 100 }}){{
                        countries{{
                            name 
                            country_id
                        }}
                    }}
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
                    available_booksConnection(pagination:{{first:100}}){{
                        books{{
                            book_id
                            name
                        }}
                    }}
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
                    country{{
                        country_id
                        name
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"readOnePublisher_{instance}".format(instance=instance), 
            "query":"""{{
                readOnePublisher(publisher_id:"{instance}_pb_190322"){{
                    publisher_id
                    name
                    booksConnection(pagination:{{first: 100}}){{
                        books{{
                            book_id
                            name
                        }}
                    }}
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"readOneBook_{instance}_count".format(instance=instance), 
            "query":"""{{
                readOneBook(book_id:"{instance}_bk_12323"){{
                    book_id
                    name
                    country_ids
                    publisher_id
                    countFilteredCountries
                }}
            }}""".format(instance=instance)
        },
        { 
            "name":"readOneCountry_{instance}_count".format(instance=instance), 
            "query":"""{{
                readOneCountry(country_id:"{instance}_ct_123232"){{
                    country_id
                    name
                    book_ids
                    countFilteredAvailable_books
                }}
            }}""".format(instance=instance)
        },
        {
            "name":"readOnePublisher_{instance}_count".format(instance=instance), 
            "query":"""{{
                readOnePublisher(publisher_id:"{instance}_pb_190322"){{
                    publisher_id
                    name
                    countFilteredBooks
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
            "name":"countCountry_{instance}".format(instance=instance), 
            "query":"""{{
                countCountries(search:{{field:country_id operator:like value:"{instance}%"}})
            }}""".format(instance=instance)
        },
        { 
            "name":"countCapital_{instance}".format(instance=instance), 
            "query":"""{{
                countCapitals(search:{{field:capital_id operator:like value:"{instance}%"}})
            }}""".format(instance=instance)
        },
        {
            "name":"countPublisher_{instance}".format(instance=instance), 
            "query":"""{{
                countPublishers(search:{{field:publisher_id operator:like value:"{instance}%"}})
            }}""".format(instance=instance)
        }



    ]