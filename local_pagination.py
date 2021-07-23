def generate_queries():
    res = []
    cursor = {
        "book": "eyJib29rX2lkIjoibG9jYWxfYmtfMTA0NDk2IiwibmFtZSI6ImJvb2sxMDQ0OTYiLCJjb3VudHJ5X2lkcyI6WyJsb2NhbF9jdF8xMDQ0OTYiLCJsb2NhbF9jdF8xMDQ0OTciXSwicHVibGlzaGVyX2lkIjoibG9jYWxfcGJfNzQzMzk3In0=",
        "country": "eyJjb3VudHJ5X2lkIjoibG9jYWxfY3RfMTA0NDk2IiwibmFtZSI6ImNvdW50cnkxMDQ0OTYiLCJib29rX2lkcyI6WyJsb2NhbF9ia18xMDQ0OTYiLCJsb2NhbF9ia18xMDQ0OTUiXX0=",
        "capital": "eyJjYXBpdGFsX2lkIjoibG9jYWxfY3BfMTA0NDk2IiwibmFtZSI6ImNhcGl0YWxfMTA0NDk2IiwiY291bnRyeV9pZCI6ImxvY2FsX2N0XzEwNDQ5NiJ9",
        "publisher": "eyJwdWJsaXNoZXJfaWQiOiJsb2NhbF9wYl8xMDQ0OTYiLCJuYW1lIjoicHVibGlzaGVyXzEwNDQ5NiJ9",
    }
    for limit in [100, 1000, 5000, 9000]:
        res.extend([        
            {
                "name":f"local_booksConnection_pagination_{limit}", 
                "query":"""{{
                    local_booksConnection(pagination: {{first:{limit}, after:"{cursor}"}}){{
                        local_books{{
                            book_id
                            name
                        }}
                    }}
                }}""".format(limit=limit, cursor=cursor["book"])
            },
            {
                "name":f"local_countriesConnection_pagination_{limit}", 
                "query": """{{
                    local_countriesConnection(pagination: {{first:{limit}, after:"{cursor}"}}){{
                        local_countries{{
                            country_id
                            name
                        }}
                    }}
                }}""".format(limit=limit, cursor=cursor["country"])
            },
            {
                "name":f"local_capitalsConnection_pagination_{limit}", 
                "query": """{{
                    local_capitalsConnection(pagination: {{first:{limit}, after:"{cursor}"}}){{
                        local_capitals{{
                            capital_id
                            name
                        }}
                    }}
                }}""".format(limit=limit, cursor=cursor["capital"])
            },
            {
                "name":f"local_publishersConnection_pagination_{limit}", 
                "query":"""{{
                    local_publishersConnection(pagination: {{first:{limit}, after:"{cursor}"}}){{
                        local_publishers{{
                            publisher_id
                            name
                        }}
                    }}
                }}""".format(limit=limit, cursor=cursor["publisher"])
            }]
        )
    return res