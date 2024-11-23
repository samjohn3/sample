function updateClock() {
    const now = new Date();
  
    // Get time components
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
  
    // Get date components
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    const date = now.toLocaleDateString(undefined, options);
  
    // Update the clock
    document.getElementById('digitalClock').textContent = `${hours}:${minutes}:${seconds}`;
    document.getElementById('dateDisplay').textContent = date;
  }
  
  // Update the clock every second
  setInterval(updateClock, 1000);
  
  // Initialize the clock
  updateClock();
  