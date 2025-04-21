function startChrono(teamId, minutes=0, seconds=0) {
    // Initialize the timer with the provided minutes and seconds
    let totalSeconds = Math.abs(minutes * 60 + seconds);
    const timerText = document.getElementById('chrono-' + teamId);
    updateChronoDisplay(timerText, totalSeconds);

    // Set the timer to update every second
    let interval = setInterval(() => {
        totalSeconds++;
        updateChronoDisplay(document.getElementById('chrono-' + teamId), totalSeconds);
    }, 1000);

    // Store the interval in a global or team-specific variable to allow stopping or resetting
    if (!window.timerIntervals) {
        window.timerIntervals = {};
    }
    window.timerIntervals[teamId] = interval;

    updateChronoDisplay(document.getElementById('chrono-' + teamId), totalSeconds);

    // Disable the start button
    const startButton = document.getElementById('start-' + teamId);
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

    // Disable the restart button
    const restartButton = document.getElementById('restart-' + teamId);
    restartButton.disabled = true;
    restartButton.style.display = 'none';
}

function updateChronoDisplay(chronoText, totalSeconds) {
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    chronoText.innerHTML = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
}

function stopChrono(teamId) {
    // Disable the stop button
    const stopButton = document.getElementById('stop-' + teamId);
    stopButton.disabled = true;
    stopButton.style.display = 'none';

    // Enable the start button
    const startButton = document.getElementById('restart-' + teamId);
    startButton.disabled = false;
    startButton.style.display = 'inline-block';
    
    // Disable the reset button
    const resetButton = document.getElementById('reset-' + teamId);
    resetButton.disabled = false;
    resetButton.style.display = 'inline-block';

    // Clear the interval
    if (window.timerIntervals && window.timerIntervals[teamId]) {
        clearInterval(window.timerIntervals[teamId]);
        delete window.timerIntervals[teamId];
    }
}

function resetChrono(teamId) {
    // Clear the interval
    if (window.timerIntervals && window.timerIntervals[teamId]) {
        clearInterval(window.timerIntervals[teamId]);
        delete window.timerIntervals[teamId];
    }

    // Reset the display
    const chronoText = document.getElementById('chrono-' + teamId);
    chronoText.innerHTML = '0:00';

    // Enable the start button
    const startButton = document.getElementById('start-' + teamId);
    startButton.disabled = false;
    startButton.style.display = 'inline-block';

    // Disable the stop button
    const stopButton = document.getElementById('stop-' + teamId);
    stopButton.disabled = true;
    stopButton.style.display = 'none';

    // Disable the reset button
    const resetButton = document.getElementById('reset-' + teamId);
    resetButton.disabled = true;
    resetButton.style.display = 'none';

    // Enable the restart button
    const restartButton = document.getElementById('restart-' + teamId);
    restartButton.disabled = true;
}

function restartChrono(teamId) {
    // Get the values from the timer display
    const timerText = document.getElementById('chrono-' + teamId);
    const timeParts = timerText.textContent.split(':');
    const minutes = parseInt(timeParts[0], 10);
    const seconds = parseInt(timeParts[1], 10);
    const totalSeconds = Math.abs(minutes * 60 + seconds);
    const newMinutes = Math.floor(totalSeconds / 6);
    const newSeconds = totalSeconds % 6;

    // Restart the timer
    startChrono(teamId, newMinutes, newSeconds);
}