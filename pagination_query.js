module.exports = (instance) => {
  //   instance1_bk_100896 instance1_ct_100896 instance1_cp_100896 instance1_pb_100896
  //   instance2_bk_10895  instance2_ct_18998  instance2_cp_18998  instance2_pb_10897
  const cursor = {
    instance1: {
      book: "eyJib29rX2lkIjoiaW5zdGFuY2UxX2JrXzEwMDg5NiIsIm5hbWUiOiJib29rMTAwODk2IiwiY291bnRyeV9pZHMiOlsiaW5zdGFuY2UxX2N0XzEwMDg5NiIsImluc3RhbmNlMV9jdF8xMDA4OTciXSwicHVibGlzaGVyX2lkIjoiaW5zdGFuY2UxX3BiXzM5OTE0MCJ9",
      country:
        "eyJjb3VudHJ5X2lkIjoiaW5zdGFuY2UxX2N0XzEwMDg5NiIsIm5hbWUiOiJjb3VudHJ5MTAwODk2IiwiYm9va19pZHMiOlsiaW5zdGFuY2UxX2JrXzEwMDg5NiIsImluc3RhbmNlMV9ia18xMDA4OTUiXX0=",
      capital:
        "eyJjYXBpdGFsX2lkIjoiaW5zdGFuY2UxX2NwXzEwMDg5NiIsIm5hbWUiOiJjYXBpdGFsXzEwMDg5NiIsImNvdW50cnlfaWQiOiJpbnN0YW5jZTFfY3RfMTAwODk2In0=",
      publisher:
        "eyJwdWJsaXNoZXJfaWQiOiJpbnN0YW5jZTFfcGJfMTAwODk2IiwibmFtZSI6InB1Ymxpc2hlcl8xMDA4OTYifQ==",
    },
    instance2: {
      book: "eyJib29rX2lkIjoiaW5zdGFuY2UyX2JrXzEwODk1IiwibmFtZSI6ImJvb2sxMDg5NSIsImNvdW50cnlfaWRzIjpbImluc3RhbmNlMl9jdF8xMDg5NSIsImluc3RhbmNlMl9jdF8xMDg5NiJdLCJwdWJsaXNoZXJfaWQiOiJpbnN0YW5jZTJfcGJfMTI1MDUifQ==",
      country:
        "eyJjb3VudHJ5X2lkIjoiaW5zdGFuY2UyX2N0XzE4OTk4IiwibmFtZSI6ImNvdW50cnkxODk5OCIsImJvb2tfaWRzIjpbImluc3RhbmNlMl9ia18xODk5OCIsImluc3RhbmNlMl9ia18xODk5NyJdfQ==",
      capital:
        "eyJjYXBpdGFsX2lkIjoiaW5zdGFuY2UyX2NwXzE4OTk4IiwibmFtZSI6ImNhcGl0YWxfMTg5OTgiLCJjb3VudHJ5X2lkIjoiaW5zdGFuY2UyX2N0XzE4OTk4In0=",
      publisher:
        "eyJwdWJsaXNoZXJfaWQiOiJpbnN0YW5jZTJfcGJfMTA4OTciLCJuYW1lIjoicHVibGlzaGVyXzEwODk3In0=",
    },
  };

  return [
    `query booksConnection_pagination {
          booksConnection(search:{field:book_id operator:like value:"${instance}%"},
          pagination: {first:100, after:"${cursor[instance]["book"]}"}){
              books{
                  book_id
              }
          }
      }`,
    `query countriesConnection_pagination{
          countriesConnection(search:{field:country_id operator:like value:"${instance}%"}, 
            pagination: {first:100, after:"${cursor[instance]["country"]}"}){
              countries{
                  country_id
              }
          }
      }`,
    `query capitalsConnection_pagination{
          capitalsConnection(search:{field:capital_id operator:like value:"${instance}%"}, 
            pagination: {first:100, after:"${cursor[instance]["capital"]}"}){
              capitals{
                  capital_id
              }
          }
      }`,
    `query publishersConnection_pagination{
          publishersConnection(search:{field:publisher_id operator:like value:"${instance}%"}, 
            pagination: {first:100, after:"${cursor[instance]["publisher"]}"}){
              publishers{
                  publisher_id
              }
          }
      }`,
    `query booksConnection_pagination_association {
        booksConnection(search:{field:book_id operator:like value:"${instance}%"}, 
        pagination: {first:25, after:"${cursor[instance]["book"]}"}){
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
    `query countriesConnection_pagination_association{
        countriesConnection(search:{field:country_id operator:like value:"${instance}%"}, 
          pagination: {first:25, after:"${cursor[instance]["country"]}"}){
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
    `query capitalsConnection_pagination_association{
        capitalsConnection(search:{field:capital_id operator:like value:"${instance}%"}, 
          pagination: {first:25, after:"${cursor[instance]["capital"]}"}){
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
    `query publishersConnection_pagination_association{
        publishersConnection(search:{field:publisher_id operator:like value:"${instance}%"}, 
          pagination: {first:25, after:"${cursor[instance]["capital"]}"}){
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
