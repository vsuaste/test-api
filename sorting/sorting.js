
(async () => {
  const { Client } = require("pg");
  const {writeFile} = require("fs/promises") 
  const client = new Client({
    user: "zendro",
    host: "localhost",
    database: "zendro_development",
    password: "zendro",
    port: 1234,
  });
  await client.connect();

  const id = {
    "local_books":"book_id", 
    "local_capitals":"capital_id", 
    "local_countries": "country_id", 
    "local_publishers": "publisher_id"
  }
  for (let modelName of ["local_books", "local_capitals", "local_countries", "local_publishers"]){
    for (let limit of [100, 1000, 5000, 9000]){
      let row = [`${modelName}_${limit}_no_sort`]
      console.log(row)
      for (let i of Array(100).keys()){
        let res = await client.query(`EXPLAIN (ANALYZE, TIMING TRUE, COSTS FALSE) 
          SELECT * FROM ${modelName} LIMIT ${limit}`);
        res = res.rows[3]["QUERY PLAN"]
        res = res.slice(res.indexOf(":")+2, res.indexOf("ms")-1)
        row.push(res)
      }
      await writeFile(`no_sort.csv`, row.join()+"\n", { flag: 'a' });
    }
  }
  console.log(`############finish no_sort.csv###########`)

  for (let modelName of ["local_books", "local_capitals", "local_countries", "local_publishers"]){
    for (let limit of [100, 1000, 5000, 9000]){
      let row = [`${modelName}_${limit}_id`]
      console.log(row)
      for (let i of Array(100).keys()){
        let res = await client.query(`EXPLAIN (ANALYZE, TIMING TRUE, COSTS FALSE) 
          SELECT * FROM ${modelName} 
          ORDER BY ${id[modelName]} ASC 
          LIMIT ${limit}`);
        res = res.rows[3]["QUERY PLAN"]
        res = res.slice(res.indexOf(":")+2, res.indexOf("ms")-1)
        row.push(res)
      }
      await writeFile(`sort_by_id.csv`, row.join()+"\n", { flag: 'a' });
    }
  }
  console.log(`##############finish sort_by_id.csv###############`)

  for (let modelName of ["local_books", "local_capitals", "local_countries", "local_publishers"]){
    for (let limit of [100, 1000, 5000, 9000]){
      let row = [`${modelName}_${limit}_name`]
      console.log(row)
      for (let i of Array(100).keys()){
        let res = await client.query(`EXPLAIN (ANALYZE, TIMING TRUE, COSTS FALSE) 
          SELECT * FROM ${modelName} 
          ORDER BY name ASC 
          LIMIT ${limit}`);
        res = res.rows[11]["QUERY PLAN"]
        res = res.slice(res.indexOf(":")+2, res.indexOf("ms")-1)
        row.push(res)
      }
      await writeFile(`sort_by_name.csv`, row.join()+"\n", { flag: 'a' });
    }
    
  }
  console.log(`#############finish sort_by_name.csv##############`)


  await client.end();
})();
