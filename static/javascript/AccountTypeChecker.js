var e = document.getElementById("id_account_type");
var value = e.options[e.selectedIndex].value;
if (value == "Customer") {
    return true;
}