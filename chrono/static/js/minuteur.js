function startCountdown(minutes, seconds, displayElement) {
    let totalSeconds = minutes * 60 + seconds;

    function updateDisplay() {
        const mins = Math.floor(totalSeconds / 60);
        const secs = totalSeconds % 60;
        displayElement.textContent = `${mins}:${secs < 10 ? '0' : ''}${secs}`;
    }

    const interval = setInterval(() => {
        if (totalSeconds <= 0) {
            clearInterval(interval);
            return;
        }
        totalSeconds--;
        updateDisplay();
    }, 1000);

    updateDisplay(); // Initialize display
}

function startCountdowns() {
    const countdowns = document.querySelectorAll('.countdown');
    countdowns.forEach(countdown => {
        const minutes = parseInt(countdown.dataset.minutes, 10);
        const seconds = parseInt(countdown.dataset.seconds, 10);
        startCountdown(minutes, seconds, countdown);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    startCountdowns();
}
);