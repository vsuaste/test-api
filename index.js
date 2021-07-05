'use strict'

const fs = require('fs')
const path = require('path')
const LoadTesting = require('easygraphql-load-tester')
const { fileLoader, mergeTypes} = require('merge-graphql-schemas')

// const schema = fs.readFileSync(path.join(__dirname, 'schema.gql'), 'utf8')
// const queries = fileLoader(path.join(__dirname, './graphql'))

const schema_array = fileLoader(path.join(__dirname, './schemas'))
const merged_schema = mergeTypes(schema_array)


// console.log(merged_schema);

// const args = {
//   SEARCH_USER: [
//     {
//       name: 'bar',
//     },
//     {
//       name: 'foo',
//     },
//   ],
// }

const customQueries = [`
{
  booksConnection(pagination:{first:50}){
    books{
      name
      book_id
    }
  }
}
  `]

const easyGraphQLLoadTester = new LoadTesting(merged_schema)

const testCases = easyGraphQLLoadTester.artillery({
  customQueries,
  onlyCustomQueries: true,
  queryFile: true,
  withMutations: false
})

module.exports = { testCases }