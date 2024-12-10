function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const trElements = document.querySelectorAll('tbody > tr');
      const searchElement = document.getElementById('searchField');

      let search = searchElement.value;
      if (search === '') return
      
      for (let row of trElements) {
         row.classList.remove('select')
      }

      for (let row of trElements) {
         let tableDescribtions = row.querySelectorAll('td');      
         for (let td of tableDescribtions) {            
            if (td.textContent.includes(search)) {
               row.classList.add('select');
               break
            }             
         }
      }
      // searchElement.value = ''      
   }
}


// function solve() {
//    document.querySelector('#searchBtn').addEventListener('click', onClick);

//    function onClick() {
//       const searchPattern = document.getElementById("searchField").value;
//       const dataCells = Array.from(document.querySelectorAll("tbody td"));

//       const rows = Array.from(document.querySelectorAll("tbody tr"))

//       rows.forEach(row => row.classList.remove("select"));

//       dataCells.forEach(cell => {
//          if (cell.textContent.includes(searchPattern)) {
//             cell.parentElement.classList.add("select")
//          };
//       });
//    };
// }

