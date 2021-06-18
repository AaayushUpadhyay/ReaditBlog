var a;
function toggle() {
    e = document.querySelector('.comments');
    b=document.querySelector('.view')
  
    if (a == 1) {
        e.style.display = "block";
        b.innerText="Hide Comments";

        return a = 0;

    }
    else {
        e.style.display = "none";
        b.innerText="View Comments";

        return a = 1;

    }




}

