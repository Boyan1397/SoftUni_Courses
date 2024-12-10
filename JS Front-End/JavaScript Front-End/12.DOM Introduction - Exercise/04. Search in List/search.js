function search() {
   let townsElement = document.querySelector('#towns');
   let searchTextElement = document.getElementById('searchText');
   let resultElement = document.getElementById('result');

   let textInput = searchTextElement.value;
   let matches = 0;

   for (let town of townsElement.children) {
      town.style.fontWeight = '';
      town.style.textDecoration = '';
   }

   for (let town of townsElement.children) {
      if (town.textContent.includes(textInput)) {

         matches++;
         town.style.fontWeight = 'bold';
         town.style.textDecoration = 'underline';
      }
   }

   resultElement.textContent = `${matches} matches found`

}
