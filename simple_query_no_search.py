def generate_queries():
    return [ 
        {
            "name":"booksConnection_100", 
            "query":"""{
                booksConnection(pagination: {first: 100}){
                    books{
                        book_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"countriesConnection_100", 
            "query": """{
                countriesConnection(pagination: {first:100}){
                    countries{
                        country_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"capitalsConnection_100", 
            "query": """{
                capitalsConnection(pagination: {first:100}){
                    capitals{
                        capital_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"publishersConnection_100", 
            "query":"""{
                publishersConnection(pagination: {first:100}){
                    publishers{
                        publisher_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"booksConnection_1000", 
            "query":"""{
                booksConnection(pagination: {first: 1000}){
                    books{
                        book_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"countriesConnection_1000", 
            "query": """{
                countriesConnection(pagination: {first:1000}){
                    countries{
                        country_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"capitalsConnection_1000", 
            "query": """{
                capitalsConnection(pagination: {first:1000}){
                    capitals{
                        capital_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"publishersConnection_1000", 
            "query":"""{
                publishersConnection(pagination: {first:1000}){
                    publishers{
                        publisher_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"booksConnection_5000", 
            "query":"""{
                booksConnection(pagination: {first: 5000}){
                    books{
                        book_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"countriesConnection_5000", 
            "query": """{
                countriesConnection(pagination: {first:5000}){
                    countries{
                        country_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"capitalsConnection_5000", 
            "query": """{
                capitalsConnection(pagination: {first:5000}){
                    capitals{
                        capital_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"publishersConnection_5000", 
            "query":"""{
                publishersConnection(pagination: {first:5000}){
                    publishers{
                        publisher_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"booksConnection_9000", 
            "query":"""{
                booksConnection(pagination: {first: 9000}){
                    books{
                        book_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"countriesConnection_9000", 
            "query": """{
                countriesConnection(pagination: {first:9000}){
                    countries{
                        country_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"capitalsConnection_9000", 
            "query": """{
                capitalsConnection(pagination: {first:9000}){
                    capitals{
                        capital_id
                        name
                    }
                }
            }"""
        },
        {
            "name":"publishersConnection_9000", 
            "query":"""{
                publishersConnection(pagination: {first:9000}){
                    publishers{
                        publisher_id
                        name
                    }
                }
            }"""
        }
        ]