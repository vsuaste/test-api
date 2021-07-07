"use strict";

const fs = require("fs");
const path = require("path");
const LoadTesting = require("easygraphql-load-tester");
const { fileLoader, mergeTypes } = require("merge-graphql-schemas");
const queries = require("./query");

// const schema = fs.readFileSync(path.join(__dirname, 'schema.gql'), 'utf8')
// const queries = fileLoader(path.join(__dirname, './graphql'))

const schema_array = fileLoader(path.join(__dirname, "./schemas"));
const merged_schema = mergeTypes(schema_array);

const customQueries = queries("instance1");
// const customQueries = [`mutation UPDATE_BOOK
// {
//   updateBook(book_id:"instance2_a" name:"aa"){
//     book_id
//     name
//   }
// }
//   `]

const easyGraphQLLoadTester = new LoadTesting(merged_schema);

const testCases = easyGraphQLLoadTester.artillery({
  customQueries: customQueries,
  onlyCustomQueries: true,
  queryFile: true,
  withMutations: false,
});

module.exports = { testCases };
