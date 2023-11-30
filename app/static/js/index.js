const uploadFile = document.getElementById("file");
const imagePreview = document.getElementById("imagePreview");
const form = document.getElementById("form");
const errorMessage = document.getElementById("error");

uploadFile.addEventListener("change", (e) => {
  const file = e.target.files[0];

  if (file) {
    const imageURL = URL.createObjectURL(file);
    imagePreview.src = imageURL;
  }
});

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const selectedFile = uploadFile.files[0];

  if (selectedFile) {
    form.submit();
  } else {
    errorMessage.textContent = "Error ! Please provide a pic.";
  }
});
