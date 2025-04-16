function updateTimerDisplay(timerText, totalSeconds) {
    const mins = Math.floor(Math.abs(totalSeconds) / 60);
    const secs = Math.abs(totalSeconds) % 60;

    timerText.textContent = `${totalSeconds < 0 ? '-' : ''}${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    if (totalSeconds < 0) {
        timerText.style.color = 'red';
    } else {
        timerText.style.color = '';
    }
}

function startTimer(minutes, seconds, timerTextId) {
    let totalSeconds = minutes * 6 + seconds;

    const interval = setInterval(() => {
        totalSeconds--;
        updateTimerDisplay(document.getElementById(timerTextId), totalSeconds);
    }, 1000);

    updateTimerDisplay(document.getElementById(timerTextId), totalSeconds);
}
