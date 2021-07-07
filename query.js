module.exports = (instance) => {
  return [
    `query readOneBook{
        readOneBook(book_id:"${instance}_bk_12323"){
          book_id
          name
          country_ids
          publisher_id
          publisher(search: null){
            name
          }
          countriesConnection(pagination: {first:2}){
            countries{
                name
            }
          }
          countFilteredCountries(search: null)
        }
    }`,
    `query readOneCountry{
        readOneCountry(country_id:"${instance}_ct_123232"){
            country_id
            name
            book_ids
            capital(search: null){
                name
            }
            available_booksConnection(pagination: {first:2}){
                books{
                    name
                }
            }
            countFilteredAvailable_books(search: null)
        }
    }`,
    `query readOneCapital{
        readOneCapital(capital_id:"${instance}_cp_12322"){
            capital_id
            country_id
            name
            country(search: null){
                name
            }
        }
    }`,
    `query readOnePublisher{
        readOnePublisher(publisher_id:"${instance}_pb_190322"){
            publisher_id
            name
            booksConnection(pagination: {first:2}){
                books{
                    name
                }
            }
            countFilteredBooks(search: null)
        }
    }`,
    `query countBooks{
        countBooks(search:{field:book_id operator:like value:"${instance}%"})
    }`,
    `query countCountries{
        countCountries(search:{field:country_id operator:like value:"${instance}%"})
    }`,
    `query countCapitals{
        countCapitals(search:{field:capital_id operator:like value:"${instance}%"})
    }`,
    `query countPublishers{
        countPublishers(search:{field:publisher_id operator:like value:"${instance}%"})
    }`,
    `query booksConnection {
        booksConnection(search:{field:book_id operator:like value:"${instance}%"}, 
        pagination: {first:25}){
            books{
                book_id
            }
            edges {
                cursor
                node {
                    name
                }
            }
            pageInfo{
                startCursor
                endCursor
                hasPreviousPage
                hasNextPage
            }
        }
    }`,
    `query countriesConnection{
        countriesConnection(search:{field:country_id operator:like value:"${instance}%"}, 
          pagination: {first:25}){
            countries{
                country_id
            }
            edges {
                cursor
                node {
                    name
                }
            }
            pageInfo{
                startCursor
                endCursor
                hasPreviousPage
                hasNextPage
            }
        }
    }`,
    `query capitalsConnection{
        capitalsConnection(search:{field:capital_id operator:like value:"${instance}%"}, 
          pagination: {first:25}){
            capitals{
                capital_id
            }
            edges {
                cursor
                node {
                    name
                }
            }
            pageInfo{
                startCursor
                endCursor
                hasPreviousPage
                hasNextPage
            }
        }
    }`,
    `query publishersConnection{
        publishersConnection(search:{field:publisher_id operator:like value:"${instance}%"}, 
          pagination: {first:25}){
            publishers{
                publisher_id
            }
            edges {
                cursor
                node {
                    name
                }
            }
            pageInfo{
                startCursor
                endCursor
                hasPreviousPage
                hasNextPage
            }
        }
    }`,
  ];
};
