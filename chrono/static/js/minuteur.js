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

    let interval = setInterval(() => {
        totalSeconds--;
        updateTimerDisplay(document.getElementById('timer-' + teamId), totalSeconds);
    }, 1000);

    // Store the interval in a global or team-specific variable to allow stopping or resetting
    if (!window.timerIntervals) {
        window.timerIntervals = {};
    }
    window.timerIntervals[teamId] = interval;

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
    stopButton.style.display = 'inline-block';
    
    // Enable the reset button
    const resetButton = document.getElementById('reset-' + teamId);
    resetButton.disabled = false;
    resetButton.style.display = 'inline-block';
}

function stopTimer(teamId) {
    // Disable the stop button
    const stopButton = document.getElementById('stop-' + teamId);
    stopButton.disabled = true;
    stopButton.style.display = 'none';

    // Enable the start button
    const startButton = document.getElementById('start-' + teamId);
    startButton.disabled = false;
    startButton.style.display = 'inline-block'; 
}

function resetTimer(minutes, seconds, teamId) {
    // Disable the reset button
    const resetButton = document.getElementById('reset-' + teamId);
    resetButton.disabled = true;
    resetButton.style.display = 'none';

    // Enable the start button
    const startButton = document.getElementById('start-' + teamId);
    startButton.disabled = false;
    startButton.style.display = 'inline-block';

    // Disable the stop button
    const stopButton = document.getElementById('stop-' + teamId);   
    stopButton.disabled = true;
    stopButton.style.display = 'none';

    // Reset the timer display
    const timerText = document.getElementById('timer-' + teamId);
    const totalSeconds = minutes * 6 + seconds;
    updateTimerDisplay(timerText, totalSeconds);
    timerText.style.color = '';

    // Clear the interval if it exists
    if (window.timerIntervals && window.timerIntervals[teamId]) {
        clearInterval(window.timerIntervals[teamId]);
        delete window.timerIntervals[teamId];
    }

}