module.exports = (instance) => {
    return [
      `query readOneBook{
          readOneBook(book_id:"${instance}_bk_12323"){
            book_id
            name
            country_ids
            publisher_id
          }
      }`,
      `query readOneCountry{
          readOneCountry(country_id:"${instance}_ct_123232"){
              country_id
              name
              book_ids
          }
      }`,
      `query readOneCapital{
          readOneCapital(capital_id:"${instance}_cp_12322"){
              capital_id
              country_id
              name
          }
      }`,
      `query readOnePublisher{
          readOnePublisher(publisher_id:"${instance}_pb_190322"){
              publisher_id
              name
          }
      }`,
      `query countBooks{
          countBooks
      }`,
      `query countCountries{
          countCountries
      }`,
      `query countCapitals{
          countCapitals
      }`,
      `query countPublishers{
          countPublishers
      }`,
      `query booksConnection {
          booksConnection(
          pagination: {first:100}){
              books{
                  book_id
              }
          }
      }`,
      `query countriesConnection{
          countriesConnection( 
            pagination: {first:100}){
              countries{
                  country_id
              }
          }
      }`,
      `query capitalsConnection{
          capitalsConnection(
            pagination: {first:100}){
              capitals{
                  capital_id
              }
          }
      }`,
      `query publishersConnection{
          publishersConnection( 
            pagination: {first:100}){
              publishers{
                  publisher_id
              }
          }
      }`,
    ];
  };