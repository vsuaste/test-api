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
        ]