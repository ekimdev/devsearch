let searchForm = document.getElementById("searchForm");
let pageLinks = document.getElementsByClassName("page-link");

if (searchForm) {
  for (let i = 0; i < pageLinks.length; i++) {
    pageLinks[i].addEventListener("click", (e) => {
      e.preventDefault();

      // data attribute
      let page = e.currentTarget.dataset.page;

      // add hidden search input to form
      searchForm.innerHTML += `<input value=${page} name="page" hidden/>`;

      searchForm.submit();
    });
  }
}
