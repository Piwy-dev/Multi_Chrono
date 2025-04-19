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

function startTimer(minutes, seconds, teamId) {
    let totalSeconds = minutes * 6 + seconds;

    const interval = setInterval(() => {
        totalSeconds--;
        updateTimerDisplay(document.getElementById('timer-' + teamId), totalSeconds);
    }, 1000);

    updateTimerDisplay(document.getElementById('timer-' + teamId), totalSeconds);

    // Disable the start button
    const startButton = document.getElementById('start-' + teamId);
    console.log(teamId)
    console.log(startButton);
    startButton.disabled = true;
    startButton.style.display = 'none';

    // Enable the stop button
    const stopButton = document.getElementById('stop-' + teamId);
    stopButton.disabled = false;
    stopButton.style.display = 'block';
    
    // Enable the reset button
    const resetButton = document.getElementById('reset-' + teamId);
    resetButton.disabled = false;
    resetButton.style.display = 'block';
}
