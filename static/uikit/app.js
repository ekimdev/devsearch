// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});

let alertClose = document.querySelectorAll('.alert__close')
let alertWrapper = document.querySelectorAll('.alert')

for (let i=0;i < alertWrapper.length; i++)
{
  alertClose[i].addEventListener('click',()=>{
    alertWrapper[i].style.display = 'none';
  })
}
