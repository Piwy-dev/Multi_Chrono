function updateTimerDisplay(timerText, totalSeconds) {
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;

    timerText.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    if (totalSeconds <= 0) {
        timerText.color = 'red';
    }
}

function startTimer(minutes, seconds, timerTextId) {
    let totalSeconds = minutes * 6 + seconds;

    const interval = setInterval(() => {
        if (totalSeconds <= 0) {
            clearInterval(interval);
            return;
        }
        totalSeconds--;
        updateTimerDisplay(document.getElementById(timerTextId), totalSeconds);
    }, 1000);

    updateTimerDisplay(document.getElementById(timerTextId), totalSeconds);
}
