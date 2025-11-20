async function submitFeedback() {
    const name = document.getElementById("name").value;
    const feedback = document.getElementById("feedback").value;

    const responseMsg = document.getElementById("responseMsg");

    if (!name || !feedback) {
        responseMsg.innerText = "Please fill all fields.";
        return;
    }

    const payload = {
        name: name,
        feedback: feedback,
        timestamp: new Date().toISOString()
    };

    try {
        const response = await fetch("YOUR_API_GATEWAY_URL", {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            responseMsg.innerText = "Feedback submitted successfully!";
            document.getElementById("name").value = "";
            document.getElementById("feedback").value = "";
        } else {
            const text = await response.text();
            responseMsg.innerText = "Error submitting feedback: " + text;
        }
    } catch (err) {
        responseMsg.innerText = "Network error: " + err.message;
    }
}
