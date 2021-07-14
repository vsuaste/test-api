const { Client } = require("pg");

(async () => {
  const client = new Client({
    user: "zendro",
    host: "localhost",
    database: "zendro_development",
    password: "zendro",
    port: 1234,
  });
  await client.connect();

  const res = await client.query(
    "EXPLAIN (ANALYZE, TIMING TRUE, COSTS FALSE) SELECT * FROM books LIMIT 100000"
  );
  console.log(res.rows[3]["QUERY PLAN"]);
  await client.end();
})();
