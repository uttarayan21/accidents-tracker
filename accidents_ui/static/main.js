function toggle_text(e, current, changed) {
  // console.log(e)
  setTimeout(() => {
    // if(e.classList.contains('collapsed')){
    if(e.innerHTML==current) {
      e.innerHTML=changed;
    } else {
      e.innerHTML=current;
    }
  }, 350);
}
