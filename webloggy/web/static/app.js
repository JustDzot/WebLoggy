function filterLogs() {
    const input = document.getElementById("search");
    const filter = input.value.toLowerCase();
    const logs = document.getElementsByClassName("log");

    for (let i = 0; i < logs.length; i++) {
        const text = logs[i].innerText.toLowerCase();
        logs[i].style.display = text.includes(filter) ? "" : "none";
    }
}