function upload() {
    let fileInput = document.getElementById("fileInput").files[0];

    let formData = new FormData();
    formData.append("file", fileInput);

    fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerHTML =
            "Eligible: " + data.eligible.join(", ") + "<br>" +
            "Not Eligible: " + data.not_eligible.join(", ");
    });
}
