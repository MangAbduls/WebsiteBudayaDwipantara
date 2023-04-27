function search() {
    const searchBar = document.getElementById("searchBar").value.toLowerCase();
    const listPulau = document.getElementByID("list-pulau");
    const pulau = document.querySelectorAll(".card");
    const namaPulau = listPulau.getElementsByTagName("h5");

    for (var i = 0; i < namaPulau.length; i++) {
        let match = pulau[i].getElementsByTagName("h5")[0];

        if (match) {
            let textValue = match.textContent || match.innerText;

            if (textValue.toLowerCase().indexOf(searchBar) > -1) {
                pulau[i].style.display = "";
            } else {
                pulau[i].style.display = "none";
            }
        }
    }
}
