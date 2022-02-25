// HIDE flash message
const message = document.querySelector('.message');

if (message) {
    setTimeout(() =>  message.classList.add("message-off-screen"), 3000);
}


// DELETE {task}
const deletebtn = document.querySelector('.btn-danger');
const closeBtn = document.querySelector('.close-btn');
const confirmBtn = document.querySelector('.confirm-btn');
const overlay = document.querySelector(".overlay");
const modal = document.querySelector('.modal');

function modalOpen() {
    overlay.classList.add('open');
    modal.classList.add('open');
}

function modalClose() {
    overlay.classList.remove("open");
    modal.classList.remove("open");
}

async function handleDelete() {
  try {
    await fetch(`/tasks/${this.dataset.id}/delete`);
    modalClose();
    window.location = '/';
  } catch (error) {
    console.log(error);
  }
}


if (confirmBtn) confirmBtn.addEventListener('click', handleDelete);
if (closeBtn) closeBtn.addEventListener('click', modalClose);
if (deletebtn) deletebtn.addEventListener("click", modalOpen);
