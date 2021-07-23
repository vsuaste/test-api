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
        ]