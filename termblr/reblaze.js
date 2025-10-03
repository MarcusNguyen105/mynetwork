function showToast() {
    const toast = document.getElementById('toast');
    toast.classList.add('show');
    
    setTimeout(() => {
        closeToast();
    }, 5000);
}

function closeToast() {
    const toast = document.getElementById('toast');
    toast.classList.remove('show');
}

document.addEventListener('DOMContentLoaded', function() {
    setTimeout(showToast, 500); 
});