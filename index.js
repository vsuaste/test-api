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

const queries_instance1 = queries("instance1");
const queries_instance2 = queries("instance2");


const easyGraphQLLoadTester = new LoadTesting(merged_schema);

const testInstance1 = easyGraphQLLoadTester.artillery({
  customQueries: queries_instance1,
  onlyCustomQueries: true,
  queryFile: true,
  withMutations: false,
});


const testInstance2 = easyGraphQLLoadTester.artillery({
  customQueries: queries_instance2,
  onlyCustomQueries: true,
  queryFile: true,
  withMutations: false,
});

module.exports = { testInstance1, testInstance2 };
