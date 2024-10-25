document.getElementById("summarizeButton").onclick = async function () {
    const text = document.getElementById("inputText").value;

    const response = await fetch("/summarize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    });

    const result = await response.json();
    
    if (response.ok) {
        document.getElementById("summaryText").innerText = result.summary;
    } else {
        document.getElementById("summaryText").innerText = "An error occurred while summarizing the text.";
        console.error(result.error); // Log the error to console
    }
};
