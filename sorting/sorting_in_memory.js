const _ = require("lodash");
const records = require("./records")


const {performance} = require('perf_hooks');
const orderRecords = (
    matchingRecords,
    order = [{ field, order }]
  ) => {
    return _.orderBy(
      matchingRecords,
      _.map(order, "field"),
      _.map(order, "order").map((orderArg) => orderArg.toLowerCase())
    );
   
  };
(async () => {
    const {writeFile} = require("fs/promises") 
    const order = [{field: "book_id", order: 'ASC'}];
    for (let num of [100, 1000, 5000, 9000]){
      let row = [`sort_book_${num}_1_2`]      

      for (let i of Array(100).keys()){
        const nodes = records["books_instance1_4500"].slice(0, num/2)
            .concat(records["books_instance2_4500"].slice(0, num/2))
        const start = performance.now();
        const res = orderRecords(nodes, order);
        const end = performance.now();
        const time = end - start;
        delete nodes
        delete res
        row.push(time)   
      }
      await writeFile(`sort_book_memory_1_2.csv`, row.join()+"\n", { flag: 'a' });

      row = [`sort_book_${num}_2_1`]      

      for (let i of Array(100).keys()){
        const nodes = records["books_instance2_4500"].slice(0, num/2)
            .concat(records["books_instance1_4500"].slice(0, num/2))
        const start = performance.now();
        const res = orderRecords(nodes, order);
        const end = performance.now();
        const time = end - start;
        delete nodes
        delete res
        row.push(time)   
      }
      await writeFile(`sort_book_memory_2_1.csv`, row.join()+"\n", { flag: 'a' });
    }
})();